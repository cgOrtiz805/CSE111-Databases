SELECT n_name
FROM
supplier INNER JOIN lineitem ON s_suppkey = l_suppkey
INNER JOIN orders ON l_orderkey = o_orderkey
  INNER JOIN nation ON s_nationkey = n_nationkey
 WHERE
 l_shipdate LIKE "1996%"
       GROUP BY n_name
       ORDER BY SUM(l_extendedprice) DESC LIMIT 1;
 
    