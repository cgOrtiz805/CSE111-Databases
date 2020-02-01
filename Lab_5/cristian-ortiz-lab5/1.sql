SELECT COUNT(DISTINCT c.c_custkey)
FROM nation n, customer c, region r
WHERE 
c.c_nationkey = n.n_nationkey
AND
n.n_regionkey = r.r_regionkey
AND r.r_name <> "AFRICA"
AND r.r_name <> "EUROPE";
