import psycopg2

conn = psycopg2.connect(database="postgres",
                    host="postgres",
                    user="a",
                    password="a",
                    port="5432")
conn.autocommit = True

## Chain of responsability
class dbUser:
    #Class Variable
    username = "."
    valid = 1
    #init    
    def __init__(self, username):
        self.username = username
        self.valid = self.valid_user()

    #functions
    def fetch_user_key(self):
        if self.valid == -1:
            return -1
        pkUse = pkFetch
        return pkUse.pk_fetch(self.username)

    def valid_user(self):
        valUse = validateUser
        return valUse.valid_user(self.username)

class validateUser: 
    def valid_user(username):
        query = "SELECT username FROM users WHERE username = "
        query += "'" + str(username) +"'"
        query += ";"

        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()

        if (not res) :
            return -1
        else :
            return 1

class pkFetch:
    def pk_fetch(username):
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