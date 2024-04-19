from database import database
import pandas as pd
import sqlite3

# first method using sql query 
# path to the database file
path_to_db = "D:\projects\database\Data Engineer - Assignment Database@eastVantage.db"

db = database(path = path_to_db)

result_sql = db.get_targeted_customers()

# storing the final result using sql in csv (;) separated files in output folder 
result_sql.to_csv(path_or_buf='../output/sql_query_output.csv',sep=';', index=False)

# Second method using Pandas
cnx = sqlite3.connect(path_to_db)

df_items = pd.read_sql_query("SELECT * FROM Items", cnx)
df_customers = pd.read_sql_query("SELECT * FROM Customers", cnx)
df_orders = pd.read_sql_query("SELECT * FROM Orders", cnx)
df_sales = pd.read_sql_query("SELECT * FROM Sales", cnx)

df = (df_customers.merge(
                    df_sales, on= 'customer_id'
                ).merge(
                    df_orders, on= 'sales_id'
                ).merge(
                    df_items, on= 'item_id'
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

result_df['Quantity'] = result_df['Quantity'].astype(int)

# storing the final result using pandas in csv (;) separated files in output folder 
result_df.to_csv(path_or_buf='../output/pandas_query_output.csv',sep=';', index=False)