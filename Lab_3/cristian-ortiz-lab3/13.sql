SELECT ROUND(AVG(c.c_acctbal),11)
FROM customer c, nation n, region r
WHERE c.c_nationkey = n.n_nationkey
AND
r.r_regionkey = n.n_regionkey
AND
r.r_name = "EUROPE"
AND c.c_mktsegment = "MACHINERY";