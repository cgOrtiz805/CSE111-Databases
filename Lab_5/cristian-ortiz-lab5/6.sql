SELECT DISTINCT(p.p_mfgr)
FROM partsupp ps 
INNER JOIN supplier s ON s.s_suppkey = ps.ps_suppkey 
INNER JOIN part p ON p.p_partkey = ps.ps_partkey
WHERE s.s_name = "Supplier#000000053"
AND
ps.ps_availqty = (SELECT MIN(ps_availqty)
 FROM supplier
  INNER JOIN partsupp ON s_suppkey = ps_suppkey
  WHERE s_name = "Supplier#000000053");
