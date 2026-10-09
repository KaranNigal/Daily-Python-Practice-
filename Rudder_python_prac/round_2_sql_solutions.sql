-- SQL answers for section 10 of the Rudder Analytics Round 2 question bank.
-- Queries use PostgreSQL syntax where dialect-specific syntax is necessary.

-- 1. Display all employees.
SELECT *
FROM employees;

-- 2. Names and salaries of employees earning more than 50000.
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- 3. Employee name and department name.
SELECT e.name AS employee_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON d.id = e.dept_id;

-- 4. All employees, including those without a matching department.
SELECT e.name AS employee_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON d.id = e.dept_id;

-- 5. Employee count per department, including departments with no employees.
SELECT d.id, d.dept_name, COUNT(e.id) AS employee_count
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.id
GROUP BY d.id, d.dept_name
ORDER BY d.id;

-- 6. Departments with more than 3 employees.
SELECT d.id, d.dept_name, COUNT(e.id) AS employee_count
FROM departments AS d
INNER JOIN employees AS e ON e.dept_id = d.id
GROUP BY d.id, d.dept_name
HAVING COUNT(e.id) > 3;

-- 7. Highest and second-highest distinct salaries.
SELECT
    MAX(salary) AS highest_salary,
    MAX(salary) FILTER (WHERE salary < (SELECT MAX(salary) FROM employees))
        AS second_highest_salary
FROM employees;

-- 8. Top 3 highest-paid employees (ties at the cutoff may be excluded).
SELECT id, name, salary
FROM employees
ORDER BY salary DESC
FETCH FIRST 3 ROWS ONLY;

-- 9. Duplicate employee names.
SELECT name, COUNT(*) AS occurrences
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

-- 10. Employees earning more than the average salary.
SELECT id, name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 11. Department with the highest average salary.
SELECT d.id, d.dept_name, AVG(e.salary) AS average_salary
FROM departments AS d
JOIN employees AS e ON e.dept_id = d.id
GROUP BY d.id, d.dept_name
ORDER BY average_salary DESC
FETCH FIRST 1 ROW ONLY;

-- 12. Employees and their managers (employees without a manager are retained).
SELECT e.name AS employee_name, m.name AS manager_name
FROM employees AS e
LEFT JOIN employees AS m ON m.id = e.manager_id;

-- 13. Customers who have placed no orders.
SELECT c.customer_id, c.name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
);

-- 14. Total order amount per customer, highest total first.
SELECT c.customer_id, c.name, COALESCE(SUM(o.amount), 0) AS total_amount
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_amount DESC;

-- 15. Customers from a supplied city whose total orders exceed 10000.
-- Bind :city to the city being queried.
SELECT c.customer_id, c.name, SUM(o.amount) AS total_amount
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
WHERE c.city = :city
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 10000;

-- 16. Employees who joined in the last 6 months.
SELECT id, name, join_date
FROM employees
WHERE join_date >= CURRENT_DATE - INTERVAL '6 months'
  AND join_date <= CURRENT_DATE;

-- 17. Delete duplicate employee records while keeping the lowest id for each
-- business-record combination. PostgreSQL ctid identifies physical row versions.
-- id is omitted from the duplicate key because it is normally unique.
WITH ranked AS (
    SELECT ctid,
           ROW_NUMBER() OVER (
               PARTITION BY name, dept_id, salary, manager_id, join_date
               ORDER BY id, ctid
           ) AS row_number
    FROM employees
)
DELETE FROM employees AS e
USING ranked AS r
WHERE e.ctid = r.ctid
  AND r.row_number > 1;

-- 18. Nth-highest distinct salary. Bind :n to a positive integer.
WITH ranked_salaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
    WHERE salary IS NOT NULL
)
SELECT MAX(salary) AS nth_highest_salary
FROM ranked_salaries
WHERE salary_rank = :n;

-- 19. Number of orders per calendar month.
SELECT DATE_TRUNC('month', order_date)::date AS month,
       COUNT(*) AS order_count
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- 20. WHERE filters rows before grouping; HAVING filters groups after
-- aggregation. INNER JOIN keeps matched rows only. LEFT JOIN keeps every left
-- row and fills unmatched right-side columns with NULL. RIGHT JOIN is the
-- mirror image of LEFT JOIN. FULL JOIN keeps matched rows and all unmatched
-- rows from both sides, filling missing-side columns with NULL.
