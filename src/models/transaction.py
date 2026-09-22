from enum import Enum
from typing import Optional

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"



class Transaction:
    def __init__(
        self,
        amount: float,
        category: str,
        date: str,
        transaction_type: TransactionType,
        description: Optional[str] = None,
    ):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero.')
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.transaction_type = transaction_type