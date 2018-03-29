# Challenge Set 9: Solutions
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

```sql
SELECT
    CustomerName
FROM
    Customers
WHERE
    Country = 'UK';
```

>Around the Horn  
B's Beverages  
Consolidated Holdings  
Eastern Connection  
Island Trading  
North/South  
Seven Seas Imports  

2. What is the name of the customer who has the most orders?

```sql
SELECT
    CustomerName,
    COUNT(*) as OrderCount
FROM
    Customers AS c
  JOIN
    Orders AS o
  ON
    c.CustomerID = o.CustomerID
GROUP BY
    o.CustomerID
ORDER BY
    OrderCount DESC
LIMIT 1;
```

> **Ernst Handel** with 10 orders

3. Which supplier has the highest average product price?

```sql
SELECT
    SupplierName,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON 
    s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID
ORDER BY
    MeanPrice DESC
LIMIT 1;
```

> **Aux joyeux ecclésiastiques** with average price of 140.75

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

```sql
SELECT
    COUNT(DISTINCT(Country)) AS NumCountries 
FROM
    Customers;
```

> **21** different countries

5. What category appears in the most orders?


```sql
SELECT
    c.CategoryName, 
    COUNT(*) AS Count
FROM
    OrderDetails as o
  JOIN
    Products as p
  JOIN
    Categories AS c
  ON
      o.ProductID = p.ProductID
    AND
      p.CategoryID = c.CategoryID
GROUP BY
    c.CategoryName
ORDER BY
    Count DESC
LIMIT 1;
```

> **Dairy Products** on 100 orders

6. What was the total cost for each order?

```sql
SELECT
    o.OrderID,
    SUM(o.Quantity * p.Price) as Total
FROM
    OrderDetails as o
  JOIN
    Products as p
  ON
    o.ProductID = p.ProductID
GROUP BY
    o.OrderID
ORDER BY
    Total DESC;
```

>Here are first 5:  
ID   Total  
10372 15353.6
10424 14366.5
10417 14104
10353 13427
10360 9244.25

7. Which employee made the most sales (by total price)?

```sql
SELECT
    e.FirstName,
    e.LastName,
    SUM(op.Quantity * p.Price) as Total
FROM
    Employees as e
  JOIN
    Orders as o
  JOIN
    OrderDetails as op
  JOIN
    Products as p
  ON
      e.EmployeeID = o.EmployeeID
    AND
      o.OrderID = op.OrderID
    AND
      op.ProductID = p.ProductID
GROUP BY
    e.EmployeeID
ORDER BY
    Total DESC;
```

>Margaret Peacock

8. What employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

```sql
SELECT
    *
FROM 
    Employees 
WHERE 
    Notes 
LIKE 
    '%BS%';
```

>Janet Leverling  
Steven Buchanan

9. What supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

```sql
SELECT
    SupplierName,
    COUNT(*) as NumProducts,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON
    s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID
HAVING
    NumProducts >= 3
ORDER BY
    MeanPrice DESC;
```

>Tokyo Traders