Today Topic:
------------
-> Subqueries

---=================
10.subqueries
---=================
A subquery is a query within a query. You can create subqueries within your SQL statements. These subqueries can reside in the WHERE clause, the FROM clause, or the SELECT clause.

WHERE clause:-
------------
Most often, the subquery will be write in the WHERE clause. These subqueries are also called "Nested subqueries".

Example:-
SELECT
d.*
FROM
dept d
WHERE d.deptno IN(SELECT e.deptno FROM emp e);


SELECT
e.ename,e.job,e.sal
FROM
emp e
WHERE e.deptno IN(SELECT d.deptno FROM dept d);


--How to display highest salary of employee details
SELECT
e.ename,e.job,e.sal
FROM
emp e
WHERE e.sal = (SELECT MAX(e2.sal) FROM emp e2);

--How to display lowest salary of employee details
SELECT
e.ename,e.job,e.sal
FROM
emp e
WHERE e.sal = (SELECT MIN(e2.sal) FROM emp e2);

--How to display lowest salary of employee details including dept name
SELECT
e.ename,e.job,e.sal,d.dname
FROM
emp e
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE e.sal = (SELECT MIN(e2.sal) FROM emp e2);

SELECT
e.ename,e.job,e.sal,d.dname
FROM
emp e
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE ((e.sal =(select max(sal) from emp)) or (e.sal =(SELECT MIN(SAL) FROM EMP)));

SELECT
e.ename,e.job,e.sal,d.dname
FROM
emp e
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE ((e.sal =5000) or (e.sal =3000));

From Clause:-
-----------
A subquery can also be write in the FROM clause. These are called "inline views".

SELECT
e.ename,e.job,e.sal,subquery_dept.dname
FROM
emp e,
(SELECT d.dname,
d.deptno
FROM
dept d) subquery_dept
WHERE
e.deptno = subquery_dept.deptno

SELECT Clause:-
-------------
A subquery can also be write in the SELECT clause.

SELECT
e.ename,e.job,e.sal,
(SELECT d.dname
FROM
dept d
WHERE e.deptno = d.deptno
) dept_name
FROM
emp e;

Types of Subqueries:-
-------------------
1.Single Row Subqueries
2.Multiple Row Subqueries
3.Multiple Column Subqueries

----------
1.Single Row Subqueries
----------
--If the subquery returns single row then we call it as single row subquery.
SELECT
e.ename,e.job,e.sal
FROM
emp e
WHERE e.sal = (SELECT MAX(e2.sal)
				FROM 
				emp e2
			   );

---------
2.Multiple Row Subqueries
---------
--If the subquery returns multiple rows then we call it as multiple row subquery.
--Using "IN" Operator
select * from dept
where deptno IN(select deptno from emp);

--Using "NOT IN" Operator
select * from dept
where deptno NOT IN(select deptno from emp);

--Using "EXISTS" Operator

select d.* from dept d
where EXISTS (select 1 from emp e
WHERE e.deptno = d.deptno);

--Using "NOT EXISTS" Operator

select d.* from dept d
where NOT EXISTS (select 1 
				   from emp e
				   WHERE 
				   e.deptno = d.deptno
				  );

--performance would be better for "EXISTS" Operator than IN Operator.

-----------
3.Multiple Column Subqueries
-----------
--A multiple-column subquery returns more than one column to the outer query
select e.ename,e.job,e.sal
 from emp e
where (e.deptno,e.sal) IN(select e2.deptno,e2.sal 
							from emp e2
							where e2.deptno between 10 AND 20
							AND e2.sal between 800 AND 2900);