-- Is Employee
SELECT 1 FROM employee WHERE employee_id = %s;

-- Is Customer
SELECT 1 FROM customer WHERE customer_id = %s;

-- Get login info
SELECT person_id, password
FROM login
WHERE username = %s;