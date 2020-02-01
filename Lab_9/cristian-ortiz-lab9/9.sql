SELECT COUNT(DISTINCT o_clerk) 
  FROM Q2,
       Q5,
       lineitem l
 WHERE s_suppkey = l.l_suppkey AND 
       l.l_orderkey = o_orderkey AND 
      s_nation = "RUSSIA";
