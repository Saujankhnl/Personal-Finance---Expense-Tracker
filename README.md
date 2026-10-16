

<img width="1915" height="1090" alt="Screenshot 2026-10-16 183004" src="https://github.com/user-attachments/assets/d80afc54-1886-47fd-8be9-30afe0c24cfa" />
<img width="1917" height="1090" alt="Screenshot 2026-10-16 182959" src="https://github.com/user-attachments/assets/9110e468-3e15-415b-8be0-20039c545195" />
FinTrack — Personal Finance & Expense Tracker
FinTrack is a personal finance web application built with Django and Django REST Framework. It is designed to help users record income and expenses and review their transaction history through a simple web interface.
Project status: In development. Confirm each feature in your local app before describing it as complete.

Features
Implemented / currently being developed
- User registration and login using Django authentication.
- Add income and expense transactions.
- Store transaction details such as title, amount, type, category, date, and description.
- View transaction history through a Django REST Framework API.
- Associate transactions with the authenticated user.
- Use a JavaScript frontend to send requests to the API.
Planned improvements
- Edit and delete transactions from the interface.
- Calculate income, expenses, and balance totals for the dashboard.
- Add date and category filters.
- Add charts and monthly summaries.
- Improve automated tests and form validation.
Tech Stack
- Backend: Python, Django
- API: Django REST Framework (DRF)
- Database: MySQL (configured for the project)
- Frontend: HTML, CSS, JavaScript
- Styling: Tailwind CSS / DaisyUI (if enabled in your current setup)
- Authentication: Django session authentication
- Development tools: VS Code, Git, GitHub
Transaction Data
A transaction includes the following fields:
Field	Description
title	Short transaction name
amount	Transaction amount
transaction_type	income or expense
category	Transaction category
date	Date of the transaction
description	Optional additional details
user	User who owns the transaction


The API assigns the transaction owner from the authenticated session. The API queryset should be restricted to the current user so users cannot view or modify other users' transactions.
Getting Started
1. Clone the repository
Replace the placeholder URL with your GitHub repository URL:
git clone https://github.com/Saujankhnl/Personal-Finance---Expense-Tracker
cd YOUR-REPOSITORY
2. Create and activate a virtual environment
On Windows PowerShell:
python -m venv env
.\env\Scripts\Activate.ps1
If PowerShell blocks activation, you can run commands using the environment's Python executable directly, or follow your system's approved PowerShell execution-policy guidance.
3. Install dependencies
If your project has a requirements.txt file:
pip install -r requirements.txt
If it does not yet exist, install the project's required packages and generate it from the activated environment:
pip install django djangorestframework mysqlclient
pip freeze > requirements.txt
Install any additional packages your project actually uses. Database driver requirements can vary by Windows/Python setup.
4. Configure the database
Create a MySQL database for the project. For example:
CREATE DATABASE personal_finance_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
Configure the database connection in your Django settings using your local MySQL credentials. If you use environment variables, create a local .env file according to your settings implementation.
Never commit database passwords, secret keys, or other credentials to GitHub. Add .env and other local secret files to .gitignore.
5. Apply migrations
From the directory containing manage.py, run:
python manage.py migrate
If your models have changed and migrations are not yet created, run:
python manage.py makemigrations
python manage.py migrate
6. Create an administrator account (optional)
python manage.py createsuperuser
