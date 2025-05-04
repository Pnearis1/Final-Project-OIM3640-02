def cancel_subscriptions(income, essential_expenses, subscriptions):
    remaining = income - essential_expenses
    print(f"\n Remaining after essentials: ${remaining:.2f}\n")

    total_sub_cost = sum(sub['cost'] for sub in subscriptions)

    if remaining >= total_sub_cost:
        print(" You can afford all your subscriptions.")
        return subscriptions, []

    canceled = []
    kept = []

    for sub in subscriptions:
        if sub['cost'] <= remaining:
            kept.append(sub)
            remaining -= sub['cost']
        else:
            canceled.append(sub)

    return kept, canceled


def main():
    print("=== Smart Subscription Manager ===")

    try:
        income = float(input("Enter your monthly income: $"))
        essential_expenses = float(input("Enter total essential expenses: $"))

        if income <= 0 or essential_expenses < 0:
            print(" Invalid input values.")
            return
    except ValueError:
        print(" Please enter valid numeric inputs.")
        return

    # Priority list: lowest priority first (will cancel these first)
    subscriptions = [
        {"name": "Paramount+", "cost": 10},
        {"name": "HBO Max", "cost": 14},
        {"name": "Apple Music", "cost": 10},
        {"name": "Phone Storage", "cost": 1},
        {"name": "Amazon Prime", "cost": 10},
        {"name": "Netflix", "cost": 15},
        {"name": "Hulu", "cost": 10},
        {"name": "Gym", "cost": 40}
    ]

    kept, canceled = cancel_subscriptions(income, essential_expenses, subscriptions)

    print("\n Subscriptions Kept:")
    for sub in kept:
        print(f" - {sub['name']} (${sub['cost']})")

    print("\n Subscriptions Canceled:")
    if canceled:
        for sub in canceled:
            print(f" - {sub['name']} (${sub['cost']})")
    else:
        print("None canceled.")

    print("\n Subscription management complete.")

if __name__ == "__main__":
    main()
