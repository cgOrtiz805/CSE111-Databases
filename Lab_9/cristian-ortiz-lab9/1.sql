SELECT c_name, SUM(o.o_totalprice), c_nation
FROM orders o, Q1
WHERE 
c_custkey = o.o_custkey
AND
c_nation = "FRANCE"
GROUP BY c_name;
