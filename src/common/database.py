# CREATE TABLE info (
#         number INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         delay INT NOT NULL,
#         client_ip VARCHAR(30),
#         user_agent VARCHAR(50),
#         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#      );

import pymysql


class SQL:

    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='1234',
                                     db='history',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.c = self.connection.cursor()

    def select(self, sql):
        self.c.execute(sql)
        self.sel = self.c.fetchall()
        self.c.close()
        self.connection.close()
        return self.sel

    def update(self, sql, delay, client_ip, user_agent):
        self.c.execute(sql, (int(delay), client_ip, user_agent))
        self.upd = self.connection.commit()
        self.c.close()
        self.connection.close()
        return self.upd
    
    
