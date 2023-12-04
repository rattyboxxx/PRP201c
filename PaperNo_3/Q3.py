import sqlite3

db = sqlite3.connect('DNSList.sqlite')
cursor = db.cursor()

init_script = """
DROP TABLE IF EXISTS DNS;

CREATE TABLE DNS
(
    IP TEXT,
    Reliability INTEGER,
    Description TEXT
);
"""
cursor.executescript(init_script)

file = open("DNSList.txt")
for line in file:
    if line.startswith('IP Address:'):
        lst = line.strip().split()
        ip = lst[2][:-1]
        rel = int(lst[3])
        if rel < 50: des = 'Low'
        else: des = 'Normal'
        cursor.execute("""INSERT INTO DNS(IP, Reliability, Description)
        VALUES (?, ?, ?)""", (ip, rel, des))
        db.commit()


show_data = "SELECT * FROM DNS ORDER BY Reliability DESC"
cursor.execute(show_data)
data = cursor.fetchall()
print("DNS server list:")
print(" IP\t\t  Reliability\tDescription")
for row in data:
    print(row[0] + "\t   ", row[1], '\t\t' + row[2])
db.close()
