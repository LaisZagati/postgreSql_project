import psycopg2

#connect to "chinook" database
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "artist"')

# Query 2 - select all records from the "Artist" table
cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "artist" WHERE "name" = %s' , ["Queen"])

# Query 4 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "artist" WHERE "name" = %s' , ["Queen"])


#fetch the results (multiple)
# results = cursor.fetchall()

#fetch the results (single)
results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)