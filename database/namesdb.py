import sqlite3


db = sqlite3.connect('names.db')
cursor=db.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS user(
  userid INTEGER  PRIMARY KEY,
  username VARCHAR(20) NOT NULL,
  name VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL);
  ''')



cursor.execute('''
INSERT INTO user (username,name,password)
VALUES ("premshanker","prem","password321")
''')

cursor.execute('''
INSERT INTO user (username,name,password)
VALUES ("vikashyap99","vikash","password321")
''')


db.commit()


cursor.execute("SELECT * FROM user")
print(cursor.fetchall())