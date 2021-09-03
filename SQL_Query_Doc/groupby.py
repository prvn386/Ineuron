import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", user="root", database="carbon_nano", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "SELECT Chiral_indice_n ,count(Chiral_indice_n),Chiral_indice_m from UICdata group by Chiral_indice_n order by count(Chiral_indice_n)"

    result_dataframe = pd.read_sql(query,mydb)
    print(result_dataframe)

    mydb.close() # close the data base

except Exception as e:
    print(str(e))
    mydb.close()