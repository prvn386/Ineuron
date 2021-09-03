import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", database="carbon_nano", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "UPDATE carbon_nano.UICdata SET Chiral_indice_n = 20,Chiral_indice_m = 30 WHERE Initial_atomic_coordinate_u like '%679005%'"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    mydb.commit()

    # lets confirm if the value updated or not
    query = "SELECT * from carbon_nano.UICdata WHERE Initial_atomic_coordinate_u like '%679005%'"
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

    mydb.close() # close the data base

except Exception as e:
    print(str(e))
    mydb.close()