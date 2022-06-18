import psycopg2

conn = psycopg2.connect(database="postgres",
                    host="postgres",
                    user="a",
                    password="a",
                    port="5432")
conn.autocommit = True

def add_user(username, password, preference_key):

    query = "INSERT INTO users(username,password,preference_key) VALUES("
    query += "'" + str(username) +"'" + ","
    query += "'" + str(password) +"'" + ","
    query += str(preference_key)
    query += ");"

    cursor = conn.cursor()
    cursor.execute(query)
    
    return "Succesfully Added "+ username+" Into DB "
