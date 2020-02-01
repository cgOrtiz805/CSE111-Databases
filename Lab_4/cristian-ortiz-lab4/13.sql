SELECT COUNT(DISTINCT o.o_orderkey)
FROM orders o, supplier s, nation n, region r, customer c, lineitem l
WHERE
s.s_nationkey = (SELECT n_nationkey FROM nation, region WHERE n_nationkey = s.s_nationkey AND n_regionkey = r_regionkey AND r_name = "EUROPE")
AND
r.r_regionkey = n.n_regionkey
AND
c.c_nationkey = (SELECT n_nationkey FROM nation WHERE n_nationkey = c.c_nationkey AND n_name = "CANADA")
AND
c.c_custkey = o.o_custkey 
AND
l.l_suppkey = s.s_suppkey 
AND
o.o_orderkey = l.l_orderkey;
