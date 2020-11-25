-- INSERT

-- INSERT INTO <table_name>
-- VALUES <value>
-- INSERT INTO salaries
-- VALUES (id01, 10000, ‘2020-01-01’, ‘2020-10-01’);


-- DELETE
DROP PROCEDURE IF EXISTS employees.DeleteTemporal;

DELIMITER $$
$$
CREATE PROCEDURE employees.DeleteTemporal(
	IN start_date VARCHAR(10), 
	IN end_date VARCHAR(10)
)
BEGIN
	DELETE FROM salaries
	FOR PORTION OF valid_period
	FROM start_date
	TO end_date;
END$$
DELIMITER ;


-- UPDATE (non temporal)

-- UPDATE <table_name>
-- SET 
-- WHERE <condition>
-- UPDATE salaries
-- SET salary = 123456
-- WHERE emp_no = 10001 AND from_date = ‘1987-06-26’ AND to_date = ‘1988-06-25’


-- UPDATE (temporal)
-- UPDATE <table_name> FOR PORTION OF valid_period
-- FROM <start_date>
-- TO <end_date>
-- SET <something>;
-- UPDATE salaries FOR PORTION OF valid_period
-- FROM ‘1986-06-26'
-- TO '1987-06-26'
-- SET salary = 100000
