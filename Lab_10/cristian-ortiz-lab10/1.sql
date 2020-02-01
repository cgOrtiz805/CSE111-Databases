

CREATE TRIGGER T_order
         AFTER INSERT
            ON orders
      FOR EACH ROW
BEGIN
    UPDATE orders
       SET o_orderdate = DATETIME('NOW') 
     WHERE o_orderkey = NEW.o_orderkey;
END;

INSERT INTO orders SELECT *
                     FROM orders
                    WHERE o_orderdate LIKE '1996-08%';

SELECT *
  FROM orders
 WHERE o_orderdate LIKE "2019-11%";
