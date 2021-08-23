Today Topics:-
------------
->Important functions
->Constraints
->Review Assignment2 Queries

CONCAT:-
------
This function allows you to concatenate two strings together.

Syntax:-
-------
CONCAT( string1, string2 )

Example:-
-------
SELECT CONCAT('This is ','SQL') VAL;

Concat with ||:-
-------------
Syntax:-
------
string1 || string2 [ || string_n ]

SELECT 'This is String1'||' String2'||' String3' VAL;

COALESCE();
-----
Syntax:-
COALESCE(e1, e2,..)

The COALESCE() function accepts two arguments. 
If e1 evaluates to null, then COALESCE() function returns e2. 
If e1 evaluates to non-null, the COALESCE() function returns e1.

SELECT ENAME,JOB,SAL,COALESCE(COMM,0) COMM FROM EMP


12.CONSTRAINTS
==============
Constraints are the rules enforced on data columns on table.
These are used to prevent invalid data from being entered into the database.
This ensures the accuracy and reliability of the data in the database.

1.NOT NULL − Ensures that a column cannot have NULL value.

2.UNIQUE − Ensures that all values in a column are different.

3.PRIMARY Key − Uniquely identifies each row/record in a database table.

4.FOREIGN Key − Constrains data based on columns in other tables.

5.CHECK − It ensures that all values in a column satisfy certain conditions.

1.NOT NULL:-
===========
It will not allows to store null values.

Example:-
--------
CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name) values(101,'Ram');
insert into employee(id) values(101);

2.UNIQUE
--------
It will not allows to store duplicate values.

drop table employee;

CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   empno          integer UNIQUE,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name,empno) values(102,'Naveen',1001);
insert into employee(id,name,empno) values(103,'Depak',1001);
insert into employee(id,name,empno) values(103,'Depak',1002);

3.PRIMARY KEY:-
-------------
It will not allows to store null values and duplicate records.

drop table employee;

CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    ,
   empno          integer ,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name,empno) values(101,'Naveen',1001);
insert into employee(id,name,empno) values(101,'Praveen',1002);
insert into employee(id,name,empno) values(null,'Kiran',1003);

4.FOREIGN KEY:-
-------------
 A foreign key means that values in one table must also appear in another table.
 
 The referenced table is called the parent table while the table with the foreign key is called the child table.
 The foreign key in the child table will generally reference a primary key in the parent table.
 
 
select * from emp

select * from dept

CREATE TABLE dept_details
(deptno integer NOT NULL,
 dname varchar(20),
 loc VARCHAR(20),
 CONSTRAINT deptno_pk PRIMARY KEY(deptno)
 );
 
 insert into dept_details values(10,'ACCOUNTING','CHICAGO');
 
 select * from dept_details
 
 CREATE TABLE emp_details
(empno INTEGER NOT NULL,
ename VARCHAR(10),
job VARCHAR(10),
deptno integer NOT NULL,
sal decimal(12,2) NOT NULL,
constraint empno_pk PRIMARY KEY(empno),
constraint deptno_fk FOREIGN KEY(deptno)
REFERENCES dept_details(deptno)
);

INSERT INTO EMP_DETAILS(EMPNO,ENAME,SAL,DEPTNO) VALUES(1001,'Ram',3000.00,10);

INSERT INTO EMP_DETAILS(EMPNO,ENAME,SAL,DEPTNO) VALUES(1002,'Sam',5000.00,10);

ALTER TABLE emp_details
DROP constraint deptno_fk;

ALTER TABLE emp_details
ADD constraint deptno_fk FOREIGN KEY(deptno)
REFERENCES dept_details(deptno);

5.CHECK
-------
It allows you to specify a condition on each row in a table.

CREATE TABLE suppliers
(
  supplier_id integer,
  supplier_name varchar(50),
  CONSTRAINT check_supplier_name
  CHECK (supplier_name = upper(supplier_name))
);

insert into suppliers(supplier_id,supplier_name) values(200,'IBM');

insert into suppliers(supplier_id,supplier_name) values(200,'ibm');