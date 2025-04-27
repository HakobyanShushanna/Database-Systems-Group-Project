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