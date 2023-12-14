import re

password = input('Input a sequence of password: ').split(',')
pattern = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$"
res = list()
for p in password:
    if re.search(pattern, p): res.append(p)
print(",".join(res))
