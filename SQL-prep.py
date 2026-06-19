# SQL Practice Questions

###  Question_id: 1757: Recyclable and low fats products
####  link ->   https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50


"""Question- Write a solution to find the ids of products that are both low fat and recyclable.
 Return the result table in any order."""

 # Solution:

"""  select product_id from Products
    where low_fats = "y" && recyclable = "y" 
"""



### 584. Find customer referee

#### link -> https://leetcode.com/problems/find-customer-referee/editorial/?envType=study-plan-v2&envId=top-sql-50


""" Find the names of the customer that are either:

 referred by any customer with id != 2.
 not referred by any customer."""

# solution :

"""   SELECT name
    FROM customer
    WHERE referee_id!=2 OR referee_id is null; 

"""

###  175. Add two tables

#### Link: https://leetcode.com/problems/combine-two-tables/


"""Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order."""

# solution:

"""    select p.firstName, p.lastName, a.City, a.state from Person p
    left join Address a 
    on p.personID = a.personID"""


### 183. Customers who never orders

#### link -> https://leetcode.com/problems/customers-who-never-order/?envType=problem-list-v2&envId=database

"""Write a solution to find all customers who never order anything.
Return the result table in any order.
"""
#### solution:

# code :


""" select c.name as Customers
    from Customers c
    left join Orders o
    on c.id = o.customerID
    where o.id is null"""


### 182. Duplicate email

#### link -> https://leetcode.com/problems/duplicate-emails/description/

# Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

#### solution

# code :
         
         
"""  select email as Email from person
    group by email
    having count(*)>1"""

### 196. delete duplicate emails

#### link -> https://leetcode.com/problems/delete-duplicate-emails/

"""Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
"""
#### solution:

# code:

""" DELETE p1
    FROM Person p1, Person p2
    WHERE p1.email = p2.email
    AND p1.id > p2.id;"""




### 595. Big countries
#### Link -> https://leetcode.com/problems/big-countries/submissions/2020358664/

"""
A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.
"""
# solution:

"""SELECT name, population, area
     FROM World
     WHERE area >= 3000000
      OR population >= 25000000;"""


# 1148. Articles views I
# Link: https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50

""" 
Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.
"""

# solution:

"""
select distinct author_id as id
     from views
     where author_id = viewer_id 
     order by author_id asc
"""

# 620. Not Boring Movies
# Link: https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.
"""

# solution:
"""
select * from cinema
     where description <>"boring"  and id%2=1
     order by rating desc;
"""

# 1251. Average Selling Price
# Link: https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.
 If a product does not have any sold units, its average selling price is assumed to be 0.

"""

# Solution:

"""
select p.product_id, round(ifnull(sum(units*price)/sum(units),0),2) average_price
     from prices p
     left join unitssold us
     on p.product_id = us.product_id
     and purchase_date between start_date and end_date
     group by p.product_id

"""

#1683. Invalid Tweets:
# Link: https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of 
characters used in the content of the tweet is strictly greater than 15.
"""

# Solution:
"""
select tweet_id from tweets
     where length(content)>15;
"""

# 1378. Replace Employee ID With the Unique Identifier
# Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to show the unique ID of each user, 
If a user does not have a unique ID replace just show null.
"""

# Solution:

"""
select eu.unique_id, e.name from Employees e
left join EmployeeUNI eu
on e.id = eu.id
"""

# 1068. Product Sales Analysis I
# Link -> https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to report the product_name, year, 
and price for each sale_id in the Sales table.
"""

# Solution:

"""
select p.product_name, s.year, s.price from sales s
join product p
on s.product_id=p.product_id;
"""

# 1581. Customer Who Visited But Did Not Make Any Transactions
# Link -> https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

'''
Write a solution to find the IDs of the users who visited without making
 any transactions and the number of times they made these types of visits.

'''

# Solution:

'''
select v.customer_id, count(*) as count_no_trans from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id  is null
group by v.customer_id 

'''

# 197. Rising Temperature
# Link-> https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50

'''
Write a solution to find all dates' id with higher temperatures
 compared to its previous dates (yesterday).
'''

# Sloution:

'''
select w1.id from weather w1, weather w2
where datediff(w1.recordDate, w2.recordDate)= 1
and w1.temperature > w2.temperature;

'''

# 1661. Average time of process per machine
# Link -> https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

'''
There is a factory website that has several machines each running the same
number of processes. Write a solution to find the average time each 
machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the
'start' timestamp. The average time is calculated by the total time 
to complete every process on the machine divided by the number of 
processes that were run.
'''
# Solution:

'''
select a.machine_id, round(avg(b.timestamp - a.timestamp),3) as processing_time
from Activity a
join Activity b
on a.machine_id = b. machine_id and a.process_id = b.process_id
where a.activity_type = 'start' and b.activity_type = 'end'
group by a.machine_id;
'''

# 577. Employee Bonus
# Link -> https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

- The employee has a bonus less than 1000.
- The employee did not get any bonus.
"""

# Solution:

'''
select e.name,b.bonus
 from employee e
left join bonus b
on e.empid=b.empid
where bonus<1000 or bonus is null
'''

# 1280. Students And Examinations
# Link -> https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50

'''
Write a solution to find the 
number of times each student attended each exam
'''

# solution:

"""
select s.student_id, s.student_name,sub.subject_name,count(e.subject_name) AS attended_exams
from students s
cross join subjects sub 
left join examinations e
on s.student_id=e.student_id and sub.subject_name=e.subject_name
group by s.student_id, s.student_name,sub.subject_name
order by s.student_id,sub.subject_name
"""

# 570. Managers With Atleast 5 Direct Reports
# Link -> https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50

"""
Write a solution to find managers with at least five direct reports.
"""

# Solution:

"""
select e1.name
from employee e1
join employee e2
on e1.id=e2.managerid
group by e1.id,e1. name
having count(e2.managerid)>=5 
"""

# 1075. Projeect Employees I
# Link -> https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50

'''
Write an SQL query that reports the average experience
 years of all the employees for each project, rounded to 2 digits.
'''

# Solution:

'''
select p.project_id, round(avg(e.experience_years),2) as average_years 
FROM Project p
JOIN Employee e
ON e.employee_id = p.employee_id
GROUP BY p.project_id;
'''

# 181. Employees Earning More than theri Managers
# Link -> https://leetcode.com/problems/employees-earning-more-than-their-managers/description/?envType=problem-list-v2&envId=db-db1-sql-i

'''
Write a solution to find the employees
 who earn more than their managers.
'''

# Solution:

'''
select e1.name as Employee from Employee e1
join Employee e2 on e1.managerId = e2.id
where e1.salary > e2.salary
'''

# Customer Placing the Largest number of Orders
# Link -> https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation

"""
Write a solution to find the customer_number for the customer 
who has placed the largest number of orders.
"""

# Solution:

'''
select customer_number from Orders
group by customer_number
order by count(*) desc limit 1;
'''

# Classes with atleast 5 Students
# Link -> https://leetcode.com/problems/classes-with-at-least-5-students/submissions/2031898683/?envType=problem-list-v2&envId=db-db2-filtering-aggregation

'''
Write a solution to find all the classes 
that have at least five students.
'''

# Solution :

'''
select class from Courses
group by class
having count(student)>= 5
'''

#Monthly Transactions I
# Link ->https://leetcode.com/problems/monthly-transactions-i/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation

'''
Write an SQL query to find for each month and country, the number of transactions and their total amount, 
the number of approved transactions and their total amount.
'''

# Solution :

'''
select DATE_FORMAT(trans_date,'%Y-%m') as month,country,
     count(*) as trans_count,
     sum(case when state = 'approved' then 1 else 0 END ) as approved_count,
     sum(amount) as trans_total_amount, 
     sum(case when state = 'approved' then amount else 0 end) as approved_total_amount 
     from Transactions
     group by DATE_FORMAT(trans_date,'%Y-%m'), country
'''

# User activity for the past 30 days
# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=problem-list-v2&envId=db-db2-filtering-aggregation

'''
Write a solution to find the daily active user count for a period of
30 days ending 2019-07-27 inclusively. A user was active on someday 
if they made at least one activity on that day.
'''

# Solution:

'''
select activity_date as day, count(distinct user_id) as active_users 
from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date;
'''

# Students and Examinations
# Link -> https://leetcode.com/problems/students-and-examinations/description/?envType=problem-list-v2&envId=db-db3-grouping-aggregation

'''
Write a solution to find the number of times each student 
attended each exam.
'''

# Solution:

'''
select s.student_id, s.student_name,sub.subject_name,count(e.subject_name) AS attended_exams
from students s
cross join subjects sub 
left join examinations e
on s.student_id=e.student_id and sub.subject_name=e.subject_name
group by s.student_id, s.student_name,sub.subject_name
order by s.student_id,sub.subject_name
'''

# Customers Who Bought ALl Products
# Link -> https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=problem-list-v2&envId=db-db3-grouping-aggregation
'''
Write a solution to report the customer ids from the Customer table 
that bought all the products in the Product table.

'''

# Solution:

'''
select c.customer_id as customer_id
from Customer c inner join Product p
on c.product_key = p.product_key
group by customer_id 
 count(distinct c.product_key) = (select count(*) from Product)
'''
# Tree Node
# Link -> https://leetcode.com/problems/tree-node/description/?envType=problem-list-v2&envId=db-db3-grouping-aggregation

'''
Write a solution to report the type of each node in the tree.

Return the result table in any order
'''
# Solution:

'''
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id
                    FROM Tree
                    WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
ORDER BY id;

'''

# Trips and Users
#Link ->

'''
Write a solution to find the cancellation rate of requests with unbanned 
users (both client and driver must not be banned) each day 
between "2013-10-01" and "2013-10-03" with at least one trip.
Round Cancellation Rate to two decimal points.
'''
# Solution:
 
'''
SELECT
    request_at AS Day,
    ROUND(
        AVG(CASE
                WHEN status != 'completed' THEN 1
                ELSE 0
            END),
        2
    ) AS 'Cancellation Rate'
FROM Trips t
JOIN Users c
    ON t.client_id = c.users_id
JOIN Users d
    ON t.driver_id = d.users_id
WHERE c.banned = 'No'
  AND d.banned = 'No'
  AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;
'''

# 178. Rank Scores
# Link -> https://leetcode.com/problems/rank-scores/description/?envType=problem-list-v2&envId=db-db4-window-functions-ranking

'''
Write a solution to find the rank of the scores. The ranking should be 
calculated according to the following rules:

- The scores should be ranked from the highest to the lowest.
- If there is a tie between two scores, both should have the same ranking.

After a tie, the next ranking number should be the next consecutive 
integer value. In other words, there should be no holes between ranks.
'''

# Solution:

'''
SELECT s1.score,(SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s1.score
    ) AS `rank`
FROM Scores s1
ORDER BY s1.score DESC;
'''

# Consecutive Numbers
# Link -> https://leetcode.com/problems/consecutive-numbers/?envType=problem-list-v2&envId=db-db4-window-functions-ranking

'''
Find all numbers that appear at least three times consecutively.

Return the result table in any order.
'''

# Solution:

'''
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1
  AND num = prev2;
'''

# Investments in 2016
# Link ->https://leetcode.com/problems/investments-in-2016/description/?envType=problem-list-v2&envId=db-db5-sql-ii

'''
Write a solution to report the sum of all total investment values in 
2016 tiv_2016, for all policyholders who:

- have the same tiv_2015 value as one or more other policyholders, and
- are not located in the same city as any other policyholder 
(i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.
'''
# Solution:

'''SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1
      )
  AND (lat, lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
      );
'''

# 184 Department Highiest Salary
# Link -> https://leetcode.com/problems/department-highest-salary/?envType=problem-list-v2&envId=db-db5-sql-ii

'''
Write a solution to find employees
who have the highest salary in each of the departments.
'''

# Solution :

'''
select d.name as Department, e.name as Employee, e.salary as Salary from Employee e
join Department d
on e.departmentID = d.id
where (e.departmentID, e.salary) in (select departmentID, max(salary) from Employee
group by departmentID);  
'''

# 1070. Product Sales Analysis III
# Link -> http://leetcode.com/problems/product-sales-analysis-iii/?envType=problem-list-v2&envId=db-db5-sql-ii

'''
Write a solution to find all sales that occurred in the first year each 
product was sold.

- For each product_id, identify the earliest year it appears in the Sales
table.

- Return all sales entries for that product in that year.
'''
# Solution :

'''
select product_id, year as First_year, quantity, price
from Sales
where (product_id, year) in (select product_id, min(year)from Sales 
group by product_id)
'''

# 601. Human Traffic To Stadium
# Link -> https://leetcode.com/problems/human-traffic-of-stadium/description/?envType=problem-list-v2&envId=db-db5-sql-ii

'''
Write a solution to display the records with three or more rows 
consecutive id's, and the number of people is greater than or equal 
to 100 for eac
'''

# Solution :

'''
with cte as (select * , id - ROW_NUMBER() OVER (ORDER BY id) as grp
from Stadium
where people >= 100)
select id,visit_date, people from cte
where grp in (
    select grp from cte
    group by grp
    having count(*) >= 3
)order by visit_date;
'''

# 586. Customer Placing the largest numbers of orders.
# Link -> https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

''' 
Write a solution to find the customer_number for the customer who
has placed the largest number of orders.

The test cases are generated so that exactly one customer will
have placed more orders than any other customer.
'''

# Solution :
'''
select customer_number from Orders
group by customer_number
order by count(*) desc limit 1;
'''

# 607. Sales Person 
# Link -> https://leetcode.com/problems/sales-person/description/

'''
Write a solution to find the names of all the salespersons who 
did not have any orders related to the company with the 
name "RED".
'''

# Solution :

'''
select name from SalesPerson
where sales_id not in (
    select o.sales_id from Orders o
    join Company c
    On o.com_id = c.com_id
    where c.name = 'red'
)
'''
# 1179. Reformat Departmet Table
# Link -> https://leetcode.com/problems/reformat-department-table/description/

'''
Reformat the table such that there is a department id column 
and a revenue column for each month.
'''

# Solution :

'''
select id, max(case when month = 'Jan' then revenue end) as JAN_Revenue,
max(case when month = 'Feb' then revenue end) as Feb_Revenue,
max(case when month = 'Mar' then revenue end) as Mar_Revenue,
max(case when month = 'Apr' then revenue end) as Apr_Revenue,
max(case when month = 'May' then revenue end) as May_Revenue,
max(case when month = 'Jun' then revenue end) as Jun_Revenue,
max(case when month = 'Jul' then revenue end) as Jul_Revenue,
max(case when month = 'Aug' then revenue end) as Aug_Revenue,
max(case when month = 'Sep' then revenue end) as Sep_Revenue,
max(case when month = 'Oct' then revenue end) as Oct_Revenue,
max(case when month = 'Nov' then revenue end) as Nov_Revenue,
max(case when month = 'Dec' then revenue end) as Dec_Revenue from Department

group by id;



'''