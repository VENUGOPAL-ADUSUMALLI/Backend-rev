CREATE TABLE User(
    id INTEGER Not NULL PRIMARY KEY,
    name VARCHAR(30),
    email TEXT unique,
    phone_number varchar(12)
);

CREATE TABLE PRODUCT(
   id INTEGER NOt NULL PRIMARY KEY,
   name varchar(50),
   price INTEGER
);

CREATE TABLE ORDERS(
   id INTEGER NOt NULL PRIMARY KEY,
   user_id INTEGER,
   price INTEGER,
   ordered_date DATE,
   no_of_items INTEGER,
   FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE ORDERITEMS(
   id INTEGER NOT NULL PRIMARY KEY,
   order_id INTEGER,
   product_id INTEGER,
   quantity INTEGER,
   PRICE INTEGER,
   total_price INTEGER,
   FOREIGN KEY (order_id) REFERENCES ORDERS(id),
   FOREIGN KEY (product_id) REFERENCES PRODUCT(id)
);

INSERT INTO
  USER (id, name, email, phone_number)
VALUES
  (1, 'VENU', 'abc@gmail.com', '9666910497'),
  (2, 'Rahul', 'ac@gmail.com', '9441844128');

INSERT INTO PRODUCT (id, name, price)
VALUES
    (101, 'Laptop', 50000),
    (102, 'Mouse', 1000),
    (103, 'Keyboard', 2500),
    (104, 'Monitor', 15000);

INSERT INTO ORDERS (id, user_id, price, ordered_date, no_of_items)
VALUES
    (1, 1, 52000, '2026-08-27', 2),
    (2, 2, 15000, '2026-08-27', 1),
    (3, 1, 3500, '2026-08-28', 2),
    (4, 3, 65000, '2026-08-28', 3);


INSERT INTO ORDERITEMS
    (id, order_id, product_id, quantity, price, total_price)
VALUES
    (1, 1, 101, 1, 50000, 50000),
    (2, 1, 102, 2, 1000, 2000),
    (3, 2, 104, 1, 15000, 15000),
    (4, 3, 102, 1, 1000, 1000),
    (5, 3, 103, 1, 2500, 2500),
    (6, 4, 101, 1, 50000, 50000),
    (7, 4, 103, 2, 2500, 5000),
    (8, 4, 102, 10, 1000, 10000);

select name, email from user where id = "1";
select * from product where name LIKE "%o%";
select * from product where id in (1, 2, 3);
select * from product where price BETWEEN 1000 and 2000;
select * from product ORDER BY PRICE DESC;
select name from PRODUCT ORDER BY PRICE asc LIMIT 2;
select name from PRODUCT ORDER BY price DESC LIMIT 2 OFFSET 3;
select count(*) from User;
select sum(price) from ORDERS;
select user_id,  sum(price) from ORDERS group by user_id;
select user_id, sum(price) as price from ORDERS GROUP BY user_id having price > 5000;

select user_id,count(*) from ORDERS group by user_id;
select user_id, sum(price) as total_spent from ORDERS GROUP by user_id;
select user_id,sum(price) as total_spent from ORDERS group by user_id having total_spent >50000;
select max(quantity) from ORDERITEMS;
select sum(quantity) from ORDERITEMS;
select user.id, orders.id from user inner join orders on user.id = orders.user_id;
