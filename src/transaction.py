from datetime import datetime
from typing import Dict, Any

class Transaction:
    """Encapsulates transaction data and operations"""
    
    def __init__(self, transaction_id: str, transaction_type: str, amount: float, 
                 description: str = ""):
        self._transaction_id = transaction_id
        self._transaction_type = transaction_type  # 'deposit' or 'withdrawal'
        self._amount = amount
        self._description = description
        self._timestamp = datetime.now()
        self._status = "completed"
    
    # Getters for encapsulation
    @property
    def transaction_id(self) -> str:
        return self._transaction_id
    
    @property
    def transaction_type(self) -> str:
        return self._transaction_type
    
    @property
    def amount(self) -> float:
        return self._amount
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
    
    @property
    def status(self) -> str:
        return self._status
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary for easy serialization"""
        return {
            'transaction_id': self._transaction_id,
            'type': self._transaction_type,
            'amount': self._amount,
            'description': self._description,
            'timestamp': self._timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'status': self._status
        }
    
    def __str__(self) -> str:
        return (f"Transaction {self._transaction_id}: {self._transaction_type} "
                f"of R{self._amount:.2f} at {self._timestamp.strftime('%Y-%m-%d %H:%M')}")
