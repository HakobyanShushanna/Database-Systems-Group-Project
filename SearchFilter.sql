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