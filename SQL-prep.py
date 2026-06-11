# SQL

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