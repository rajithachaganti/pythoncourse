Today Topic:-
------------
-> Create new table using exising table in db with same table structure
-> Drop table from database
-> Select data using where , group by, having Clauses
-> Wildcard Characters 
	->percent wildcard
	->underscore wildcard
-------------------------------------------------

--How to create table using existing table available in database?

CREATE TABLE employee_copy AS SELECT * FROM emp;

SELECT * FROM employee_copy;

--How to remove or drop table from database?
DROP TABLE employee_copy;


CREATE TABLE employee_copy AS SELECT * FROM emp WHERE 1=1; --with records

DROP TABLE employee_copy;

--How to create the new table with same structure of exising table in db without records?
CREATE TABLE employee_copy AS SELECT * FROM emp WHERE 1=2; --without records

-------------------------------
--working on emp and dept tables:-
-------------------------------
--4.select data using where clause, group by, having and LIKE operator
-------------------------------
SELECT empno,ename,job,sal FROM emp;

--Display employee details of their job is "MANAGER"?
SELECT empno,ename,job,sal FROM emp WHERE job = 'MANAGER';

--Display employee details of their salary is greater than or equal to 3000?
SELECT empno,ename,job,sal FROM emp WHERE sal >=3000; 

--Display employee details of their employee name stars with "J"
SELECT empno,ename,job,sal FROM emp WHERE ename LIKE 'J%'; --Using LIKE operator

--Display total salary of all employees
SELECT SUM(sal) total_sal FROM emp;

--Display total salary and job of all employees based on the job?
SELECT SUM(sal) total_sal,job FROM emp GROUP BY job;

--Display total salary and job of all employees based on the job and total salary is greater than or equal to 5000?
SELECT SUM(sal) total_sal,job FROM emp GROUP BY job HAVING SUM(sal) >=5000;

---==================================================
--------------------------
--5.wildcards (using LIKE operator)
--------------------------
--Display employee details of their employee name stars with letter "C"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE 'C%'; --starts with C

--Display employee details of their employee name ends with letter "S"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '%S'; --end with S

--Display employee details of their employee name contains letters "LA"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '%LA%'; --contains LA

--Display employee details of their employee name doesnot contains letters "LA"
--Using NOT LIKE
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename NOT LIKE '%LA%'; --not contains LA

Requirement:-
--Get total salary of employees job wise.employee name should not starts with C
--and total salary should be greater than or equal to 5000 and display job in descending order.

SELECT SUM(sal) total_sal,job 
FROM emp
WHERE ename NOT LIKE 'C%'
GROUP BY job
HAVING SUM(sal) >=5000
ORDER BY job DESC;

(Using underscore(_)).It represents single character
----------------------------------------------------

Requirement:-
--display employee details and employee name second character should be letter "I".
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '_I%'; 


-----------------
--Structure of SQL Query--
-----------------
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY