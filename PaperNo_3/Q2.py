import re

file = input('Enter file: ')
if len(file) == 0: file = 'DNSList.txt'

fh = open(file)
mydict = dict()
for f in fh:
    if f.startswith('Location: '):
        tmp = re.findall("Location: (.+)", f)
        for t in tmp:
            mydict[t.strip().split()[0]] = mydict.get(t.strip().split()[0], 0) + 1
print('DNS server list:')
print('Country\tCount')
for k,v in sorted(mydict.items()):
    print(k + "\t" + str(v))
