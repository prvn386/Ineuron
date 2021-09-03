import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "Create database carbon_nano;"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Database is created")
    mydb.close()

except Exception as e:
    print(str(e))
    mydb.close()