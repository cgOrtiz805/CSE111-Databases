SELECT n.n_name, COUNT(s.s_suppkey)
FROM supplier s, nation n
WHERE 
s.s_nationkey = n.n_nationkey
GROUP BY n.n_nationkey
ORDER BY n.n_name ASC;