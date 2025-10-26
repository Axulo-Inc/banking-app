from typing import Dict, List, Optional
from .account import Account, SavingsAccount, CurrentAccount

class AxizuloAfricanBank:
    """Main banking system class"""
    
    def __init__(self):
        self._name = "Axizulo African Bank"
        self._accounts: Dict[str, Account] = {}
        self._currency = "ZAR"  # South African Rand
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def currency(self) -> str:
        return self._currency
    
    def create_account(self, account_holder: str, account_type: str = "savings", 
                      initial_deposit: float = 0.0, **kwargs) -> Optional[Account]:
        """Create a new bank account"""
        account_holder = account_holder.strip()
        
        if not account_holder:
            print("Account holder name cannot be empty.")
            return None
        
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return None
        
        account = None
        
        if account_type.lower() == "savings":
            interest_rate = kwargs.get('interest_rate', 2.5)
            account = SavingsAccount(account_holder, initial_deposit, interest_rate)
        elif account_type.lower() == "current":
            overdraft_limit = kwargs.get('overdraft_limit', 1000.0)
            account = CurrentAccount(account_holder, initial_deposit, overdraft_limit)
        else:
            print(f"Unknown account type: {account_type}")
            return None
        
        self._accounts[account.account_number] = account
        
        print(f"\n=== Account Created Successfully ===")
        print(f"Bank: {self._name}")
        print(f"Account Holder: {account_holder}")
        print(f"Account Number: {account.account_number}")
        print(f"Account Type: {account_type.title()}")
        print(f"Initial Balance: R{initial_deposit:.2f}")
        print("====================================\n")
        
        return account
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Retrieve account by account number"""
        return self._accounts.get(account_number)
    
    def close_account(self, account_number: str) -> bool:
        """Close an existing account"""
        account = self._accounts.get(account_number)
        
        if not account:
            print("Account not found.")
            return False
        
        if account.balance > 0:
            print(f"Cannot close account with balance. Please withdraw R{account.balance:.2f} first.")
            return False
        
        account.deactivate()
        # In a real system, you might want to remove or archive the account
        print(f"Account {account_number} has been closed.")
        return True
    
    def get_all_accounts(self) -> List[Account]:
        """Get all accounts (for admin purposes)"""
        return list(self._accounts.values())
    
    def get_total_bank_balance(self) -> float:
        """Get total balance of all accounts"""
        return sum(account.balance for account in self._accounts.values())
    
    def transfer_funds(self, from_account_num: str, to_account_num: str, amount: float) -> bool:
        """Transfer funds between accounts"""
        from_account = self._accounts.get(from_account_num)
        to_account = self._accounts.get(to_account_num)
        
        if not from_account or not to_account:
            print("One or both accounts not found.")
            return False
        
        if not from_account.is_active or not to_account.is_active:
            print("One or both accounts are inactive.")
            return False
        
        if amount <= 0:
            print("Transfer amount must be positive.")
            return False
        
        # Withdraw from source account
        if from_account.withdraw(amount, f"Transfer to {to_account_num}"):
            # Deposit to target account
            if to_account.deposit(amount, f"Transfer from {from_account_num}"):
                print(f"Successfully transferred R{amount:.2f} from {from_account_num} to {to_account_num}")
                return True
            else:
                # Rollback withdrawal if deposit fails
                from_account.deposit(amount, "Rollback failed transfer")
                print("Transfer failed. Rolling back transaction.")
                return False
        
        return False
