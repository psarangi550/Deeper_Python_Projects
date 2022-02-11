import duckdb
conn = duckdb.connect('product.duckdb')
cursor = conn.cursor()
 
cursor.execute('create table product( id int primary key , name varchar(255))')
 
cursor.close()
conn.close()