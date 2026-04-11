def menu_display():
        print()
        print("Welcome to the Daily Expense Tracker!")
        print()
        print("Menu:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Calculate total and average expense")
        print("4. Clear all expenses")
        print("5. Exit")
        print()
def add_new_expense(expenses):
        num = float(input("Enter your expense: "))
        expenses.append(num)
        print("Expense added successfully!")
def view_all_expenses(expenses):
        if not expenses:
                print("No expenses recorded yet.")
        else:
                print("Your Expenses:")
                for i, value in enumerate(expenses, start = 1):
                        print(f"{i}. {value}")
def total_average (expenses):
        if not expenses:
                print("No expenses recorded yet.")
        else:
                total = 0
                for i, value in enumerate(expenses, start = 1):
                        total += value
                average = total/len(expenses)
                print(f"Total expended: {total}")
                print(f"Average expended: {average}")
def clear_all(expenses):
        expenses.clear()
        print("All expenses cleared")

expenses = []
while True:
        menu_display()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
                add_new_expense(expenses)
                print()
        elif choice == "2":
                view_all_expenses(expenses)
                print()
        elif choice == "3":
                total_average(expenses)
                print()
        elif choice == "4":
                clear_all(expenses)
                print()
        elif choice == "5":
                print("Exiting the Daily Expense Tracker. Goodbye!")
                break
        else:
                print("Invalid choice. Please try again.")
                print()
