import psycopg2

conn = psycopg2.connect(database="postgres",
                    host="localhost",
                    user="a",
                    password="a",
                    port="5432")

cursor = conn.cursor()
cursor.execute("INSERT INTO users(username,password,preference_key) VALUES('x',1,1);")

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())




#     # cursor.execute("INSERT INTO users(username,password,preference_key) VALUES('kike',1,1);")
#     cursor.execute("SELECT * FROM users")
#     print(cursor.fetchall())



# if __name__ == "__main__":
#     main()