import unittest

from src.models.transaction import Transaction, TransactionType
from src.services.transaction_service import TransactionService


class TestTransactionService(unittest.TestCase):

    def test_add_transaction(self):
        service = TransactionService()

        transaction = Transaction(
            25.00,
            "Food",
            "2026-09-22",
            TransactionType.EXPENSE,
            "Lunch"
        )

        added_transaction = service.add_transaction(transaction)

        self.assertIs(added_transaction, transaction)
        self.assertEqual(len(service.transactions), 1)
        self.assertIs(service.transactions[0], transaction)

    def test_get_transactions_returns_copy(self):
        service = TransactionService()

        transaction = Transaction(
            25.00,
            "Food",
            "2026-09-22",
            TransactionType.EXPENSE,
            "Lunch"
        )

        service.add_transaction(transaction)

        transactions = service.get_transactions()

        self.assertEqual(len(transactions), 1)
        self.assertIs(transactions[0], transaction)

        transactions.clear()

        self.assertEqual(len(transactions), 0)
        self.assertEqual(len(service.transactions), 1)

    def test_get_total_income(self):
        service = TransactionService()

        salary = Transaction(
            1500.00,
            "Salary",
            "2026-09-22",
            TransactionType.INCOME
        )

        scholarship = Transaction(
            500.00,
            "Education",
            "2026-09-22",
            TransactionType.INCOME
        )

        food = Transaction(
            50.00,
            "Food",
            "2026-09-22",
            TransactionType.EXPENSE
        )

        service.add_transaction(salary)
        service.add_transaction(scholarship)
        service.add_transaction(food)

        self.assertEqual(service.get_total_income(), 2000.00)

    def test_get_total_expenses(self):
        service = TransactionService()

        food = Transaction(
            50.00,
            "Food",
            "2026-09-22",
            TransactionType.EXPENSE
        )

        transportation = Transaction(
            30.00,
            "Transportation",
            "2026-09-22",
            TransactionType.EXPENSE
        )

        salary = Transaction(
            1500.00,
            "Salary",
            "2026-09-22",
            TransactionType.INCOME
        )

        service.add_transaction(food)
        service.add_transaction(transportation)
        service.add_transaction(salary)

        self.assertEqual(service.get_total_expenses(), 80.00)

    def test_get_balance(self):
        service = TransactionService()

        salary = Transaction(
            2000.00,
            "Salary",
            "2026-09-22",
            TransactionType.INCOME
        )

        food = Transaction(
            150.00,
            "Food",
            "2026-09-22",
            TransactionType.EXPENSE
        )

        transportation = Transaction(
            50.00,
            "Transportation",
            "2026-09-22",
            TransactionType.EXPENSE
        )

        service.add_transaction(salary)
        service.add_transaction(food)
        service.add_transaction(transportation)

        self.assertEqual(service.get_balance(), 1800.00)

if __name__ == "__main__":
    unittest.main()