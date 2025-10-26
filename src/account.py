from typing import List, Optional, Dict, Any
import uuid
from .transaction import Transaction

class Account:
    """Base account class with common banking functionality"""
    
    def __init__(self, account_holder: str, initial_deposit: float = 0.0):
        self._account_number = str(uuid.uuid4())[:8].upper()
        self._account_holder = account_holder
        self._balance = max(0.0, initial_deposit)  # Prevent negative initial deposit
        self._transaction_history: List[Transaction] = []
        self._is_active = True
        
        # Record initial deposit if any
        if initial_deposit > 0:
            transaction = Transaction(
                transaction_id=str(uuid.uuid4())[:6].upper(),
                transaction_type="deposit",
                amount=initial_deposit,
                description="Initial deposit"
            )
            self._transaction_history.append(transaction)
    
    # Encapsulated getters
    @property
    def account_number(self) -> str:
        return self._account_number
    
    @property
    def account_holder(self) -> str:
        return self._account_holder
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money into account"""
        if not self._is_active:
            print("Account is inactive. Cannot deposit.")
            return False
        
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        
        self._balance += amount
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4())[:6].upper(),
            transaction_type="deposit",
            amount=amount,
            description=description
        )
        self._transaction_history.append(transaction)
        
        print(f"Successfully deposited R{amount:.2f}. New balance: R{self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Withdraw money from account"""
        if not self._is_active:
            print("Account is inactive. Cannot withdraw.")
            return False
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self._balance:
            print("Insufficient funds.")
            return False
        
        self._balance -= amount
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4())[:6].upper(),
            transaction_type="withdrawal",
            amount=amount,
            description=description
        )
        self._transaction_history.append(transaction)
        
        print(f"Successfully withdrew R{amount:.2f}. New balance: R{self._balance:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Check current balance"""
        return self._balance
    
    def get_transaction_history(self) -> List[Transaction]:
        """Get transaction history (encapsulated)"""
        return self._transaction_history.copy()  # Return copy to maintain encapsulation
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information as dictionary"""
        return {
            'account_number': self._account_number,
            'account_holder': self._account_holder,
            'balance': self._balance,
            'is_active': self._is_active,
            'account_type': self.__class__.__name__
        }
    
    def deactivate(self) -> None:
        """Deactivate account"""
        self._is_active = False
        print("Account has been deactivated.")
    
    def activate(self) -> None:
        """Activate account"""
        self._is_active = True
        print("Account has been activated.")


class SavingsAccount(Account):
    """Savings account with interest functionality"""
    
    def __init__(self, account_holder: str, initial_deposit: float = 0.0, interest_rate: float = 2.5):
        super().__init__(account_holder, initial_deposit)
        self._interest_rate = interest_rate
    
    @property
    def interest_rate(self) -> float:
        return self._interest_rate
    
    def calculate_interest(self) -> float:
        """Calculate monthly interest"""
        return (self._balance * self._interest_rate) / 100 / 12
    
    def apply_interest(self) -> bool:
        """Apply monthly interest to account"""
        interest = self.calculate_interest()
        if interest > 0:
            return self.deposit(interest, "Monthly interest")
        return True


class CurrentAccount(Account):
    """Current account with overdraft facility"""
    
    def __init__(self, account_holder: str, initial_deposit: float = 0.0, overdraft_limit: float = 1000.0):
        super().__init__(account_holder, initial_deposit)
        self._overdraft_limit = overdraft_limit
    
    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Override withdraw to allow overdraft within limit"""
        if not self._is_active:
            print("Account is inactive. Cannot withdraw.")
            return False
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        available_balance = self._balance + self._overdraft_limit
        
        if amount > available_balance:
            print(f"Insufficient funds. Available: R{available_balance:.2f}")
            return False
        
        self._balance -= amount
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4())[:6].upper(),
            transaction_type="withdrawal",
            amount=amount,
            description=description
        )
        self._transaction_history.append(transaction)
        
        print(f"Successfully withdrew R{amount:.2f}. New balance: R{self._balance:.2f}")
        return True
