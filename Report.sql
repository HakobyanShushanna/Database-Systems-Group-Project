-- The number of Deposits
SELECT COUNT(*) AS number_of_deposits
FROM transaction
WHERE sender_id = %s;

-- The number of withdrawls
SELECT COUNT(*) AS number_of_withdrawals
FROM transaction
WHERE receiver_id = %s;

-- The total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transaction
Where sender_id = %s
	or receiver_id = %s;

-- Total amount repaid
SELECT SUM(lr.amount_paid) AS total_amount_repaid
FROM loan_repayment lr
JOIN loan l ON lr.loan_id = l.loan_id
WHERE l.customer_id = %s;

-- remaining balance
SELECT SUM(lr.remaining_balance) AS total_remaining_balance
FROM loan_repayment lr
JOIN loan l ON lr.loan_id = l.loan_id
WHERE l.customer_id = %s;

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

-- Number of Employees
SELECT COUNT(*) AS number_of_employees
FROM branch_employees
WHERE branch_id = %s;

-- Number of Customers
SELECT COUNT(*) AS number_of_customers
FROM customer
WHERE bank_id = %s;

-- Number of Accounts
SELECT COUNT(*) AS number_of_accounts
FROM account
WHERE bank_id = %s;