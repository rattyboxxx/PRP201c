import sqlite3
import re

def checkTax(total):
    return total * 0.05 if total >= 9000000 else 0
        
fu_db = sqlite3.connect("employee.sqlite")
cursor = fu_db.cursor()

init_script = """
DROP TABLE IF EXISTS employee;

CREATE TABLE employee
(
    Name TEXT,
    rate FLOAT,
    salary int,
    Total FLOAT,
    Tax FLOAT
);
"""
cursor.executescript(init_script)

data_raw = open('Data.txt')
num_line = 0
for line in data_raw:
    num_line += 1
    if num_line >= 3:
        lst = line.strip().split()
        print(lst)
        if len(lst) == 0: continue
        Name = lst[0]
        rate = float(lst[1])
        salary = int(lst[2])
        Total = rate * salary
        Tax = checkTax(Total)
        cursor.execute("""INSERT INTO employee(Name, rate, salary, Total, Tax)
        VALUES (?, ?, ?, ?, ?)""", (Name, rate, salary, Total, Tax))
        fu_db.commit()

print('employee list:')

show_data = "SELECT * FROM employee where rate > 3 ORDER BY Name asc"
cursor.execute(show_data)
data = cursor.fetchall()
print("Name\trate\tsalary\tTotal\t\tTax")
for row in data:
    print(row[0], row[1], row[2], int(row[3]), row[4], sep = '\t')
fu_db.close()
