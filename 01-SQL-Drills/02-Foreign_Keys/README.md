# Foreign Keys


* The following are a query and output involving two tables. Notice that `department_id` and `id` columns match.

  ```sql
  SELECT * FROM employees e
  JOIN departments d
  ON (e.department_id = d.id)
  WHERE e.department_id = 45;
  ```
  
  ![Images/foreign01.png](Images/foreign01.png)
  
* Based on the above, reconstruct the table schema for `employees` and `departments` tables.

departments
-
id INTEGER PK
dept_name VARCHAR NOT NULL

employees
-
employee_id INTEGER PK
first_name VARCHAR NOT NULL
last_name VARCHAR NOT NOLL
department_id INTEGER FK >- employees.id

