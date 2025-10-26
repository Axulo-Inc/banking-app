from src.bank import AxizuloAfricanBank
from src.account import Account
import sys

class BankingApp:
    """Main banking application interface"""
    
    def __init__(self):
        self.bank = AxizuloAfricanBank()
    
    def display_menu(self):
        """Display main menu"""
        print(f"\n{'='*50}")
        print(f"    WELCOME TO {self.bank.name.upper()}")
        print(f"{'='*50}")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Transfer Funds")
        print("7. View Account Information")
        print("8. Exit")
        print(f"{'='*50}")
    
    def create_account_flow(self):
        """Handle account creation flow"""
        print("\n--- Create New Account ---")
        
        account_holder = input("Enter account holder name: ")
        if not account_holder:
            print("Account holder name is required.")
            return
        
        print("\nAccount Types:")
        print("1. Savings Account (2.5% interest)")
        print("2. Current Account (R1000 overdraft)")
        
        account_type_choice = input("Choose account type (1 or 2): ")
        
        if account_type_choice == "1":
            account_type = "savings"
        elif account_type_choice == "2":
            account_type = "current"
        else:
            print("Invalid choice. Defaulting to Savings Account.")
            account_type = "savings"
        
        try:
            initial_deposit = float(input("Enter initial deposit amount (R): "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative. Setting to R0.00")
                initial_deposit = 0.0
        except ValueError:
            print("Invalid amount. Setting initial deposit to R0.00")
            initial_deposit = 0.0
        
        account = self.bank.create_account(account_holder, account_type, initial_deposit)
        
        if account:
            print(f"✅ Account created successfully! Your account number is: {account.account_number}")
    
    def get_account_input(self) -> Account:
        """Get account number input and return account object"""
        account_number = input("Enter account number: ").strip().upper()
        account = self.bank.get_account(account_number)
        
        if not account:
            print("Account not found. Please check the account number.")
        
        return account
    
    def deposit_flow(self):
        """Handle deposit flow"""
        print("\n--- Deposit Money ---")
        account = self.get_account_input()
        
        if not account:
            return
        
        try:
            amount = float(input("Enter deposit amount (R): "))
            description = input("Enter description (optional): ")
            
            if not description:
                description = "Deposit"
            
            account.deposit(amount, description)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    def withdraw_flow(self):
        """Handle withdrawal flow"""
        print("\n--- Withdraw Money ---")
        account = self.get_account_input()
        
        if not account:
            return
        
        try:
            amount = float(input("Enter withdrawal amount (R): "))
            description = input("Enter description (optional): ")
            
            if not description:
                description = "Withdrawal"
            
            account.withdraw(amount, description)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    def check_balance_flow(self):
        """Handle balance check flow"""
        print("\n--- Check Balance ---")
        account = self.get_account_input()
        
        if not account:
            return
        
        balance = account.get_balance()
        print(f"Account Balance: R{balance:.2f}")
    
    def transaction_history_flow(self):
        """Handle transaction history flow"""
        print("\n--- Transaction History ---")
        account = self.get_account_input()
        
        if not account:
            return
        
        transactions = account.get_transaction_history()
        
        if not transactions:
            print("No transactions found.")
            return
        
        print(f"\nTransaction History for Account {account.account_number}:")
        print("-" * 60)
        for transaction in transactions:
            transaction_data = transaction.to_dict()
            print(f"{transaction_data['timestamp']} - {transaction_data['type'].upper():10} "
                  f"R{transaction_data['amount']:8.2f} - {transaction_data['description']}")
        print("-" * 60)
    
    def transfer_flow(self):
        """Handle fund transfer flow"""
        print("\n--- Transfer Funds ---")
        
        from_account_num = input("Enter your account number: ").strip().upper()
        to_account_num = input("Enter recipient account number: ").strip().upper()
        
        try:
            amount = float(input("Enter transfer amount (R): "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        
        self.bank.transfer_funds(from_account_num, to_account_num, amount)
    
    def account_info_flow(self):
        """Handle account information flow"""
        print("\n--- Account Information ---")
        account = self.get_account_input()
        
        if not account:
            return
        
        info = account.get_account_info()
        
        print(f"\nAccount Information:")
        print(f"Bank: {self.bank.name}")
        print(f"Account Number: {info['account_number']}")
        print(f"Account Holder: {info['account_holder']}")
        print(f"Account Type: {info['account_type']}")
        print(f"Balance: R{info['balance']:.2f}")
        print(f"Status: {'Active' if info['is_active'] else 'Inactive'}")
        
        # Additional info based on account type
        if hasattr(account, 'interest_rate'):
            print(f"Interest Rate: {account.interest_rate}%")
        if hasattr(account, 'overdraft_limit'):
            print(f"Overdraft Limit: R{account.overdraft_limit:.2f}")
    
    def run(self):
        """Main application loop"""
        print(f"🚀 Starting {self.bank.name} Banking Application...")
        
        while True:
            self.display_menu()
            
            choice = input("Enter your choice (1-8): ").strip()
            
            try:
                if choice == "1":
                    self.create_account_flow()
                elif choice == "2":
                    self.deposit_flow()
                elif choice == "3":
                    self.withdraw_flow()
                elif choice == "4":
                    self.check_balance_flow()
                elif choice == "5":
                    self.transaction_history_flow()
                elif choice == "6":
                    self.transfer_flow()
                elif choice == "7":
                    self.account_info_flow()
                elif choice == "8":
                    print(f"\nThank you for banking with {self.bank.name}!")
                    print("Goodbye! 👋")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter a number between 1-8.")
            
            except KeyboardInterrupt:
                print(f"\n\nThank you for banking with {self.bank.name}!")
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = BankingApp()
    app.run()
