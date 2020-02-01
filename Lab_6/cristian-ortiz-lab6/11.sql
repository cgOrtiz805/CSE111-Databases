SELECT n_name
FROM
   customer  INNER JOIN nation ON c_nationkey = n_nationkey
 
       GROUP BY n_name
       ORDER BY COUNT(c_custkey) DESC LIMIT 2;
 
    