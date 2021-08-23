Example:-  

CREATE TABLE students_table(
student_id integer,
student_name varchar(100),
branch varchar(50)
);

INSERT INTO students_table VALUES(100101,'Ram','ECE');

INSERT INTO students_table VALUES(100102,'Ravi','EEE');

INSERT INTO students_table VALUES(100103,'Swaroop','CSE');

INSERT INTO students_table VALUES(100104,'Naveen','ECE');

SELECT student_id,student_name,branch FROM students_table;

UPDATE students_table SET branch = 'CSE' WHERE student_id = 100104;

SELECT student_id,student_name,branch FROM students_table;

DELETE FROM students_table where student_name = 'Ravi';

SELECT student_id,student_name,branch FROM students_table;

DROP TABLE students_table;

DML (Data manupulation language)
INSERT
UPDATE
DELETE


DDL (Data definition language)
CREATE
DROP
ALTER