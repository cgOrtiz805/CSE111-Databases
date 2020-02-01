SELECT supplier_nation, s_price - c_price
FROM
    (SELECT SUM(l_extendedprice) AS s_price, n_name AS supplier_nation
        FROM supplier
            INNER JOIN lineitem ON l_suppkey = s_suppkey
            INNER JOIN orders ON o_orderkey = l_orderkey
            INNER JOIN nation ON n_nationkey = s_nationkey
            WHERE
            l_shipdate LIKE "1996%"
            GROUP BY n_name),
            
    (SELECT SUM(l_extendedprice) AS c_price, n_name AS customer_nation
    FROM customer
    INNER JOIN orders ON o_custkey = c_custkey
    INNER JOIN lineitem ON l_orderkey = o_orderkey
    INNER JOIN nation ON n_nationkey = c_nationkey
            WHERE
            l_shipdate LIKE "1996%"
            GROUP BY n_name)
          
 WHERE supplier_nation = customer_nation;
