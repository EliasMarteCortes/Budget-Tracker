# Budget Tracker

A web application built with Django and SQLite that helps you track your income, 
expenses, and budget limits by category.

## Features

- Add, edit, and delete transactions (income or expense)
- Organize transactions by category
- Set monthly budget limits per category
- Dashboard with total income, total expenses, balance, and budget status

## Requirements

- Python 3.x
- Django

## Installation

1. Clone the repository
```
git clone https://github.com/EliasMarteCortes/Budget-Tracker
cd Budget-Tracker/budget_tracker/
```
2. Install Django
```
pip install django
```
3. Run migrations
```
python manage.py migrate
```
4. Start the server
```
python manage.py runserver
```
5. Open your browser and go to
```
http://127.0.0.1:8000/
```
## Usage

1. Go to Categories and add your spending categories (Food, Rent, etc.)
2. Go to Add Transaction to log your income and expenses
3. Go to Budgets to set monthly spending limits per category
4. Check the Dashboard to see your balance and budget status

## Built With

- Python
- Django
- SQLite
