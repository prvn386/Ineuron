import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", database="carbon_nano", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "SELECT * from carbon_nano.UICdata;"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)

    for result in cursor.fetchall():
        print(result)
    mydb.close() # close the data base

except Exception as e:
    print(str(e))
    mydb.close()