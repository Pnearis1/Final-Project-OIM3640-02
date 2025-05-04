def get_spending_limit():
    while True:
        try:
            limit = float(input("Set your monthly spending limit ($): "))
            if limit <= 0:
                print("Spending limit must be greater than 0.")
            else:
                return limit
        except ValueError:
            print("Please enter a valid number.")

def alert_user(total_spent, limit):
    percent_used = (total_spent / limit) * 100

    if percent_used >= 100:
        print(f"\n You have exceeded your spending limit!")
        print(f"Total spent: ${total_spent:.2f} / Limit: ${limit:.2f}")
    elif percent_used >= 100 - 0.01:
        print(f"\n You are exactly at your spending limit.")
    elif percent_used >= 80:
        print(f"\n Warning: You're at {percent_used:.1f}% of your spending limit!")
        print(f"Total spent so far: ${total_spent:.2f}")
    else:
        print(f"\n You are within your spending limit. ({percent_used:.1f}% used)")

def track_expenses(limit):
    total_spent = 0
    while True:
        try:
            expense = float(input("Enter expense amount (or 0 to stop): $"))
            if expense < 0:
                print("Expense cannot be negative.")
                continue
            elif expense == 0:
                break
            total_spent += expense
            alert_user(total_spent, limit)
        except ValueError:
            print("Please enter a valid number.")

    print(f"\n Final total spent: ${total_spent:.2f}")
    print(f" Remaining: ${max(0, limit - total_spent):.2f}")
    if total_spent > limit:
        print(" You went over your limit by ${:.2f}".format(total_spent - limit))

def main():
    print("=== Spending Limit Tracker ===")
    limit = get_spending_limit()
    track_expenses(limit)
    print(" Done tracking.")

if __name__ == "__main__":
    main()
