import sqlite3

def checkTax(total):
    return total * 0.1 if total >= 2000000 else 0

fu_db = sqlite3.connect("Wage.sqlite")
cursor = fu_db.cursor()

init_script = """
DROP TABLE IF EXISTS Wage;

CREATE TABLE Wage
(
    Name TEXT,
    Hours FLOAT,
    Rate FLOAT,
    Total FLOAT,
    Tax FLOAT
);
"""
cursor.executescript(init_script)

# Mac dinh o day khi mo file la file txt se o cung folder voi file py
# neu khong cung folder thi se khong the mo duoc
data_raw = open('Database.txt')
num_line = 0
for line in data_raw:
    num_line += 1
    if num_line >= 3:
        lst = line.rstrip().split()
        name = lst[0]
        hours = float(lst[1])
        rate = float(lst[2])
        total = hours * rate
        tax = checkTax(total)
        cursor.execute("""INSERT INTO Wage(Name, Hours, Rate, Total, Tax)
        VALUES (?, ?, ?, ?, ?)""", (name, hours, rate, total, tax))
        fu_db.commit()

print('Lecturer list:')

# Ghi chu: De bai yeu cau in ra cac giang vien co so gio day > 5
# va DUOC SAP XEP THEO THU TU TANG DAN CUA SO GIO. Nhung sample output
# thi lai khong sap xep. Nen neu cac thay co cham trong truong khong sap
# xep thi co the bo cho em cum 'ORDER BY Hours asc' o dong duoi a.
# Em xin cam on

show_data = "SELECT * FROM Wage where Hours > 5 ORDER BY Hours asc"
cursor.execute(show_data)
data = cursor.fetchall()
print("Name\tHours\tRate\t\tTotal\t\tTax")
for row in data:
    print(row[0], row[1], row[2], row[3], row[4], sep = '\t')
fu_db.close()
