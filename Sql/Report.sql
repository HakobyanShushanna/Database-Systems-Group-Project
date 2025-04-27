-- The number of deposits
SELECT COUNT(*) AS number_of_deposits
FROM transaction
WHERE sender_id = %s;

-- The number of withdrawals
SELECT COUNT(*) AS number_of_withdrawals
FROM transaction
WHERE receiver_id = %s;

-- The number of transactions
SELECT COUNT(*) AS total_transactions
FROM transaction
Where sender_id = %s
	or receiver_id = %s;

-- Deposits
SELECT *
FROM transaction
WHERE sender_id = %s;

-- Withdrawals
SELECT *
FROM transaction
WHERE receiver_id = %s;

-- Transactions
SELECT *
FROM transaction
Where sender_id = %s
	or receiver_id = %s;

-- Total amount repaid
SELECT SUM(lr.amount_paid) AS total_amount_repaid
FROM loan_repayment lr
JOIN loan l ON lr.loan_id = l.loan_id
WHERE l.customer_id = %s;

-- Remaining balance
SELECT SUM(lr.remaining_balance) AS total_remaining_balance
FROM loan_repayment lr
JOIN loan l ON lr.loan_id = l.loan_id
WHERE l.customer_id = %s;

-- Repayments
SELECT *
FROM loan_repayment lr
JOIN loan l ON lr.loan_id = l.loan_id
WHERE l.customer_id = %s;

-- Total loan amount
SELECT SUM(loan.amount)
FROM loan
WHERE loan.customer_id = %s;

-- Loans
SELECT *
FROM loan
WHERE loan.customer_id = %s;

-- Cards
SELECT *
from card
where card.customer_id = %s;

-- Accounts
SELECT *
from account
where account.customer_id = %s;

-- No transaction for the last 90 days
SELECT a.account_id
FROM account a
JOIN customer_account ca ON a.account_id = ca.account_id
WHERE ca.customer_id = %s
  AND NOT EXISTS (
    SELECT 1
    FROM transaction t
    WHERE (t.sender_id = %s OR t.receiver_id = %s)
      AND t.transaction_date >= CURRENT_DATE - INTERVAL '90 days'
  );

-- Number of employees by branch
SELECT COUNT(*) AS number_of_employees
FROM branch_employees
WHERE branch_id = %s;

-- Number of customers by bank
SELECT COUNT(*) AS number_of_customers
FROM customer
WHERE bank_id = %s;

-- Number of accounts by bank
SELECT COUNT(*) AS number_of_accounts
FROM account
WHERE bank_id = %s;

-- Number of cards
SELECT COUNT(*) FROM card;

-- Employees by branch
SELECT AS employees
FROM branch_employees
JOIN employee ON employee.employee_id = branch_employees.employee_id
JOIN person ON person.id = employee.employee_id
WHERE branch_id = %s;

-- Customers by bank
SELECT *
FROM customer
WHERE bank_id = %s;

-- Accounts by bank
SELECT *
FROM account
WHERE bank_id = %s;

-- Cards
SELECT * FROM card;