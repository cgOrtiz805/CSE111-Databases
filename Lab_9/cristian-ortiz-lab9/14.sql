SELECT s_region,
       c_region,
       SUM(l.l_extendedprice) 
  FROM Q1,
       lineitem l,
       orders o,
       Q2
 WHERE o.o_orderkey = l.l_orderkey AND 
       c_custkey = o.o_custkey AND 
       l.l_suppkey = s_suppkey
  
 GROUP BY s_region, c_region;
