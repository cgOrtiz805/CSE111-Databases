SELECT COUNT(DISTINCT o.o_orderkey)
FROM orders o, Q1,Q2, lineitem l
WHERE
s_region = (SELECT s_region FROM Q2 WHERE s_region = "EUROPE")

AND
c_nation = (SELECT c_nation FROM Q1 WHERE c_nation = "CANADA")
AND
c_custkey = o.o_custkey 
AND
l.l_suppkey = s_suppkey 
AND
o.o_orderkey = l.l_orderkey;
