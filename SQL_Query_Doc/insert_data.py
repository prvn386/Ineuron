import mysql.connector as connection
import csv

try:
    mydb = connection.connect(host="localhost", database="carbon_nano", user="root", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    cursor = mydb.cursor()

    with open('carbon_formatted.csv', 'r') as data: # open a csv file in read format
        next(data)
        data_reader = csv.reader(data, delimiter='\n') # reading the csv file using csv reader
        for i in enumerate(data_reader):
            # print(i)
            for j in i[1]:
                cursor.execute("Insert into carbon_nano.UICdata values ({data})".format(data=j))  # each row is inserted into the table
        print("Complete Data insertion is successfull")
    mydb.commit()  # commit is done to finish the insertion of data
    mydb.close()

except Exception as e:
    print(str(e))
    mydb.close()