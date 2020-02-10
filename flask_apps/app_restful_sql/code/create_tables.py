#import

import sqlite3

#cria conexao e cursor

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#cria string de criacao sql da tabela
create_table_string = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table_string)

select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()