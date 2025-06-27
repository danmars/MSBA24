-- Challenge 1 - subqueries- use zagi
-- Find all the transaction totals smaller than the larger transaction totals for vendor Mountain king
-- Return vendorname, transaction id and the transaction total
-- Hint: the transaction total = quantity*productprice for each transaction. Use ANY function.

-- Challenge 2 - funcions- use my_guitar_shop
-- Write a SELECT statement that uses regular expression functions to get the 
-- username and domain name parts of the email addresses in the Administrators table. 
-- Return these columns:
-- The email_address column
-- A column named user_name that contains the username part of the 
-- email_address column (the part before the @ symbol)
-- A column named domain_name that contains the domain name part
-- of the email_address column (the part after the @ symbol)
-- Note: The username part of the email addresses contains only letters, and the 
-- domain name part contains only letters and a period.

-- Challenge 3 - functions- use my_guitar_shop
-- Write a SELECT statement that uses the ranking functions to rank products by the 
-- total quantity sold. Return these columns:
-- The product_name column from the Products table
-- A column named total_quantity that shows the sum of the quantity for 
-- each product in the Order_Items table
-- A column named rank that uses the RANK function to rank the total 
-- quantity in descending sequence
-- A column named dense_rank that uses the DENSE_RANK function to 
-- rank the total quantity in descending sequence

-- Challenge 4 - functions- use my_guitar_shop
-- Write a SELECT statement that uses the analytic functions to get the highest and 
-- lowest sales by product within each category. Return these columns:
-- The category_name column from the Categories table
-- The product_name column from the Products table
-- A column named total_sales that shows the sum of the sales for each 
-- product with sales in the Order_Items table
-- A column named highest_sales that uses the FIRST_VALUE function to 
-- show the name of the product with the highest sales within each category 
-- A column named lowest_sales that uses the LAST_VALUE function to 
-- show the name of the product with the lowest sales within each category

 