import mysql.connector
from mysql.connector import errorcode
import os

# Database connection details
DB_NAME = "Honda_Civic_History"
DB_USER = "root"
DB_PASSWORD = "aliahcakes"
DB_HOST = "localhost"
DB_PORT = 3306  # Replace with the correct port number (integer)

# Connection
def connect():
    try:
        con = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print('Connection successful')
        return con
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        elif err.errno == errorcode.ER_HOST_NOT_PRIVILEGED or err.errno == errorcode.ER_HOST_IS_BLOCKED:
            print(f"Error connecting to the database: {err}")
        else:
            print(f"Error connecting to the database: {err}")
        return None

# Create (Insert) Record
def add_civic_model():
    con = connect()
    try:
        while True:
            model_year = int(input('Enter Model Year: '))
            body_style_id = int(input('Enter Body Style ID (from available options): '))
            engine_type_id = int(input('Enter Engine Type ID (from available options): '))
            horsepower = int(input('Enter Horsepower: '))
            transmission = input('Enter Transmission (e.g., CVT, Manual): ')

            # Execute SQL
            cursor = con.cursor()
            sql = "INSERT INTO Civic_Models (Model_Year, Body_Style_ID, Engine_Type_ID, Horsepower, Transmission) VALUES (%s, %s, %s, %s, %s)"
            values = (model_year, body_style_id, engine_type_id, horsepower, transmission)
            cursor.execute(sql, values)
            con.commit()

            print('New Civic model record added successfully')
            x = input("Do you want to add another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
        print(err)

    else:
        cursor.close()
        con.close()

# Retrieve (Select) Records
def retrieve_civic_models(criteria=None):
    con = connect()
    try:
        cursor = con.cursor()

        if not criteria:
            # Retrieve all records
            sql = "SELECT cm.*, bs.Body_Style_Name, et.Engine_Description FROM Civic_Models cm INNER JOIN Body_Styles bs ON cm.Body_Style_ID = bs.Body_Style_ID INNER JOIN Engine_Types et ON cm.Engine_Type_ID = et.Engine_Type_ID ORDER BY cm.Model_Year DESC"
        else:
            # Retrieve based on criteria (e.g., model year, horsepower)
            sql = f"SELECT cm.*, bs.Body_Style_Name, et.Engine_Description FROM Civic_Models cm INNER JOIN Body_Styles bs ON cm.Body_Style_ID = bs.Body_Style_ID INNER JOIN Engine_Types et ON cm.Engine_Type_ID = et.Engine_Type_ID WHERE {criteria} ORDER BY cm.Model_Year DESC"

        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            print("Honda Civic Models:")
            for row in rows:
                print(f"  Model Year: {row[1]}")
                print(f"  Body Style: {row[6]}")
                print(f"  Engine Type: {row[3]}")
                print(f"  Horsepower: {row[4]}")
                print(f"  Transmission: {row[5]}")
                print()
        else:
            print("No records found based on the provided criteria.")

    except mysql.connector.Error as err:
        print(err)

    else:
        cursor.close()
        con.close()

# Update Record
def update_civic_model():
    con = connect()
    try:
        while True:
            model_id = int(input('Enter Model ID of the record to update: '))
            update_choice = input('Update (1) Body Style, (2) Engine Type, (3) Horsepower, (4) Transmission: ')

            cursor = con.cursor()
            if update_choice == '1':
                new_body_style_id = int(input('Enter new Body Style ID: '))
                sql = "UPDATE Civic_Models SET Body_Style_ID = %s WHERE Model_ID = %s"
                values = (new_body_style_id, model_id)
            elif update_choice == '2':
                new_engine_type_id = int(input('Enter new Engine Type ID: '))
                sql = "UPDATE Civic_Models SET Engine_Type_ID = %s WHERE Model_ID = %s"
                values = (new_engine_type_id, model_id)
            elif update_choice == '3':
                new_horsepower = int(input('Enter new Horsepower: '))
                sql = "UPDATE Civic_Models SET Horsepower = %s WHERE Model_ID = %s"
                values = (new_horsepower, model_id)
            elif update_choice == '4':
                new_transmission = input('Enter new Transmission: ')
                sql = "UPDATE Civic_Models SET Transmission = %s WHERE Model_ID = %s"
                values = (new_transmission, model_id)
            else:
                print("Invalid update choice. Please try again.")
                continue

            cursor.execute(sql, values)
            con.commit()

            print('Civic model record updated successfully')
            x = input("Do you want to update another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
        print(err)

    else:
        cursor.close()
        con.close()

# Delete Record
def delete_civic_model():
    con = connect()
    try:
        while True:
            model_id = int(input('Enter Model ID of the record to delete: '))

            cursor = con.cursor()
            sql = f"DELETE FROM Civic_Models WHERE Model_ID = %s"
            value = (model_id,)
            cursor.execute(sql, value)
            con.commit()

            print('Civic model record deleted successfully')
            x = input("Do you want to delete another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
        print(err)

    else:
        cursor.close()
        con.close()

def main():
    while True:
        os.system('cls')  # Clear the console
        print("\nHonda Civic History Management System")
        print("1. Add New Civic Model")
        print("2. View Civic Models")
        print("3. Update Civic Model")
        print("4. Delete Civic Model")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system('cls')
            con = connect()
            add_civic_model()
        elif choice == "2":
            os.system('cls')
            con = connect()
            criteria = input("Enter search criteria (e.g., Model Year > 2020): ")
            retrieve_civic_models(criteria)
        elif choice == "3":
            os.system('cls')
            con = connect()
            update_civic_model()
        elif choice == "4":
            os.system('cls')
            con = connect()
            delete_civic_model()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

        x = input("Return to main menu [y/n]? ")
        if x != 'y':
            break

if __name__ == "__main__":
    main()