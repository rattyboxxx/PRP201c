import sqlite3

db = sqlite3.connect("scholarship.sqlite")
cursor = db.cursor()

init_script = """
DROP TABLE IF EXISTS CLASS;

CREATE TABLE CLASS
(
    ClassID TEXT,
    ClassName TEXT
);

DROP TABLE IF EXISTS STUDENT;
CREATE TABLE STUDENT
(
    SID TEXT,
    SName TEXT,
    ClassID TEXT REFERENCES CLASS(ClassID),
    GPA FLOAT
);
"""
cursor.executescript(init_script)

# Mac dinh o day khi mo file la file txt se o cung folder voi file py
# neu khong cung folder thi se khong the mo duoc
data_raw = open("Sholarship.txt", "r")

myclass = set()

for idx, line in enumerate(data_raw):
    if idx > 0:
        lst = line.strip().split("\t")

        SID = lst[0]
        SName = lst[1]
        ClassID = lst[2]
        ClassName = lst[3]
        GPA = float(lst[4])

        myclass.add((ClassID, ClassName))

        cursor.execute(
            """INSERT INTO STUDENT(SID, SName, ClassID, GPA) VALUES (?, ?, ?, ?)""",
            (SID, SName, ClassID, GPA),
        )
        db.commit()

for ele in myclass:
    cursor.execute(
        """INSERT INTO CLASS(ClassID, ClassName) VALUES (?, ?)""",
        ele,
    )
    db.commit()

print("Excellent Students:")

show_data = "SELECT SName, ClassName, GPA, 5000000 as 'Scholar' FROM STUDENT, CLASS WHERE GPA >= 8.5 AND STUDENT.ClassID = CLASS.ClassID ORDER BY SName ASC"
cursor.execute(show_data)
data = cursor.fetchall()

print("Student Name\tClass\t\t\t\tGPA\tScholar")

for ele in data:
    for col in ele:
        print(col, end="\t")
    print()

db.close()
