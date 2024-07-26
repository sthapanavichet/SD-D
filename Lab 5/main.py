import psycopg2

print("Connecting to the database")
connection = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '123')

if not connection.closed:
    print("Connection was successful")

    cursor = connection.cursor()

    create_table_query = 'CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR, email VARCHAR, age INTEGER);'
    cursor.execute(create_table_query)

    insert_query = """INSERT INTO users VALUES
    (1, 'John Doe', 'john.doe@example.com', 30), 
    (2, 'Jane Smith', 'jane.smith@example.com', 28),
    (3, 'Michael Johnson','michael.johnson@example.com', 35)"""
    cursor.execute(insert_query)


    select_query = 'SELECT * FROM users'
    print("Result from SELECT query:")
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    connection.close()
else:
    print("Connection failed")