import sqlite3

def checkgrade(grade):
    if grade >=8:
        return 'A'
    elif grade >=7:
        return 'B'
    else :
        return ' '
fu_db = sqlite3.connect("Scholar.sqlite")
cursor = fu_db.cursor()

init_script = """
DROP TABLE IF EXISTS Student;

CREATE TABLE Student
(
    Name TEXT,
    term INTEGER,
    grade FLOAT,
    Scholar TEXT
);
"""
cursor.executescript(init_script)
data_raw = open("Data.txt")
num_line = 1
for line in data_raw:
    num_line += 1
    if num_line == 2 :
        continue
    lst = line.rstrip().split()
    name = lst[0]
    term = int(lst[1])
    grade = float(lst[2])
    Scholar = checkgrade(grade)
    cursor.execute("""INSERT INTO Student(Name, term, grade, Scholar)
    VALUES (?, ?, ?, ?)""", (name, term, grade, Scholar))
    fu_db.commit()

print('Scholar list:')
show_data = "SELECT * FROM Student ORDER BY grade desc"
cursor.execute(show_data)
data = cursor.fetchall()
print("Name\tterm\tgrade\tScholar")
for row in data:
    print(row[0], row[1], row[2], row[3], sep = '\t')
fu_db.close()