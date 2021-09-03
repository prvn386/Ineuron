import mysql.connector as connection

try:
    mydb = connection.connect(host = "localhost",user = "root", passwd = "Password2!",use_pure = True)
    # check if connection is established or not
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    print(str(e))