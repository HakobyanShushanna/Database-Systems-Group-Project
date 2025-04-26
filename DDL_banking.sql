CREATE TABLE account (
    account_id SERIAL PRIMARY KEY,
    balance DECIMAL(15, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    CHECK (status IN ('active', 'inactive', 'closed', 'suspended')),
    CHECK (account_type IN ('savings', 'checking', 'business'))
);

CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(75) NOT NULL,
    role VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    CHECK (role IN ('customer', 'employee')),
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    date_of_birth DATE NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES person(id) ON DELETE CASCADE
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    salary NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES person(id) ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION trg_customer_role_check()
RETURNS TRIGGER AS $$
BEGIN
  IF (SELECT role FROM person WHERE id = NEW.customer_id) <> 'customer' THEN
    RAISE EXCEPTION 'person % must have role="customer"', NEW.customer_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER customer_role_must_be_customer
  BEFORE INSERT OR UPDATE ON customer
  FOR EACH ROW
  EXECUTE FUNCTION trg_customer_role_check();

CREATE OR REPLACE FUNCTION trg_employee_role_check()
RETURNS TRIGGER AS $$
BEGIN
  IF (SELECT role FROM person WHERE id = NEW.employee_id) <> 'employee' THEN
    RAISE EXCEPTION 'person % must have role="employee"', NEW.employee_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employee_role_must_be_employee
  BEFORE INSERT OR UPDATE ON employee
  FOR EACH ROW
  EXECUTE FUNCTION trg_employee_role_check();


CREATE TABLE card (
    card_id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,  
    card_number VARCHAR(16) NOT NULL UNIQUE,
    card_type VARCHAR(20) NOT NULL  
		CHECK (card_type IN ('debit', 'credit', 'prepaid')),
    expiry_date  DATE NOT NULL,
    status VARCHAR(20)  NOT NULL  
		CHECK (status IN ('active', 'blocked', 'expired', 'pending')),
    cvv	CHAR(3)	NOT NULL  
		CHECK (cvv ~ '^[0-9]{3}$'),
    FOREIGN KEY (account_id) 
        REFERENCES account(account_id) ON DELETE CASCADE
);

CREATE TABLE customer_card(
	customer_id INT NOT NULL,
	card_id INT NOT NULL,
	PRIMARY KEY (customer_id, card_id),
	FOREIGN KEY (customer_id)
		REFERENCES customer(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (card_id)
		REFERENCES card(card_id) ON DELETE CASCADE
);

CREATE TABLE customer_account(
	customer_id INT NOT NULL,
	account_id INT NOT NULL,
	PRIMARY KEY (customer_id, account_id),
	FOREIGN KEY (customer_id)
		REFERENCES customer(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (account_id)
		REFERENCES account(account_id) ON DELETE CASCADE
);


CREATE TABLE transaction (
    transaction_id SERIAL PRIMARY KEY,
	sender_id INT NOT NULL,
	receiver_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
		CHECK (amount > 0),
    description TEXT,
    type VARCHAR(50) NOT NULL,
    transaction_date TIMESTAMP NOT NULL 
		DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (sender_id)
		REFERENCES customer(customer_id),
	FOREIGN KEY (receiver_id)
		REFERENCES customer(customer_id),
	CHECK (sender_id <> receiver_id)
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    transaction_id INT UNIQUE, 
    payment_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_method VARCHAR(50) NOT NULL 
		CHECK (payment_method IN ('cash', 'credit_card', 'debit_card', 'bank_transfer')),
    FOREIGN KEY (transaction_id) 
		REFERENCES transaction(transaction_id) ON DELETE CASCADE
);

CREATE TABLE loan (
    loan_id SERIAL PRIMARY KEY,
    customer_id INT,  
    loan_type VARCHAR(50)  NOT NULL,
    amount DECIMAL(15,2) NOT NULL
		CHECK (amount > 0),
    issued_date DATE NOT NULL,
    due_date DATE NOT NULL,
    created_at DATE NOT NULL
		DEFAULT CURRENT_DATE,
    interest_rate  DECIMAL(5,2) NOT NULL
		CHECK (interest_rate >= 0),
    status	VARCHAR(20)  NOT NULL
		CHECK (status IN ('pending','active','closed','defaulted')),
    FOREIGN KEY (customer_id)
   		REFERENCES customer(customer_id) ON DELETE CASCADE
);

CREATE TABLE loan_repayment(
	repayment_id SERIAL PRIMARY KEY,
	loan_id INTEGER, 
	repayment_date DATE NOT NULL,
	amount_paid DECIMAL(15,2) NOT NULL
		CHECK (amount_paid > 0),
	remaining_balance DECIMAL(15,2) NOT NULL
		CHECK (remaining_balance >= 0),
	created_at DATE NOT NULL DEFAULT CURRENT_DATE,
	FOREIGN KEY (loan_id)
		REFERENCES loan(loan_id) ON DELETE CASCADE
);

CREATE TABLE audit_log(
	log_id SERIAL PRIMARY KEY,
	employee_id INT NOT NULL,
	action TEXT NOT NULL,
	log_date DATE NOT NULL DEFAULT CURRENT_DATE,
	ip_address INET NOT NULL,
	FOREIGN KEY (employee_id)
		REFERENCES employee(employee_id) ON DELETE CASCADE
);	

CREATE TABLE bank(
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100)  NOT NULL,
    bank_address VARCHAR(255) NOT NULL,
	bank_swift_code VARCHAR(11)  NOT NULL
);

CREATE TABLE branch (
    branch_id SERIAL PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL
		CHECK (contact_number ~ '^[0-9 +()-]+$'),
    bank_id INT NOT NULL
        REFERENCES bank(bank_id),
    manager_id INT NOT NULL
		UNIQUE REFERENCES employee(employee_id) ON DELETE RESTRICT
);

CREATE TABLE branch_employees(
	branch_id INT NOT NULL,
	employee_id INT NOT NULL,
	PRIMARY KEY(branch_id, employee_id),
	FOREIGN KEY(branch_id)
		REFERENCES branch(branch_id) ON DELETE CASCADE,
	FOREIGN KEY(employee_id) 
		REFERENCES employee(employee_id) ON DELETE CASCADE
);

CREATE TABLE beneficiary (
    beneficiary_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    beneficiary_name VARCHAR(100) NOT NULL,
    beneficiary_account_number VARCHAR(30) NOT NULL,
    bank_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (bank_id) REFERENCES bank(bank_id) ON DELETE RESTRICT
);




