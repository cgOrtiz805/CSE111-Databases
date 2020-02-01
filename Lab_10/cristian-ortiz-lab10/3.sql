
CREATE TRIGGER PriorityD
         AFTER DELETE
            ON lineitem
      FOR EACH ROW
BEGIN
    UPDATE orders
       SET o_orderpriority = 'HIGH'
     WHERE o_orderkey = OLD.l_orderkey;
END;

CREATE TRIGGER PriorityI
         AFTER INSERT
            ON lineitem
      FOR EACH ROW
BEGIN
    UPDATE orders
       SET o_orderpriority = 'HIGH'
     WHERE o_orderkey = OLD.l_orderkey;
END;

DELETE FROM lineitem
      WHERE l_orderkey IN (
    SELECT l_orderkey
      FROM lineitem
           INNER JOIN
           orders ON l_orderkey = o_orderkey
     WHERE o_orderdate LIKE '1995-08%'
);


SELECT COUNT(o_orderkey)
FROM  orders
WHERE o_orderpriority LIKE '%HIGH%'
AND o_orderdate LIKE '1995-08%';