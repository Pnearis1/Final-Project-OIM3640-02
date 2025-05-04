from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Sample expenses
expenses = [
    {"name": "Rent", "amount": 1800, "category": "Housing + utilities", "last_paid": "2025-04-01", "next_due": "2025-05-01"},
    {"name": "Electricity", "amount": 65, "category": "Housing + utilities", "last_paid": "2025-04-10", "next_due": "2025-05-10"},
    {"name": "WIFI", "amount": 50, "category": "Housing + utilities", "last_paid": "2025-04-12", "next_due": "2025-05-12"},
    {"name": "Phone", "amount": 75, "category": "Housing + utilities", "last_paid": "2025-04-12", "next_due": "2025-05-12"},
    {"name": "Gas", "amount": 70, "category": "Housing + utilities", "last_paid": "2025-04-15", "next_due": "2025-05-15"},
    {"name": "Water", "amount": 65, "category": "Housing + utilities", "last_paid": "2025-04-15", "next_due": "2025-05-15"},
    {"name": "Health Insurance", "amount": 300, "category": "Health", "last_paid": "2025-04-05", "next_due": "2025-05-05"},
    {"name": "Dental", "amount": 100, "category": "Health", "last_paid": "2025-04-10", "next_due": "2025-05-10"},
    {"name": "Groceries", "amount": 400, "category": "Housing essentials", "last_paid": "2025-04-20", "next_due": "2025-04-27"},
    {"name": "Toiletries", "amount": 125, "category": "Housing essentials", "last_paid": "2025-04-20", "next_due": "2025-04-27"},
    {"name": "Clothing", "amount": 150, "category": "Housing essentials", "last_paid": "2025-04-20", "next_due": "2025-04-27"},
    {"name": "Credit Card", "amount": 1000, "category": "Debt/finance", "last_paid": "2025-04-12", "next_due": "2025-05-12"},
    {"name": "Venmo", "amount": 160, "category": "Debt/finance", "last_paid": "2025-04-15", "next_due": "2025-05-15"},
    {"name": "Netflix", "amount": 10, "category": "Subscriptions", "last_paid": "2025-04-17", "next_due": "2025-05-17"},
    {"name": "Apple Music", "amount": 10, "category": "Subscriptions", "last_paid": "2025-04-18", "next_due": "2025-05-18"},
    {"name": "Hulu", "amount": 10, "category": "Subscriptions", "last_paid": "2025-04-19", "next_due": "2025-05-19"},   
    {"name": "Amazon Prime", "amount": 10, "category": "Subscriptions", "last_paid": "2025-04-20", "next_due": "2025-05-20"},
    {"name": "Gym", "amount": 40, "category": "Subscriptions", "last_paid": "2025-04-22", "next_due": "2025-05-22"},
    {"name": "HBO Max", "amount": 14, "category": "Subscriptions", "last_paid": "2025-04-23", "next_due": "2025-05-23"},
    {"name": "Paramount+", "amount": 10, "category": "Subscriptions", "last_paid": "2025-04-24", "next_due": "2025-05-24"},
    {"name": "Phone Storage", "amount": 1, "category": "Subscriptions", "last_paid": "2025-04-25", "next_due": "2025-05-25"},
    {"name": "golf", "amount": 45, "category": "Lifestyle", "last_paid": "2025-04-26"},
    {"name": "coffee", "amount": 5, "category": "Lifestyle", "last_paid": "2025-04-26"},
    {"name": "Gas", "amount": 60, "category": "Lifestyle", "last_paid": "2025-04-26"},
    {"name": "Uber", "amount": 75, "category": "Lifestyle", "last_paid": "2025-04-26"},
    {"name": "Concert", "amount": 120, "category": "Lifestyle", "last_paid": "2025-04-26"},
    {"name": "Dining Out", "amount": 120, "category": "Lifestyle", "last_paid": "2025-04-25"},
]

@app.route('/Expenses')
def exp_index():
    categories = {
        "Housing + utilities": [],
        "Health": [],
        "Housing essentials": [],
        "Debt/finance": [],
        "Subscriptions": [],
        "Lifestyle": []
    }

    for expense in expenses:
        if expense["category"] in categories:
            categories[expense["category"]].append(expense)

    return render_template("expense.html", categories=categories)

if __name__ == '__main__':
    app.run(debug=True)