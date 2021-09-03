import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database="carbon_nano", user="root", passwd="mysql", use_pure=True)
    # check if connection is established or not
    print(mydb.is_connected())

    query = "create table if not exists carbon_nano.UICdata (Chiral_indice_n VARCHAR(15),Chiral_indice_m VARCHAR(15)," \
            "Initial_atomic_coordinate_u VARCHAR(15),Initial_atomic_coordinate_v VARCHAR(15)," \
            "Initial_atomic_coordinate_w VARCHAR(15)," \
            "Calculated_atomic_coordinates_u VARCHAR(15),Calculated_atomic_coordinates_v VARCHAR(15)," \
            "Calculated_atomic_coordinates_w VARCHAR(15))"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Table is created")
    mydb.close()

except Exception as e:
    print(str(e))
    mydb.close()
