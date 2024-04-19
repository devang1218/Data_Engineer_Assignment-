import sqlite3
import pandas as pd


class database:
    def __init__(self, path) -> None:
        con = sqlite3.connect(path)
        self.cur = con.cursor()

    def get_targeted_customers(self):
        result = self.cur.execute('''Select c.customer_id as Customer,c.age as Age , i.item_name as Item, sum(o.quantity) as Quantity from Customers c inner join Sales s 
                        on c.customer_id = s.customer_id 
                        inner join Orders o 
                        on o.sales_id = s.sales_id 
                        inner join Items i 
                        on i.item_id = o.item_id 
                        where c.age BETWEEN 18 AND 35
                        group by c.customer_id , i.item_id
                        Having sum(o.quantity) > 0 ;''')
        
        df = pd.DataFrame(result.fetchall(),columns = [desc[0] for desc in self.cur.description]) 
        return df
    
    def get_table(self, table_name):
        response = self.cur.execute(f'''Select * from {table_name};''')
        df = pd.DataFrame(response.fetchall(),columns = [desc[0] for desc in self.cur.description]) 
        return df