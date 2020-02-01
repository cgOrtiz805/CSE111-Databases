SELECT l_quantity AS quantity, l_extendedprice AS extendedprice
FROM lineitem
WHERE l_returnflag = "N"
AND
l_shipdate = "1995-09-25";