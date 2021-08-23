Today Topics:-
-------------
-> CASE Statement
-> Alias_name usage
-> ORDER BY Clause
-> DISTINCT keyword
-> Predefined functions
--------------------------
CASE Statement:-
---------------
--Syntax:-

SELECT
CASE 
 WHEN column_name1 = Value1 THEN
 val1
 WHEN column_name1 = Value2 THEN
 Val2
 ELSE
 Val3
END column_n
FROM
table_name;

SELECT empno,ename,job,sal,deptno from emp;

SELECT
 CASE 
  WHEN sal <= 2500 THEN
  sal + 1000
  WHEN sal > 2500 AND sal <= 3000 THEN
  sal + 600
  ELSE
  sal + 400
 END sal_increment,empno,ename,job,sal,deptno
 FROM emp;
  
 --------------
 --Aliases (temporary name)
 --------------
 --Syntax
 SELECT column_name AS alias_name
FROM table_name;

--AS keyword is optional

SELECT column_name alias_name
FROM table_name;

Example:-

SELECT
empno employee_number,
ename employee_name,
job,
sal salary,
deptno department_number
FROM
emp;

--table alias name
SELECT
e.empno employee_number,
e.ename employee_name,
e.job,
sal salary,
deptno department_number
FROM
emp e;

--with multiple table using alias name
SELECT
e.empno employee_number,
e.ename employee_name,
e.job,
sal salary,
d.deptno department_number,
d.dname
FROM
emp e,
dept d
WHERE
e.deptno = d.deptno;

--------------------
---ORDER BY---------
--------------------
SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno

SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno ASC,ename ASC

---------
SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno ASC,ename DESC

--------------------
-----DISTINCT-------
--------------------
--Display job from employee table with unique values
SELECT DISTINCT job from emp; --> Distinct takes more time to execute

SELECT job --> Group by should be use for better performance than DISTINCT
FROM
emp
GROUP BY job;


-------------------
-- 7.Predefined functions
-------------------
1.Aggregate Functions
2.Number Functions
3.Date Functions
4.Conversion Functions
5.Character Functions

--7.1 Aggregate Functions
--SUM --> To get total value

SELECT SUM(sal) total_sal
FROM
emp

--MAX --> To get maximum value
SELECT MAX(sal) max_sal
FROM
emp

--MIN --> To get minimum value
SELECT MIN(sal) min_sal
FROM
emp

--AVG --> To get average value
SELECT ROUND(AVG(sal),2) avg_sal
FROM
emp

--COUNT  --> To get number of records
SELECT COUNT(*) cnt --> * takes more time because it considers all columns
FROM
emp

SELECT COUNT(1) cnt --> consume less time to execute and it consider based on first column
FROM
emp

SELECT COUNT(empno) cnt 
FROM
emp

--7.2 Number Functions
----------------------
--ABS --It converts negative value to positive
Syntax:-
ABS( number )
---
SELECT ABS(-23);

ABS(-23)
Result: 23

ABS(-23.6)
Result: 23.6

ABS(-23.65)
Result: 23.65

ABS(23.65)
Result: 23.65

ABS(23.65 * -1)
Result: 23.65
---

SELECT empno,ename,job,sal, ABS(-45) val from emp;

SELECT empno,ename,job,sal, ABS(54) val from emp;

--ROUND --round to nearest integer
Syntax:-
ROUND( number [, decimal_places] )
---
SELECT ROUND(125.315)
Result: 125

ROUND(125.315, 0)
Result: 125

ROUND(125.315, 1)
Result: 125.3

ROUND(125.315, 2)
Result: 125.32

ROUND(125.315, 3)
Result: 125.315

ROUND(-125.315, 2)
Result: -125.32

SELECT ABS(ROUND(-125.685));
---

SELECT empno,ename,job,sal, ROUND(45.8934,2) val from emp; 

SELECT empno,ename,job,sal, ROUND(45.8994,2) val from emp; 

--TRUNC --truncated the value
Syntax:-
TRUNC( number [, decimal_places] )
---
SELECT TRUNC(125.815)
Result: 125

TRUNC(125.815, 0)
Result: 125

TRUNC(125.815, 1)
Result: 125.8

TRUNC(125.815, 2)
Result: 125.81

TRUNC(125.815, 3)
Result: 125.815
---
SELECT empno,ename,job,sal, TRUNC(45.8934) val from emp; 