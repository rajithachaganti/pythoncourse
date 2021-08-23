Today Topic:
-----------
-> Set Operators

11.SET operators (UNION,UNION ALL,INTERSECT,EXCEPT)

Set operators are used to combines the results of two (or more) SELECT statements.

Rules:-
-----------------------
1.Both the SELECT Statements must be compatible
(same no. of columns and same data type)
2.ORDER BY Clause can occur only at the end of query.
3.GROUP BY and HAVING clauses are allowed only within individual queries.

UNION Operator:-
--------------
It removes duplicate rows.

Each SELECT statement within the UNION operator must have the same number of fields in the result sets with similar data types.

Syntax:-
SELECT columnname1,columnname2 FROM table1
UNION
SELECT columnname1,columnname2 FROM table2;

Example:-1
----------
SELECT
empno,ename,job
FROM
emp
where empno in(7900,7876,7369)
UNION
SELECT 
empno,ename,job
FROM
emp
where empno in(7900,7876,7839)
ORDER BY ename;

Example:-2
----------
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
UNION
SELECT 
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
ORDER BY JOB ASC

Example:-3
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
HAVING JOB = 'MANAGER'
UNION
SELECT 
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
HAVING JOB = 'PRESIDENT'
ORDER BY JOB ASC

Example:-4
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
HAVING JOB = 'MANAGER'
UNION
SELECT 
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
HAVING JOB = 'MANAGER'
ORDER BY JOB ASC

UNION ALL Operator:-
--------------
UNION and UNION ALL are similar in their functioning with a slight difference.
But UNION ALL gives the result set without removing duplication and sorting the data.

Syntax:-
SELECT columnname1,columnname2 FROM table1
UNION ALL
SELECT columnname1,columnname2 FROM table2;
Example:-
SELECT
empno,ename,job
FROM
emp
where empno in(7900,7876,7369)
UNION ALL
SELECT 
empno,ename,job
FROM
emp
where empno in(7900,7876,7839)
ORDER BY 2;

Example:-2
----------
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
UNION ALL
SELECT 
job,SUM(sal) job_wise_total_sal
FROM
emp
GROUP BY job
ORDER BY JOB ASC

INTERSECT Operator:-
------------------
It is used to select common values in a column from tables.

Syntax:-
SELECT columnname1,columnname2 FROM table1
INTERSECT
SELECT columnname1,columnname2 FROM table2;

{A,B,C,D} 
{A,B,E,F}

Common values :A,B

Example:-1

--Query:-1
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
WHERE JOB IN('PRESIDENT','SALESMAN')
GROUP BY job
--Query:-2
INTERSECT
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
WHERE JOB IN('PRESIDENT','SALESMAN','ANALYST')
GROUP BY job

EXCEPT(in place of MINUS in postgreSQL):-
--------------------------------------

The following statement combines results with the EXCEPT operator, which returns only unique rows returned by the first query but not by the second:


SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
WHERE JOB IN('PRESIDENT','SALESMAN','ANALYST')
GROUP BY job
--Query:-2
EXCEPT
SELECT
job,SUM(sal) job_wise_total_sal
FROM
emp
WHERE JOB IN('PRESIDENT','SALESMAN')
GROUP BY job;