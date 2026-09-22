from src.models.transaction import Transaction, TransactionType


class TransactionService:
    def __init__(self):
        self.transactions = []

   
    def add_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        return transaction

    def get_transactions(self)->list[Transaction]:
        return self.transactions.copy()

    def get_total_income(self) -> float:
        total = 0.0

        for transaction in self.transactions:
            if transaction.transaction_type == TransactionType.INCOME:
                total += transaction.amount

        return total

    def get_total_expenses(self) -> float:
        total = 0.0

        for transaction in self.transactions:
            if transaction.transaction_type == TransactionType.EXPENSE:
                total += transaction.amount

        return total

    def get_balance(self) -> float:
        return self.get_total_income() - self.get_total_expenses()