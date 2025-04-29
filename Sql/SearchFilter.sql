-- Banks list
SELECT bank_id, bank_name FROM bank;

-- Roles list
SELECT position_id, position_name
FROM position
WHERE bank_id = %s

-- Branches list
SELECT branch_id, branch_name
FROM branch
WHERE bank_id = %s;

-- Customers list
SELECT * FROM customer
JOIN person ON person.id = customer.person_id;

-- Employees list
SELECT * FROM employee
JOIN person ON person.id = employee.employee_id;

-- Customer
SELECT * FROM customer
JOIN person ON customer.customer_id = person.id
WHERE customer.customer_id = %s;

-- Employee
SELECT * FROM employee
JOIN person ON employee.employee_id = person.id
WHERE employee.employee_id = %s;

-- Person
SELECT * FROM person
WHERE person.id = %s;

-- Login
SELECT * FROM login
WHERE login.username = %s
	AND login.password = %s;

-- Customers for admin
SELECT id, first_name, middle_name, last_name 
FROM person WHERE person.role = 'customer'
ORDER BY last_name;


-- Employees for admin
SELECT id, first_name, middle_name, last_name 
FROM person WHERE person.role <> 'customer'
ORDER BY last_name;