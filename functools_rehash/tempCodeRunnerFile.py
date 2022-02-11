import duckdb
conn = duckdb.connect('sales.duckdb')
cursor = conn.cursor()
 
cursor.execute("""
CREATE TABLE sales(
   Transaction_date date 
  ,Product          varchar 
  ,Price            bigint  
  ,Payment_Type     varchar 
  ,Name             varchar 
  ,City             varchar 
  ,State            varchar 
  ,Country          varchar 
  ,Account_Created  varchar 
  ,Last_Login       varchar 
  ,Latitude         double 
  ,Longitude        double 
)
"""
)
 
cursor.execute("COPY sales FROM 'sales.csv' (HEADER)")
 
print(cursor.execute('select count(*) from sales').fetchall())
cursor.close()
conn.close()