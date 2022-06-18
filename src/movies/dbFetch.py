import psycopg2

conn = psycopg2.connect(database="postgres",
                    host="postgres",
                    user="a",
                    password="a",
                    port="5432")
conn.autocommit = True

def fetch_user_key(username):

    query = "SELECT preference_key FROM users WHERE username = "
    query += "'" + str(username) +"'"
    query += ";"

    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()

    if (not res) :
        return -1
    else :
        return res[0][0]

