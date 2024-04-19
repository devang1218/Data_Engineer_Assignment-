from database import database
import pandas as pd
import sqlite3

# first method using sql query 
# I have used separate file(dataabse.py) to connect to db and get the result from it into the python code
db = database()

cnx = sqlite3.connect('XYZ')

result_sql = db.get_targeted_customers()
result_sql.to_csv(path_or_buf='../output/sql_query_output.csv',sep=';', index=False)


# Second method using Pandas
df_item = pd.read_sql_query("SELECT * FROM Items", cnx)
df_customer = pd.read_sql_query("SELECT * FROM Customer", cnx)
df_orders = pd.read_sql_query("SELECT * FROM Orders", cnx)
df_sales = pd.read_sql_query("SELECT * FROM Sales", cnx)

df = (df_customer.merge(
                    df_sales, on= 'customer_id'
                ).merge(
                    df_orders, on= 'sales_id'
                ).merge(
                    df_item, on= 'item_id'
                )
                .query('age >= 18 and age <= 35')
                .groupby(['customer_id', 'age', 'item_id','item_name'])
                .agg(Quantity=pd.NamedAgg(column='quantity', aggfunc='sum'))
                .reset_index()
                .query('Quantity > 0')
                )

result_df = df[['customer_id', 'age', 'item_name', 'Quantity']].rename(columns={
    'customer_id': 'Customer',
    'age': 'Age',
    'item_name': 'Item',
    'quantity': 'Quantity'
})

result_df.to_csv(path_or_buf='../output/pandas_query_output.csv',sep=';', index=False)