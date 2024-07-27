import json
import os

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        return json.load(file)

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount):
    expenses = load_expenses()
    expense = {
        'description': description,
        'amount': amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense: {description} - ${amount}")

def view_expenses():
    expenses = load_expenses()
    if expenses:
        print("\nExpenses:")
        total = 0
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['description']} - ${expense['amount']}")
            total += expense['amount']
        print(f"\nTotal Expenses: ${total}")
    else:
        print("No expenses recorded.")

def delete_expense(index):
    expenses = load_expenses()
    if 0 < index <= len(expenses):
        removed_expense = expenses.pop(index - 1)
        save_expenses(expenses)
        print(f"Deleted expense: {removed_expense['description']} - ${removed_expense['amount']}")
    else:
        print("Invalid index. No expense deleted.")

def reset_expenses():
    save_expenses([])
    print("All expenses have been deleted.")

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Reset All Expenses")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            view_expenses()
            index = int(input("Enter the number of the expense to delete: "))
            delete_expense(index)

        elif choice == '4':
            reset_expenses()

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
