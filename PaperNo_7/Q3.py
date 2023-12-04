import sqlite3

def checkDes(reli: int) -> str:
    if reli < 50:
        return "Low"
    return "Normal"

fu_db = sqlite3.connect("DNSList.sqlite")
cursor = fu_db.cursor()

init_script = """
DROP TABLE IF EXISTS DNS;

CREATE TABLE DNS
(
    IP TEXT,
    Reliability INTERGER,
    Description TEXT
);
"""
cursor.executescript(init_script)

# Mac dinh o day khi mo file la file txt se o cung folder voi file py
# neu khong cung folder thi se khong the mo duoc
data_raw = open('DNSList.txt')

reli = None

for line in data_raw:
    if "IP" in line:
        ip = line.strip().split()[2][:-1]
    if "Reliability" in line:
        reli = int(line.strip().split()[1][:-1])
    if reli is not None:
        des = checkDes(reli)

    if reli is not None:
        cursor.execute("""INSERT INTO DNS(IP, Reliability, Description)
        VALUES (?, ?, ?)""", (ip, reli, des))
        reli = None
        fu_db.commit()

print('DNS Server list:')

show_data = "SELECT * FROM DNS ORDER BY Reliability DESC"
cursor.execute(show_data)
data = cursor.fetchall()
print(" IP\t\tReliability\t Description")

# for row in data:
#     print(row[0] + "\t    " + str(row[1]) + "\t\t" + row[2])
# fu_db.close()

head = data[:2]
tail = data[-6:]

for row in head:
    print(row[0] + "\t    " + str(row[1]) + "\t\t" + row[2])
print("....")
for row in tail:
    print(row[0] + "\t    " + str(row[1]) + "\t\t" + row[2])

fu_db.close()
