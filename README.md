# Banking App - Database Systems Project

This project is part of the Database Systems class, where we implemented a banking system with a PostgreSQL backend. The application allows customers to manage accounts, transactions, loans, and more, while also keeping track of employee actions in an audit log.

## Features

- **Customer Profiles**: Store and manage customer information, including personal details, accounts, cards, transactions, loans, and repayments.
- **Account Management**: Create and manage customer accounts, including deposit and withdrawal functionalities.
- **Card Management**: Issue and manage customer cards with details like card number, type, expiry date, and status.
- **Transaction Management**: Track transactions (deposits, withdrawals, etc.) between customers, including detailed logs.
- **Loan Management**: Handle loans, including applying for loans and tracking repayments.
- **Audit Logs**: Track actions performed by employees, such as account updates or loan approvals.
- **Beneficiary Management**: Link customers to their beneficiaries for easy fund transfers.

## Database Design

The app uses **PostgreSQL** to store and manage data. Below is an overview of the tables used in the system:

### Key Tables

1. **bank**: Stores information about banks (bank name, address, SWIFT code).
2. **customer**: Stores customer information, linked to the `person` table.
3. **employee**: Stores employee data, linked to positions.
4. **account**: Stores customer account details, including balance and status.
5. **transaction**: Tracks customer transactions (deposits, withdrawals, etc.).
6. **loan**: Stores loan information, including type, amount, status, and repayment schedule.
7. **loan_repayment**: Tracks loan repayments and remaining balances.
8. **audit_log**: Logs employee actions related to customer accounts and transactions.
9. **branch**: Stores bank branches, each linked to an employee as a manager.
10. **branch_employees**: Stores employees assigned to specific branches.
11. **beneficiary**: Links customers to their beneficiaries for transaction purposes.

### Foreign Key Relationships

- **customer** table references `person.id` (for customer details).
- **employee** references `person.id` (for employee details).
- **transaction** has `sender_id` and `receiver_id` referencing `customer.id`.
- **loan** references `customer.id`.
- Other tables maintain foreign key relationships for integrity (e.g., `bank_id`, `position_id`).

## Database Setup

To set up the PostgreSQL database for this app, follow these steps:

1. **Create the PostgreSQL Database**:
   
   If you haven't already, create a new PostgreSQL database by running:

   ```sql
   CREATE DATABASE banking_app;
   ```

2. **Set Up the Tables**:

   After setting up your database, execute the SQL script (`Sql/DDL_banking.sql`) to create the necessary tables..

   ```bash
   psql -U username -d banking_app -f Sql/DDL_banking.sql
   ```

   Ensure you replace `username` with your PostgreSQL username.

3. **Configuring Database Connection**:

   In your `config.py`, set the connection parameters for PostgreSQL. Here is an example:

   ```python
   DB_PARAMS = {
       "host": "localhost",
       "dbname": "banking_app",
       "user": "your_username",
       "password": "your_password"
   }
   ```

   **Warning**: **DO NOT** forget to change these parameters to match your local or production PostgreSQL instance before running the app.

4. **Connecting to PostgreSQL using psycopg2**:

   The app uses `psycopg2` for database connectivity. The database connection is managed by the `psycopg2.connect()` function. Here's an example of how the connection is established:

   ```python
   import psycopg2
   from config import DB_PARAMS

   def get_connection():
       return psycopg2.connect(
           host=DB_PARAMS["host"],
           dbname=DB_PARAMS["dbname"],
           user=DB_PARAMS["user"],
           password=DB_PARAMS["password"]
       )
   ```

   You can call `get_connection()` in various modules of the app to interact with the database.

## Project Structure

Here's a brief overview of the project directory structure:

```
.
├── Sql/                     # SQL scripts for creating tables
│   └── Report.sql           # SQL script for creating the banking app schema
├── Models/                  # Python models for interacting with the database
│   ├── customer_model.py    # Customer-related model
│   ├── card_model.py        # Card-related model
│   ├── account_model.py     # Account-related model
│   ├── transaction_model.py # Transaction-related model
├── Logic/                   # Business logic for managing customer actions
│   ├── Customer.py          # Customer logic (transactions, loans, etc.)
│   ├── Register.py          # Register logic (for both employees and customers)
├── config.py                # Configuration file (Database settings)
├── main.py                  # Main Streamlit app
└── README.md                # Project documentation
```

## Dependencies

Ensure you have the required dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

Required dependencies include:

- `psycopg2`: PostgreSQL database adapter for Python.
- `streamlit`: For building the web interface.
- `datetime`: For handling date and time.
- Any other libraries you might have used.

## Running the App

Once you have configured your database and installed the dependencies, you can run the Streamlit app using:

```bash
streamlit run app.py
```

The app will start locally and be accessible via `http://localhost:8501`.
