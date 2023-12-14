# print and sort list of students
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return self.name + "\t" + self.age + "\t" + self.score

def student():
    res = list()
    while True:
        res.append(Student(input("Enter name: "), input("Enter age: "), input("Enter score: ")))
        while True:
            ch = input('Continue? (y/n): ')
            if ch.lower() in ['y', 'n']: break
        if ch.lower() == 'n': break
        print()
    for p in res: print(p)
    print()
    res.sort(key=lambda x: x.name)
    for p in res: print(p)

student()
