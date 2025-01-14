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


DROP PROCEDURE IF EXISTS employees.projection;

DELIMITER $$
$$
CREATE PROCEDURE `employees`.`projection`(
IN table_name VARCHAR(15), 
IN column_name VARCHAR(15))
BEGIN
	SET @sql = CONCAT('SELECT ',column_name, ', from_date, to_date FROM ', table_name);
	PREPARE stmt FROM @sql;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
END$$
DELIMITER ;


-- TEMPORAL UNION

-- SELECT <primary_key>, MIN(from_date) as from_date, MAX(to_date) as to_date
-- FROM
-- (SELECT * from <table_name>
-- UNION
-- SELECT * FROM <table_name>) AS u
-- GROUP BY <primary_key>


-- TEMPORAL DIFFERENCE

-- SELECT <primary_key>, MIN(from_date) as from_date, MAX(to_date) as to_date
-- FROM
-- (SELECT * from <table_name>
-- EXCEPT
-- SELECT * FROM <table_name>) AS d
-- GROUP BY <primary_key>


-- TEMPORAL JOIN

-- SELECT <column-name>
--   IF(<t1.from_date> >= <t2.from_date>,
--     <t1.from_date>, <t2.from_date>)
--       AS from_date,
--   IF(<t1.to_date> <= <t2.to_date>,
--     <t1.to_date>, <t2.to_date>)
--       AS to_date
-- FROM <t1> INNER JOIN <t2>
-- ON <t1.column_name> = <t2.column_name>
