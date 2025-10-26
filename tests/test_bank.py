import unittest
from src.bank import AxizuloAfricanBank
from src.account import SavingsAccount, CurrentAccount

class TestBankingApplication(unittest.TestCase):
    
    def setUp(self):
        self.bank = AxizuloAfricanBank()
        self.test_account = self.bank.create_account("Test User", "savings", 1000.0)
    
    def test_bank_initialization(self):
        self.assertEqual(self.bank.name, "Axizulo African Bank")
        self.assertEqual(self.bank.currency, "ZAR")
    
    def test_account_creation(self):
        self.assertIsNotNone(self.test_account)
        self.assertEqual(self.test_account.account_holder, "Test User")
        self.assertEqual(self.test_account.balance, 1000.0)
        self.assertTrue(self.test_account.is_active)
    
    def test_deposit(self):
        initial_balance = self.test_account.balance
        self.test_account.deposit(500.0)
        self.assertEqual(self.test_account.balance, initial_balance + 500.0)
    
    def test_withdrawal(self):
        initial_balance = self.test_account.balance
        self.test_account.withdraw(200.0)
        self.assertEqual(self.test_account.balance, initial_balance - 200.0)
    
    def test_insufficient_funds(self):
        result = self.test_account.withdraw(2000.0)
        self.assertFalse(result)
    
    def test_transaction_history(self):
        self.test_account.deposit(100.0)
        self.test_account.withdraw(50.0)
        transactions = self.test_account.get_transaction_history()
        self.assertEqual(len(transactions), 3)  # Initial deposit + our two transactions
    
    def test_savings_account_interest(self):
        savings_account = SavingsAccount("Test User", 1000.0, 5.0)
        interest = savings_account.calculate_interest()
        self.assertAlmostEqual(interest, (1000.0 * 5.0) / 100 / 12, places=2)
    
    def test_current_account_overdraft(self):
        current_account = CurrentAccount("Test User", 100.0, 500.0)
        # Try to withdraw more than balance but within overdraft
        result = current_account.withdraw(400.0)
        self.assertTrue(result)
        self.assertEqual(current_account.balance, -300.0)

if __name__ == '__main__':
    unittest.main()
