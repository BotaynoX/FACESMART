import mysql.connector
from mysql.connector import Error
import datetime
def connect_to_database(host, database, user, password):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
        else:
            print('Failed to connect to MySQL database')
            return None
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def fetch_images_from_database(connection, table_name):
    import cv2
    import numpy as np
    images = []
    ids_names = []
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, prenom, photo FROM {table_name}")
        persons = cursor.fetchall()
        for person in persons:
            nparr = np.frombuffer(person[2], np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            images.append(img)
            ids_names.append((person[0], person[1]))  # (id, name) tuple
    except Error as e:
        print(f"Error fetching images from the database: {e}")
    finally:
        if cursor:
            cursor.close()
    return images, ids_names

def login(email, password, connection):
    if connection is None:
        print("No database connection available.")
        return False

    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    return user is not None


def AfficheDa(connection):
    try:
        db = connection
        cursor = db.cursor()

        query = "SELECT id,nom,prenom,email,password,departement FROM employee"
        cursor.execute(query)
        employee_list = cursor.fetchall()

        cursor.close()
        return employee_list
    except mysql.connector.Error as error:
        print("Error occurred while fetching employee list:", error)
        return []
    
def insert_employee(nom, prenom, email, password, departement, image_data):
    conn = connect_to_database("localhost","face_smart","root","")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employee (nom, prenom, email, password, departement, photo)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (nom, prenom, email, password, departement, image_data))
    conn.commit()
    cursor.close()
    conn.close()

def mark_presence(con, id):
    try:
        # Get current datetime
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        
        # Create a cursor object
        cur = con.cursor()
        
        # SQL query to select the presence records for the given employee on the current date
        query = f"SELECT statu, date_travail FROM presence WHERE id_employee = {id} AND DATE(date_travail) = '{current_date}' ORDER BY date_travail DESC LIMIT 1"
        
        # Execute the SQL query
        cur.execute(query)
        
        # Fetch the latest record for the current date
        latest_record = cur.fetchone()
        
        # Check if there's already a record for today
        if latest_record:
            last_status, last_datetime = latest_record
            
            # Calculate the time difference between the current time and the last record time
            time_difference = current_datetime - last_datetime
            
            # If the last record is "in" and the time difference is less than 1 minute, ignore
            if last_status == "in" and time_difference.total_seconds() < 60:
                return "Ignored"
            
            # If the last record is "out" and the time difference is less than 1 minute, ignore
            if last_status == "out" and time_difference.total_seconds() < 60:
                return "Ignored"
        
        # If there's no record for today or the time difference is more than 1 minute, insert new record
        if not latest_record or time_difference.total_seconds() >= 60:
            # Determine the status based on the last record
            new_status = "out" if latest_record and latest_record[0] == "in" else "in"
            
            # SQL query to insert a new record marking the person with determined status
            insert_query = f"INSERT INTO presence (id_employee, date_travail, statu) VALUES (%s, %s, %s)"
            # Execute the insert query
            cur.execute(insert_query, (id, current_datetime, new_status))
            # Commit the transaction
            con.commit()
            
            # Return the status marked
            return new_status
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the cursor
        if cur:
            cur.close()
            
def calculate_work_time(con, id, date):
    try:
        # Create a cursor object
        cur = con.cursor()
        
        # SQL query to select the "in" and "out" records for the given employee on the specified date
        query = f"SELECT date_travail, statu FROM presence WHERE id_employee = {id} AND DATE(date_travail) = '{date}' ORDER BY date_travail"
        
        # Execute the SQL query
        cur.execute(query)
        
        # Fetch all records
        records = cur.fetchall()
        
        # Initialize variables to accumulate work time
        total_work_time = datetime.timedelta()
        last_in_time = None
        
        # Iterate through the records
        for date_time, status in records:
            if status == "in":
                last_in_time = date_time
            elif status == "out":
                if last_in_time is not None:
                    # If there's a corresponding "in" record, calculate the work duration and accumulate it
                    work_duration = date_time - last_in_time
                    total_work_time += work_duration
                    last_in_time = None  # Reset last_in_time for next iteration
                else:
                    # If there's no corresponding "in" record, ignore the "out" record
                    print(f"Ignored 'out' record without preceding 'in' record.")
        
        # Check if there are any remaining "in" records without corresponding "out" records
        if last_in_time is not None:
            print(f"Ignored 'in' record without corresponding 'out' record.")
        
        # Print the total work time
        print(f"Total work time for Employee {id} on {date}: {total_work_time}")
        
        # Return the total work time
        return total_work_time
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the cursor
        if cur:
            cur.close()
def get_status_by_id(employee_id):
    # Connect to the database
    connection = connect_to_database(
        host='localhost',
        database='face_smart',
        user='root',
        password=''
    )
    if connection is None:
        print("Failed to connect to the database.")
        return None

    # Execute SQL query to retrieve status for the given employee ID with the maximum date
    cursor = connection.cursor()
    query = """
        SELECT statu
        FROM presence
        WHERE id_employee = %s
        ORDER BY date_travail DESC
        LIMIT 1
    """
    cursor.execute(query, (employee_id,))
    status = cursor.fetchone()  # Assuming it returns a single value
    connection.close()

    if status is not None:
        return status[0]  # Assuming status is the first column in the result
    else:
        return None

def checkStatus( employee_id):
    # Assuming you have a database function to retrieve status for an employee ID
    status = get_status_by_id(employee_id)
    
    # Assuming status is returned as a string
    return status

def delete_employee( employee_id):
    try:
        connection = connect_to_database(
            host='localhost',
            database='face_smart',
            user='root',
            password=''
        )
        if connection is None:
            print("Failed to connect to the database.")
            return None


        # Execute SQL query to retrieve status for the given employee ID with the maximum date
        cursor = connection.cursor()
  
        query = "DELETE FROM employee WHERE id = %s"
        cursor.execute(query, (employee_id,))
        connection.commit()
        return cursor.rowcount > 0  # Returns True if a row was deleted
    except Error as e:
        print(f"Error: {e}")
        return False
