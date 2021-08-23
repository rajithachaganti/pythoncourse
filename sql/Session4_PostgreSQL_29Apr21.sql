Today Topics:
-----------
-> Date Functions
-> Conversion Functions
-> Character Functions

--7.3 Date Functions
--------------------

SELECT empno,ename,job,sal, CURRENT_DATE today_date from emp; --current date

SELECT empno,ename,job,sal, CURRENT_TIME today_time from emp; --current time with time zone

SELECT empno,ename,job,sal, now() today_date_time from emp; --current timestamp with time zone

--========================
--7.4 Conversion Functions
--========================

--PostgreSQL TO_DATE Function: Convert String to Date
--Conversion Functions
Syntax:-
TO_DATE(text,format_mask);
--The TO_DATE() function accepts two string arguments.The first argument is string
--that you want to convert to date.the second one is the input format.
--Example:- (simply it converts string to date format)

SELECT TO_DATE('20210126','YYYYMMDD');

--postgreSQL TO_CHAR FUNCTION : Convert Date or number to String
Syntax:-
to_char( value, format_mask )

SELECT TO_CHAR(now(),'DD Month YYYY');

SELECT TO_CHAR(now(),'Day Month YYYY');

SELECT TO_CHAR(now(),'Dy Mon YYYY');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH24:MI:SS');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS am');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS am tz');

---- Number examples for to_char
SELECT to_char(1210, '9999.99');

SELECT to_char(1210.7, '9G999.99');

SELECT to_char(121, '9 9 9');

SELECT to_char(121, '00999');


SELECT empno,ename,job,sal, TO_CHAR(now(),'DD-MON') date_month from emp; --day and month

SELECT empno,ename,job,sal, TO_CHAR(now(),'DAY') today_day from emp; --day

SELECT empno,ename,job,sal, TO_CHAR(now(),'MONTH') this_month from emp; --month

SELECT empno,ename,job,sal, TO_CHAR(now(),'YYYY') this_year from emp; --year

SELECT empno,ename,job,sal, TO_CHAR(now(),'HH24:MI:SS') today_time from emp; --day

--7.4 Character Functions
--LENGTH --It returns the length of the string
Syntax:-
LENGTH( string1 )
---
SELECT LENGTH(' ')
Result: 1

LENGTH('postgreSQL')
Result: 10

LENGTH('postgreSQL ')
Result: 11
--------

SELECT
empno employee_number,
LENGTH(ename) emp_name_length,
ename,
LENGTH(job) job_name_length,
job,
sal salary,
deptno department_number,
LENGTH('testing string') test_length
FROM
emp;
--UPPER -- It converts to uppercase
SELECT
empno employee_number,
UPPER(ename) employee_name,
UPPER(job) job,
sal salary,
deptno department_number,
UPPER('testing string') test_upper
FROM
emp;

--LOWER --It converts to lower case
Syntax:-
LOWER( string1 )
---
LOWER('Testing LowerCase');
Result: 'testing lowercase'

LOWER('GEORGE BURNS 123   ');
Result: george burns 123 
---

SELECT
empno employee_number,
LOWER(ename) employee_name,
LOWER(job) job,
sal salary,
deptno department_number,
LOWER('TESTING STRING') test_lower
FROM
emp;


--TRIM --TRIM function removes all specified characters either from the beginning or the end of a string.
Syntax:-
TRIM( [ [ LEADING | TRAILING | BOTH ] trim_character FROM ] string1 )

--Parameters or Arguments
LEADING
--The function will remove trim_character from the front of string1.
TRAILING
--The function will remove trim_character from the end of string1.
BOTH
--The function will remove trim_character from the front and end of string1.
trim_character
--The character that will be removed from string1. If this parameter is omitted, the TRIM function will remove space characters from string1.
---Examples:-
SELECT TRIM('   tech   ')
Result: 'tech'

TRIM(' '  FROM  '   tech   ')
Result: 'tech'

TRIM(LEADING '0' FROM '000123')
Result: '123'

TRIM(TRAILING '1' FROM 'Tech1')
Result: 'Tech'

TRIM(BOTH '1' FROM '123Tech111')
Result: '23Tech'
---
SELECT
empno employee_number,
TRIM(ename) employee_name,
TRIM(job) job,
sal salary,
deptno department_number,
TRIM('1245' FROM '245321testing string ') trim_testing
FROM
emp;
--LTRIM -- LTRIM function removes all specified characters from the left-hand side of a string.
Syntax:-
LTRIM( string1 [, trim_string] )
---
LTRIM('   tech')
Result: 'tech'

LTRIM('   tech', ' ')
Result: 'tech'

LTRIM('000123', '0')
Result: '123'

LTRIM('123123Tech', '123')
Result: 'Tech'

LTRIM('123123Tech123', '123')
Result: 'Tech123'

LTRIM('xyxzyyyTech', 'xyz')
Result: 'Tech'

LTRIM('6372Tech', '0123456789')
Result: 'Tech'
---
SELECT
empno employee_number,
LTRIM(ename) employee_name,
LTRIM(job) job,
sal salary,
deptno department_number,
LTRIM('89888999testing string','89') ltrim_testing
FROM
emp;
--RTRIM -- RTRIM function removes all specified characters from the right-hand side of a string
Syntax:-
RTRIM( string1 [, trim_string ] )
---Examples:-
RTRIM('tech   ')
Result: 'tech'

RTRIM('tech   ', ' ')
Result: 'tech'

RTRIM('123000', '0')
Result: '123'

RTRIM('Tech123123', '123')
Result: 'Tech'

RTRIM('123Tech123', '123')
Result: '123Tech'

RTRIM('Techxyxzyyy', 'xyz')
Result: 'Tech'

RTRIM('Tech6372', '0123456789')
Result: 'Tech'
---
SELECT
empno employee_number,
RTRIM(ename) employee_name,
RTRIM(job) job,
sal salary,
deptno department_number,
RTRIM('testing string23332 ','23') rtrim_testing
FROM
emp;
--LPAD -- LPAD function pads the left-side of a string with a specific set of characters 
--syntax:-
LPAD( string1, padded_length [, pad_string] )

----Examples:-
SELECT LPAD('tech', 7);
Result: '   tech'

LPAD('tech', 8, '0');
Result: '0000tech'

LPAD('testing string', 14, 'z');
Result: 'testing string'

LPAD('testing string', 16, 'z');
Result: 'zztesting string'
----

Example:- 1
SELECT
empno employee_number,
LPAD(ename,15) emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 2
SELECT
empno employee_number,
LPAD(ename,15,'Y') emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 3
SELECT
empno employee_number,
LPAD(ename,15,'YA') emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;
--RPAD --RPAD function pads the right-side of a string with a specific set of characters
Syntax:-
RPAD( string1, padded_length [, pad_string] )
---Example:-
RPAD('tech', 7)
Result: 'tech   '

RPAD('tech', 8, '0')
Result: 'tech0000'

RPAD('testing string', 14, 'z')
Result: 'testing string'

RPAD('testing string', 16, 'z')
Result: 'testing stringzz'
---
Example:- 1
SELECT
empno employee_number,
RPAD(ename,15) emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 2
SELECT
empno employee_number,
RPAD(ename,15,'Y') emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 3
SELECT
empno employee_number,
RPAD(ename,15,'YA') emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

SELECT LPAD(RPAD('testing string', 16, 'z'),20,'Y')

SELECT RTRIM(LTRIM('6372Tech98778888', '0123456789'),'0123456789')

SELECT RTRIM(LTRIM('         6372Tech98778888          '))