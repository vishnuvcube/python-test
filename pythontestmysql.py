import mysql.connector

try:
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vishnu@1234.",
        database="vishnu5pm"
    )

    # Create a cursor object to interact with the database
    cursor = db_connection.cursor()

    # Create table if not exists
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
    '''
    cursor.execute(create_table_query)
    print(f"Rows affected by CREATE TABLE: {cursor.rowcount}")

    # Insert data into the table
    insert_query = '''
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES (%s, %s, %s, %s)
    '''
    student_data = ("Alice", "Smith", 18, 95.5)
    cursor.execute(insert_query, student_data)
    print(f"Rows affected by INSERT: {cursor.rowcount}")
    db_connection.commit()

    # Update data in the table
    update_query = '''
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
    '''
    update_data = (97.0, "Alice")
    cursor.execute(update_query, update_data)
    print(f"Rows affected by UPDATE: {cursor.rowcount}")
    db_connection.commit()

    # Delete data from the table
    delete_query = '''
    DELETE FROM students
    WHERE last_name = %s
    '''
    delete_data = ("Smith",)
    cursor.execute(delete_query, delete_data)
    print(f"Rows affected by DELETE: {cursor.rowcount}")
    db_connection.commit()

    # Select and display all records from the table
    select_query = '''
    SELECT * FROM students
    '''
    cursor.execute(select_query)
    students = cursor.fetchall()

    print("Student Records:")
    for student in students:
        print(student)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and database connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()

    if 'db_connection' in locals() and db_connection.is_connected():
        db_connection.close()
