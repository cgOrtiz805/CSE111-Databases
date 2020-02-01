SELECT c.c_name, SUM(o.o_totalprice), n.n_name
FROM orders o, customer c, nation n
WHERE n.n_nationkey = c.c_nationkey
AND
c.c_custkey = o.o_custkey
AND
n.n_name = "FRANCE"
GROUP BY c.c_name;
