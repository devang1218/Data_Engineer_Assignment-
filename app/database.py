import sqlite3
import pandas as pd

con = sqlite3.connect("XYZ")
cur = con.cursor()

# res = cur.execute('''CREATE TABLE Customer (
#                         customer_id int AUTO_INCREMENT,
#                         age int,
#                         PRIMARY KEY (customer_id)
#                     );''')

# res = cur.execute('''CREATE TABLE Items (
#                         item_id int AUTO_INCREMENT,
#                         item_name varchar(255),
#                         PRIMARY KEY (item_id)
#                     );''')

# res = cur.execute('''CREATE TABLE Sales (
#                         sales_id int AUTO_INCREMENT,
#                         customer_id int not null,
#                         PRIMARY KEY (sales_id),
#                         FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
#                     );''')

# res = cur.execute('''CREATE TABLE Orders (
#                         order_id int AUTO_INCREMENT,
#                         sales_id int not null,
#                         item_id int not null,
#                         quantity int,
#                         PRIMARY KEY (order_id),
#                         FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
#                         FOREIGN KEY (item_id) REFERENCES Items(item_id)
#                     );''')

# con.execute('''insert into Items values (1, 'x'),
#                                          (2, 'y'),
#                                          (3, 'z');''')

# con.execute('''insert into Customer values (1, 21),
#                                             (2, 23),
#                                             (3, 35),
#                                             (4,40);''')

# con.execute('''insert into Sales values (101, 1),
#                                          (102, 1),
#                                          (103, 1),
#                                          (104, 1),
#                                          (105, 2),
#                                          (106, 3),
#                                          (107, 3);''')

# con.execute('''insert into Orders values (1001, 101,1,3),
#                                           (1002, 102,1,2),
#                                           (1003, 103,1,1),
#                                           (1004, 104,1,4),
#                                           (1005, 105,1,1),
#                                           (1006, 105,2,1),
#                                           (1007, 105,3,1),
#                                           (1008, 106,3,1),
#                                           (1009, 107,3,1);''')

# con.commit()

class database:
    def __init__(self) -> None:
        pass

    def get_targeted_customers(self):
        result = cur.execute('''Select c.customer_id as Customer,c.age as Age , i.item_name as Item, sum(o.quantity) as Quantity from Customer c inner join Sales s 
                        on c.customer_id = s.customer_id 
                        inner join Orders o 
                        on o.sales_id = s.sales_id 
                        inner join Items i 
                        on i.item_id = o.item_id 
                        where c.age BETWEEN 18 AND 35
                        group by c.customer_id , i.item_id
                        Having sum(o.quantity) > 0 ;''')
        
        df = pd.DataFrame(result.fetchall(),columns = [desc[0] for desc in cur.description]) 
        return df
    
    def get_table(self, table_name):
        response = cur.execute(f'''Select * from {table_name};''')
        df = pd.DataFrame(response.fetchall(),columns = [desc[0] for desc in cur.description]) 
        return df