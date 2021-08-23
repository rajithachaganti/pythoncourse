Today Topics:-
------------
-> Advanced Character functions
-> Operators
-> Joins

--SUBSTR --SUBSTR function allows you to extract a substring from a string.
Syntax:-
SUBSTR( string, start_position [, length ] )
string
	--The source string.
start_position
	--The starting position for extraction. The first position in the string is always 1.
length
	--Optional. It is the number of characters to extract. If this parameter is omitted, the SUBSTR function will return the entire string.
---Examples--
SELECT SUBSTR('This is a test', 6, 2)
Result: 'is'

SUBSTR('This is a test', 6)
Result: 'is a test'

SUBSTR('This is postgreSQL', 9, 10)
Result: 'postgreSQL'

--position --position function is used to find the location of a substring within a specified string.
Syntax:-
POSITION(search_string in main_string) 

search_string	--> The substring which is to be searched.
main_string	    --> The string in which the position of the substring will be detected.

--Example--
SELECT POSITION('SQL' IN 'postgreSQL');
	
---------------------
--8.Operators (Arithmetic, Comparison, Logical, Other Operators(IN, BETWEEN, EXISTS))
---------------------
1.Arithmetic Operators
2.Comparison Operators
3.Logical Operators

--8.1 Arithmetic Operators
-- + (Addition)
SELECT 100 + 2 val;

-- - (Subtraction)

SELECT 100 - 2 val;

-- * (Multiplication)

SELECT 100 * 2 val;

-- / (Division)

SELECT 100/2 val;

--8.2 Comparison Operators
-- < , <= , > , >= <> , =

SELECT empno,ename,job,sal FROM emp WHERE sal < 5000;
 
SELECT empno,ename,job,sal FROM emp WHERE sal <= 5000;

SELECT empno,ename,job,sal FROM emp WHERE sal > 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal >= 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal <> 3000;

		--OR
SELECT empno,ename,job,sal FROM emp WHERE sal != 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal = 3000;

--8.3 Logical Operators
-- AND , OR , NOT

--AND --> To add condition

SELECT empno,ename,job,sal FROM emp WHERE sal = 3000 AND job='ANALYST';

--OR --> Either of condition should be true

SELECT empno,ename,job,sal FROM emp WHERE (sal = 3000 OR sal=5000);

SELECT empno,ename,job,sal FROM emp WHERE ename NOT IN('KING','SCOTT');

--IN --> To check multiple values

SELECT empno,ename,job,sal FROM emp WHERE ename IN('KING','SCOTT');

--BETWEEN --> To check range of values

SELECT * FROM emp WHERE sal BETWEEN 2900 AND 3100;

--================
--9.Joins
--================
1.INNER JOIN (or SIMPLE JOIN)
2.LEFT OUTER JOIN (or LEFT JOIN)
3.RIGHT OUTER JOIN (or RIGHT JOIN)
4.FULL OUTER JOIN (or FULL JOIN)

1.INNER JOIN (or SIMPLE JOIN)
--PostgreSQL INNER JOINS return all rows from multiple tables where the join condition is met.

Syntax:-
SELECT columns
FROM table1 
INNER JOIN table2
ON table1.column = table2.column;


Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
emp e
INNER JOIN dept d
ON e.deptno = d.deptno;

This PostgreSQL INNER JOIN example would return all rows from the emp and dept tables 
where there is a matching deptno value in both the emp and dept tables.

2.LEFT OUTER JOIN (or LEFT JOIN)

--This type of join returns all rows from the LEFT-hand table specified in the left side table and only those rows 
from the right side table where the joined fields are equal (join condition is met).
Syntax:-
SELECT columns
FROM table1
LEFT OUTER JOIN table2
ON table1.column = table2.column;


Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
dept d
LEFT OUTER JOIN emp e
ON e.deptno = d.deptno;

3.RIGHT OUTER JOIN (or RIGHT JOIN)
--This type of join returns all rows from the RIGHT-hand table specified in the left-side table 
and only those rows from right-side table where the joined fields are equal (join condition is met).

Syntax:-
SELECT columns
FROM table1
RIGHT OUTER JOIN table2
ON table1.column = table2.column;

Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
emp e
RIGHT OUTER JOIN dept d
ON e.deptno = d.deptno;

4.FULL OUTER JOIN (or FULL JOIN)

-- This type of join returns all rows from the LEFT-hand table and RIGHT-hand table with nulls in place 
where the join condition is not met.

Syntax:-
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;

Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
emp e
FULL OUTER JOIN dept d
ON e.deptno = d.deptno;

Self Join:-
==========
A self-join is a regular join that joins a table to itself. 
In practice, you typically use a self-join to query hierarchical data or to compare rows within the same table.

To form a self-join, you specify the same table twice with different table aliases.

SELECT
 e.ename employee,
 m.ename manager
FROM
emp e
INNER JOIN emp m
ON e.mgr = m.empno
