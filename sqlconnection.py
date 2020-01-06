import mysql.connector

class MySQLConnection():
    def __init__(self, db):
        config = {
            'host':'localhost',
            'database': db,
            'user':'root',
            'password':'root',
            'port':'3305'
        }
        self.cnx = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'], database=config['database'], port=config['port'])
    def query_db(self, query, data=None):
        result = self.cnx.cursor().execute(text(query))
        if query[0:6].lower() == 'insert':
            self.cnx.commit()
            return result.lastrowid
        

def MySQLConnector(db):
    return MySQLConnection(db)
    
mysqldb = MySQLConnector('AmazonPriceTracker')
mysqldb.query_db('''INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
                    VALUES ('Eric', 'Greenhalgh', 'egreenhalgh@gmail.com', '1234', NOW(), NOW())''')