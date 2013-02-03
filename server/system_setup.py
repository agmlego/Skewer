#!/usr/bin/env python
import ConfigParser, psycopg2 as sql

config = ConfigParser.SafeConfigParser()
config.readfp(open('skewer.ini'))

user = config.get('database','user')
password = config.get('database','password')
server = config.get('database','server')
port = config.get('database','port')
database = config.get('database','database')
inventory_table = config.get('database','inventory_table')

db = sql.connect(database=database, user=user, password=password, host=server, port=port)
cur = db.cursor()
    
cur.execute("select exists(select * from information_schema.tables where table_catalog='%s' and table_name='%s')"%(database,inventory_table,))
exists = cur.fetchone()[0]
    
if exists:
    cur.execute('select * from %s;'%inventory_table)
    print 'Inventory table found, %d rows!'%cur.rowcount
else:
    cur.execute('create table %s (idx SERIAL PRIMARY KEY, code TEXT, description TEXT, size TEXT, type TEXT, quantity INTEGER, lastUsed TIMESTAMP, lastAdded TIMESTAMP);'%inventory_table)
    print 'Inventory table %s created'%inventory_table

db.commit()

cur.close()
db.close()
