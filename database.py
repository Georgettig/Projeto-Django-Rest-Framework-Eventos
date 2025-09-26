import pandas as pd
import sqlite3

conn = sqlite3.connect('db.sqlite3')

tabelas = pd.read_sql_query('select name from sqlite_master where type="table";', conn)

eventos = pd.read_sql_query('select * from eventin_evento', conn)
participantes = pd.read_sql_query('select * from eventin_participante', conn)

conn.close()

print(eventos)
print(participantes)