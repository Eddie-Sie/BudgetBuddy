from src.models.transaction import Transaction, TransactionType
from src.services.transaction_service import TransactionService

def create_transaction(transaction_type):
    amount = float(input("Enter amount: "))

    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description (optional): ")

    return Transaction(
        amount,
        category,
        date,
        transaction_type,
        description
    )

def main():
    service = TransactionService()

    while True:
        print("\n========================")
        print("       BudgetBuddy")
        print("========================")
        print("1. Add income")
        print("2. Add expense")
        print("3. View transactions")
        print("4. View financial summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                transaction = create_transaction(TransactionType.INCOME)

                service.add_transaction(transaction)

                print("Income added successfully!")

            except (ValueError, TypeError) as error:
                print(f"Error: {error}")
        elif choice == "2":
            try:
                transaction = create_transaction(TransactionType.EXPENSE)

                service.add_transaction(transaction)

                print("Expense added successfully!")
            
            except (ValueError, TypeError) as error:
                print(f"Error: {error}")
        elif choice == "3":
            transactions = service.get_transactions()

            if not transactions:
                print("No transactions found.")
            else:
                print()
                print(f"{'Date':<12}{'Type':<10}{'Category':<18}{'Amount':<12}{'Description'}")
                print("-" * 70)

                for transaction in transactions:
                    print(
                        f"{transaction.date:<12}"
                        f"{transaction.transaction_type.value:<10}"
                        f"{transaction.category:<18}"
                        f"${transaction.amount:<11.2f}"
                        f"{transaction.description or ''}"
                        )
        elif choice == "4":
                    total_income = service.get_total_income()
                    total_expenses = service.get_total_expenses()
                    balance = service.get_balance()

                    print("\n========== Financial Summary ==========")
                    print(f"Total Income:   ${total_income:.2f}")
                    print(f"Total Expenses: ${total_expenses:.2f}")
                    print(f"Balance:        ${balance:.2f}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()