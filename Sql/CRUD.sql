-- Register person
INSERT INTO person (first_name, middle_name, last_name, role, phone, email)
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id;

-- Register customer
INSERT INTO customer (customer_id, date_of_birth, created_at, address, bank_id)
VALUES (%s, %s, %s, %s, %s);

-- Register employee
INSERT INTO employee(employee_id, position_id)
values(%s, %s)

-- Add account
INSERT INTO account(balance, status, account_type, created_at, bank_id, customer_id)
VALUES(%s, %s, %s, %s, %s, %s)

-- Add audit_log
INSERT INTO audit_log(employee_id, action, log_date, ip_address)
VALUES(%s, %s, %s, %s)

-- Add bank
INSERT INTO bank(bank_name, bank_address, bank_swift_code)
VALUES(%s, %s, %s)

-- Add beneficiary
INSERT INTO beneficiary(customer_id, beeficiary_name, beneficiary_account_number, bank_id)
VALUES(%s, %s, %s, %s)

-- Add branch
INSERT INTO branch(branch_name, location, contact_number, bank_id, manager_id)
VALUES(%s, %s, %s, %s, %s)

-- Add card
INSERT INTO card(account_id, card_number, card_type, expiry_date, status, cvv, customer_id)
VALUES(%s, %s, %s, %s, %s, %s, %s)

-- Add loan
INSERT INTO loan(customer_id, loan_type, amount, issued_date, due_date, created_at, interest_rate, status)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)

-- Add loan_repayment
INSERT INTO loan_repayment(loan_id, repayment_date, amount_paid, remining_balance, created_at)
VALUES(%s, %s, %s, %s, %s)

-- Add payment
INSERT INTO payment(transaction_id, payment_date, amount, payment_method)
VALUES(%s, %s, %s, %s)

-- Add position
INSERT INTO position(position_name, salary, bank_id)
VALUES(%s, %s, %s)

-- Add transaction
INSERT INTO transaction(sender_id, receiver_id, amount, description, type, transaction_date)
VALUES(%s, %s, %s, %s, %s, %s)

-- Add login
INSERT INTO login (person_id, username, password)
VALUES (%s, %s, %s);

-- Register person
INSERT INTO person (first_name, middle_name, last_name, role, phone, email)
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id;

-- READ person
SELECT id, first_name, middle_name, last_name, role, phone, email
  FROM person
 WHERE id = %s;

-- UPDATE person
UPDATE person
   SET first_name  = %s,
       middle_name = %s,
       last_name = %s,
       role = %s,
       phone = %s,
       email = %s
 WHERE id = %s;

-- DELETE person
DELETE FROM person
 WHERE id = %s;

-- Register customer
INSERT INTO customer (customer_id, date_of_birth, created_at, address, bank_id)
VALUES (%s, %s, %s, %s, %s);

-- READ customer
SELECT customer_id, date_of_birth, created_at, address, bank_id
  FROM customer
 WHERE customer_id = %s;

-- UPDATE customer
UPDATE customer
   SET date_of_birth = %s,
       created_at = %s,
       address = %s,
       bank_id = %s
 WHERE customer_id = %s;

-- DELETE customer
DELETE FROM customer
 WHERE customer_id = %s;

-- Register employee
INSERT INTO employee(employee_id, position_id)
values(%s, %s)

-- READ employee
SELECT employee_id, position_id
  FROM employee
 WHERE employee_id = %s;

-- UPDATE employee
UPDATE employee
   SET position_id = %s
 WHERE employee_id = %s;

-- DELETE employee
DELETE FROM employee
 WHERE employee_id = %s;


-- Add account
INSERT INTO account(balance, status, account_type, created_at, bank_id, customer_id)
VALUES(%s, %s, %s, %s, %s, %s)

-- READ account
SELECT account_id, balance, status, account_type, created_at, customer_id, bank_id
  FROM account
 WHERE account_id = %s;

-- UPDATE account
UPDATE account
   SET balance = %s,
       status = %s,
       account_type = %s,
       created_at = %s,
       customer_id = %s,
       bank_id = %s
 WHERE account_id = %s;

-- DELETE account
DELETE FROM account
 WHERE account_id = %s;


-- Add audit_log 
INSERT INTO audit_log(employee_id, action, log_date, ip_address)
VALUES(%s, %s, %s, %s)

-- READ audit_log
SELECT log_id, employee_id, action, log_date, ip_address
  FROM audit_log
 WHERE log_id = %s;

-- UPDATE audit_log
UPDATE audit_log
   SET employee_id = %s,
       action = %s,
       log_date = %s,
       ip_address = %s
 WHERE log_id = %s;

-- DELETE audit_log
DELETE FROM audit_log
 WHERE log_id = %s;


-- Add bank 
INSERT INTO bank(bank_name, bank_address, bank_swift_code)
VALUES(%s, %s, %s)

-- READ bank
SELECT bank_id, bank_name, bank_address, bank_swift_code
  FROM bank
 WHERE bank_id = %s;

-- UPDATE bank
UPDATE bank
   SET bank_name = %s,
       bank_address = %s,
       bank_swift_code = %s
 WHERE bank_id = %s;

-- DELETE bank
DELETE FROM bank
 WHERE bank_id = %s;

-- Add beneficiary
INSERT INTO beneficiary
  (customer_id, beneficiary_name, beneficiary_account_number, bank_id)
VALUES(%s, %s, %s, %s);

-- READ beneficiary
SELECT beneficiary_id, customer_id, beneficiary_name, beneficiary_account_number, bank_id
  FROM beneficiary
 WHERE beneficiary_id = %s;

-- UPDATE beneficiary 
UPDATE beneficiary
   SET customer_id = %s,
       beneficiary_name = %s,
       beneficiary_account_number = %s,
       bank_id = %s
 WHERE beneficiary_id = %s;

-- DELETE beneficiary
DELETE FROM beneficiary
 WHERE beneficiary_id = %s;


-- Add branch
INSERT INTO branch(branch_name, location, contact_number, bank_id, manager_id)
VALUES(%s, %s, %s, %s, %s)

-- READ branch
SELECT branch_id, branch_name, location, contact_number, bank_id, manager_id
  FROM branch
 WHERE branch_id = %s;

-- UPDATE branch
UPDATE branch
   SET branch_name = %s,
       location = %s,
       contact_number  = %s,
       bank_id = %s,
       manager_id = %s
 WHERE branch_id = %s;

-- DELETE branch
DELETE FROM branch
 WHERE branch_id = %s;


-- Add card
INSERT INTO card(account_id, card_number, card_type, expiry_date, status, cvv, customer_id)
VALUES(%s, %s, %s, %s, %s, %s, %s)

-- READ card
SELECT card_id, account_id, customer_id, card_number, card_type, expiry_date, status, cvv
  FROM card
 WHERE card_id = %s;

-- UPDATE card
UPDATE card
   SET account_id = %s,
       customer_id = %s,
       card_number = %s,
       card_type = %s,
       expiry_date = %s,
       status = %s,
       cvv = %s
 WHERE card_id = %s;

-- DELETE card
DELETE FROM card
 WHERE card_id = %s;


-- Add loan
INSERT INTO loan(customer_id, loan_type, amount, issued_date, due_date, created_at, interest_rate, status)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)

-- READ loan
SELECT loan_id, customer_id, loan_type, amount, issued_date, due_date, created_at, interest_rate, status
  FROM loan
 WHERE loan_id = %s;

-- UPDATE loan
UPDATE loan
   SET customer_id = %s,
       loan_type = %s,
       amount = %s,
       issued_date = %s,
       due_date = %s,
       created_at = %s,
       interest_rate = %s,
       status = %s
 WHERE loan_id = %s;

-- DELETE loan
DELETE FROM loan
 WHERE loan_id = %s;


-- Add loan_repayment
INSERT INTO loan_repayment
  (loan_id, repayment_date, amount_paid, remaining_balance, created_at)
VALUES(%s, %s, %s, %s, %s);

-- READ loan_repayment
SELECT repayment_id, loan_id, repayment_date, amount_paid, remaining_balance, created_at
  FROM loan_repayment
 WHERE repayment_id = %s;

-- UPDATE loan_repayment
UPDATE loan_repayment
   SET loan_id = %s,
       repayment_date = %s,
       amount_paid = %s,
       remaining_balance = %s,
       created_at = %s
 WHERE repayment_id = %s;

-- DELETE loan_repayment
DELETE FROM loan_repayment
 WHERE repayment_id = %s;


-- Add payment
INSERT INTO payment(transaction_id, payment_date, amount, payment_method)
VALUES(%s, %s, %s, %s)

-- READ payment
SELECT payment_id, transaction_id, payment_date, amount, payment_method
  FROM payment
 WHERE payment_id = %s;

-- UPDATE payment
UPDATE payment
   SET transaction_id = %s,
       payment_date = %s,
       amount = %s,
       payment_method = %s
 WHERE payment_id = %s;

-- DELETE payment
DELETE FROM payment
 WHERE payment_id = %s;


-- Add position
INSERT INTO position(position_name, salary, bank_id)
VALUES(%s, %s, %s)

-- READ position
SELECT position_id, position_name, salary, bank_id
  FROM position
 WHERE position_id = %s;

-- UPDATE position
UPDATE position
   SET position_name = %s,
       salary        = %s,
       bank_id       = %s
 WHERE position_id = %s;

-- DELETE position
DELETE FROM position
 WHERE position_id = %s;

-- Add transaction
INSERT INTO transaction(sender_id, receiver_id, amount, description, type, transaction_date)
VALUES(%s, %s, %s, %s, %s, %s)

-- READ transaction
SELECT transaction_id, sender_id, receiver_id, amount, description, type, transaction_date
  FROM transaction
 WHERE transaction_id = %s;

-- UPDATE transaction
UPDATE transaction
   SET sender_id = %s,
       receiver_id = %s,
       amount = %s,
       description = %s,
       type = %s,
       transaction_date = %s
 WHERE transaction_id = %s;

-- DELETE transaction
DELETE FROM transaction
 WHERE transaction_id = %s;


-- Insert into login
INSERT INTO login (person_id, username, password)
VALUES (%s, %s, %s);

-- READ login
SELECT person_id, username, password
  FROM login
 WHERE person_id = %s
   AND username = %s;

-- UPDATE login 
UPDATE login
   SET password = %s
 WHERE person_id = %s
   AND username = %s;

-- DELETE login
DELETE FROM login
 WHERE person_id = %s
   AND username  = %s;