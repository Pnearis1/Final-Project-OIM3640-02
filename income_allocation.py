
# this code is a simple program that helps users allocate their remaining income after expenses into different categories: retirement, emergency fund, and liquidity. It ensures that the user inputs valid percentages that total 100% and provides an alert system for spending limits.
def get_valid_percentage_input():
    print("\nEnter the percentage you'd like to allocate for each category (must total 100%).")
    
    while True:
        try:
            retirement_pct = float(input("Retirement Fund (%): "))
            emergency_pct = float(input("Emergency Fund (%): "))
            liquidity_pct = float(input("Liquidity (%): "))

            total = retirement_pct + emergency_pct + liquidity_pct

            if abs(total - 100) > 0.001:
                print(f"\n❌ Total is {total}%. It must equal 100%. Please try again.\n")
                continue

            return {
                "retirement": retirement_pct,
                "emergency": emergency_pct,
                "liquidity": liquidity_pct
            }

        except ValueError:
            print("⚠️ Please enter valid numbers.\n")


def allocate_remaining_income(remaining_income, allocation_percentages):
    allocation = {}
    for category, pct in allocation_percentages.items():
        allocation[category] = round(remaining_income * (pct / 100), 2)
    return allocation


def main():
    print("=== Income Allocation After Expenses ===")
    try:
        income = float(input("Enter your monthly income: $"))
        expenses = float(input("Enter your total monthly expenses: $"))

        if income <= 0 or expenses < 0:
            print(" Income must be greater than 0 and expenses cannot be negative.")
            return

        if expenses > income:
            print("Expenses exceed income. There's no money left to allocate.")
            return

        remaining = round(income - expenses, 2)
        print(f"\nYou have ${remaining:.2f} left after expenses.")

    except ValueError:
        print(" Invalid input. Please enter numbers.")
        return

    percentages = get_valid_percentage_input()
    result = allocate_remaining_income(remaining, percentages)

    print("\n--- Allocation Summary ---")
    for category, amount in result.items():
        print(f"{category.title()}: ${amount:.2f}")

    print("\n Allocation complete based on your preferences.")

def alert_spending_limit(current_spending, spending_limit):
    """
    This function alerts the user when they are close to their spending limit or over it.
    """
    if current_spending >= spending_limit:
        return "Alert: You have exceeded your spending limit!"
    elif current_spending >= spending_limit * 0.9:
        return "Alert: You are close to your spending limit!"
    else:
        return "You are within your spending limit."
    
if __name__ == "__main__":
    main()