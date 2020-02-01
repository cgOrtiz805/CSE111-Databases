SELECT COUNT(DISTINCT s_suppkey)
   FROM supplier 
   INNER JOIN partsupp ON s_suppkey = ps_suppkey
    INNER JOIN part ON ps_partkey = p_partkey
    WHERE
    
    p_retailprice = (SELECT MIN(p.p_retailprice) FROM part p);