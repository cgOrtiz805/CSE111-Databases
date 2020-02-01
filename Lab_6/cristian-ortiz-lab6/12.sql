SELECT n_name
FROM
   customer INNER JOIN orders ON c_custkey = o_custkey
  INNER JOIN nation ON c_nationkey = n_nationkey
 
       GROUP BY n_name
       ORDER BY COUNT(o_totalprice) DESC LIMIT 1;
 
    