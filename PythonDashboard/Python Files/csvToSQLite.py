import csv, sqlite3, sys, re, os

fullFileName = sys.argv[1]
tableName = fullFileName.replace(".log","")

directory = 'C:\\SQLite\\Databases\\'

if not os.path.exists(directory):
    os.makedirs(directory)

connection = sqlite3.connect(directory + 'testPython.db')
createTable = 'CREATE TABLE IF NOT EXISTS ' + tableName + ' (IPAddress text, Datestamp text, Timestamp text, Method text, URL text, HTTPCode text, Referrer text, UserAgent text)'
cursor = connection.cursor()
cursor.execute(createTable)

with open(fullFileName, 'rb') as f:
    dr = csv.DictReader(f, delimiter='|')
    insertQuery = [(i['IPAddress'], i['Datestamp'], i['Timestamp'], i['Method'], i['URL'], i['HTTPCode'], i['Referrer'], i['UserAgent']) for i in dr]

cursor.executemany('INSERT INTO ' + tableName + '(IPAddress, Datestamp, Timestamp, Method, URL, HTTPCode, Referrer, UserAgent) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', insertQuery)
connection.commit()
connection.close()
