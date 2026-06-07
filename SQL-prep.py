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

# 1250. Average Selling Price
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