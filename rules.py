# this code will be used to create budgeting rules and alerts when users get to their spending limit 
# 1. create a budgeting rule that allocates the monlthy income to the respected categories 
#     - savings, expenses, energency + retirment, luquidity 
# 2. create a budgeting rule that alerts the user when they are close to their spending limit
# 3. create a budgeting rule that alerts the user when they are over their spending limit
# 4. create a rule that deletes subscritptions based on user priotirty and budgeting 
#     - create priority list from user input to delete subscriptions when close to spending limit 
# 5. create a user input for custom budgeting rules 
#     - create input for % allocation to each category

def create_budgeting_rule(monthly_income, savings_percentage, expenses_percentage, emergency_retirement_percentage, liquidity_percentage):
    """
    This function creates a budgeting rule that allocates the monthly income to the respective categories.
    """
    # Calculate the allocation for each category
    savings = monthly_income * (savings_percentage / 100)
    expenses = monthly_income * (expenses_percentage / 100)
    emergency_retirement = monthly_income * (emergency_retirement_percentage / 100)
    liquidity = monthly_income * (liquidity_percentage / 100)

    # Create a dictionary to store the allocations
    budget_allocation = {
        'Savings': savings,
        'Expenses': expenses,
        'Emergency + Retirement': emergency_retirement,
        'Liquidity': liquidity
    }

    return budget_allocation

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
    