
## **exercise-01**  
**Tytuł**:  
Write a SQL query to select the sex and body mass columns from the little_penguins in that order, sorted such that the largest body mass appears first.

**SQL**:  
SELECT sex, body_mass_g FROM little_penguins ORDER BY body_mass_g DESC"


**Link**: [Przechwytywanie1](https://github.com/endis1306/Isi/blob/main/sql-exercises/screenshots/Przechwytywanie1.PNG)

---

## **exercise-02**  
**Tytuł**:  
Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.

**SQL**:  
select * from penguins limit 11 offset 49

**Link**: [Przechwytywanie2](https://github.com/endis1306/Isi/blob/main/sql-exercises/screenshots/Przechwytywanie2.PNG)

---

## **exercise-03**  
**Tytuł**:  
Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.

**SQL**:  
SELECT DISTINCT island, species FROM ( SELECT island, species FROM penguins LIMIT 11 OFFSET 49 ) AS subquery

**Link**: [Przechwytywanie3](https://github.com/endis1306/Isi/blob/main/sql-exercises/screenshots/Przechwytywanie3.PNG)

---

## **exercise-04**  
**Tytuł**:  
Write a query to select the body masses from penguins that are less than 3000.0 grams.

**SQL**:  
select body_mass_g from penguins where body_mass_g < 3000

**Link**: [Przechwytywanie4](https://github.com/endis1306/Isi/blob/main/screenshots/Przechwytywanie4.PNG)

---

## **exercise-05**  
**Tytuł**:  
Write another query to select the species and sex of penguins that weight less than 3000.0 grams. This shows that the columns displayed and those used in filtering are independent of each other.

**SQL**:  
select species ,sex from penguins  where body_mass_g < 3000

**Link**: [Przechwytywanie5](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie5.PNG)

---

## **exercise-06**  
**Tytuł**:  
Use the not operator to select penguins that are not Gentoos.

**SQL**:  
select * from penguins where species is not 'Gentoo'

**Link**: [Przechwytywanie6](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie6.PNG)

---

## **exercise-07**  
**Tytuł**:  
SQL's or is an inclusive or: it succeeds if either or both conditions are true. SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on Torgersen Island but not both.

**SQL**:  
select * from penguins where (sex = 'FEMALE' and island != 'Torgersen') or (sex = 'MALE' and island = 'Torgersen')

**Link**: [Przechwytywanie7](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie7.PNG)

---

## **exercise-08**  
**Tytuł**:  
A column called what_where that has the species and island of each penguin separated by a single space.

**SQL**:  
SELECT species || ' ' || island AS combined_info FROM penguins;

**Link**: [Przechwytywanie8](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie8.PNG)

---

## **exercise-09**  
**Tytuł**:  
A column called bill_ratio that has the ratio of bill length to bill depth.

**SQL**:  
SELECT *, bill_length_mm / bill_depth_mm AS bill_ratio FROM penguins

**Link**: [Przechwytywanie9](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie9.PNG)

---

## **exercise-10**  
**Tytuł**:  
Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?

**SQL**:  
.nullvalue
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 5;

**Link**: [Przechwytywanie10](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie10.PNG)

---

## **exercise-11**  
**Tytuł**:  
Write a query to find penguins whose body mass is known but whose sex is not.

**SQL**:  
SELECT * FROM penguins WHERE body_mass_g IS NOT NULL AND sex IS NULL

**Link**: [Przechwytywanie11](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie11.PNG)

---

## **exercise-12**  
**Tytuł**:  
Write another query to find penguins whose sex is known but whose body mass is not.

**SQL**:  
SELECT *
FROM penguins
WHERE body_mass_g IS NULL
AND sex IS NOT NULL


**Link**: [Przechwytywanie12](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie12.PNG)

---

## **exercise-13**  
**Tytuł**:  
What is the average body mass of penguins that weight more than 3000.0 grams?

**SQL**:  
SELECT AVG(body_mass_g) AS average_body_mass
FROM penguins
WHERE body_mass_g > 3000.0

**Link**: [Przechwytywanie13](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie13.PNG)

---

## **exercise-14**  
**Tytuł**:  
How many different body masses are in the penguins dataset?

**SQL**:  
SELECT COUNT(DISTINCT body_mass_g) AS unique_body_masses
FROM penguins

**Link**: [Przechwytywanie14](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie14.PNG)

---

## **exercise-15**  
**Tytuł**:  
Explain why the output of the previous query has a blank line before the rows for female and male penguins.
Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much.

**SQL**:  
SELECT body_mass_g, COUNT(*) AS num_penguins
FROM penguins
GROUP BY body_mass_g
ORDER BY body_mass_g;

**Link**: [Przechwytywanie15](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie15.PNG)

---

## **exercise-16**  
**Tytuł**:  
Write a query that uses filter to calculate the average body masses of heavy penguins (those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. Is it possible to do this using where instead of filter?

**SQL**:  
SELECT 
AVG(body_mass_g) FILTER(WHERE body_mass_g > 4500) AS average_heavy_penguins,
AVG(body_mass_g) FILTER(WHERE body_mass_g < 3500) AS average_light_penguins
FROM penguins

**Link**: [Przechwytywanie16](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie16.PNG)

---

## **exercise-17**  
**Tytuł**:  
Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. Use a query to check that the notes have been stored and that you can (for example) select by author name.
What happens if you try to insert too many or too few values into notes? What happens if you insert a number instead of a string into the note field?

**SQL**:  
Create table Notess (autor text, note text)
insert into Notess (autor, note) VALUES ('Kuba', 'cos')
insert into Notess (autor, note) VALUES ('Pawel', 'cosasdsd')
insert into Notess (autor, note) VALUES ('Alex', 'codsfsfds')
insert into Notess (autor, note) VALUES ('Jacek', 'Album9')
select * from Notess

**Link**: [Przechwytywanie17](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie17.PNG)

---

## **exercise-18**  
**Tytuł**:  
1. Re-create the notes table in an in-memory database and then use SQLite's .output and .dump commands to save the database to a file called notes.sql. Inspect the contents of this file: how has your data been stored?

2. Start a fresh SQLite session and load notes.sql using the .read command. Inspect the database using .schema and select *: is everything as you expected?

**Python Script Link**: https://github.com/endis1306/Isi/blob/main/sql-exercises/exercise-18.py


**Link**: [Przechwytywanie18](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie18.PNG)

---

## **exercise-19**  
**Tytuł**:  
1. Re-create the notes table in an in-memory database once again and use SQLite's .backup command to save it to a file called notes.db. Inspect this file using od -c notes.db or a text editor that can handle binary data: how has your data been stored?

2. Start a fresh SQLite session and load notes.db using the .restore command. Inspect the database using .schema and select *: is everything as you expected?

**Python Script Link**: https://github.com/endis1306/Isi/blob/main/sql-exercises/exercise-19.py


**Link**: [Przechwytywanie19](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie19.PNG)

---

## **exercise-20**  
**Tytuł**:  
Re-run the query shown above using where job = name instead of the full table.name notation. Is the shortened form easier or harder to read and more or less likely to cause errors?

**SQL**:  
elect *
from work inner join job
on job = nam

**Link**: [Przechwytywanie1](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie1.PNG)

---

## **exercise-21**  
**Tytuł**:  
Find the least time each person spent on any job. Your output should show that mik and po each spent 0.5 hours on some job. Can you find a way to show the name of the job as well using the SQL you have seen so far?

**SQL**:  
SELECT w.person, j.name AS job_name, MIN(j.billable) AS min_time
FROM work w
INNER JOIN job j ON w.job = j.name
GROUP BY w.person

**Link**: [Przechwytywanie19](https://github.com/endis1306/Isi/blob/main/programming-exercises/screenshots/Przechwytywanie19.PNG)

---
