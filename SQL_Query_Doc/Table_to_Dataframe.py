import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", user="root", database="carbon_nano", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "SELECT * from carbon_nano.UICdata;"

    dataframe = pd.read_sql(query,mydb) # read the table
    print(dataframe)
    mydb.close() # close the data base

except Exception as e:
    print(str(e))
    mydb.close()