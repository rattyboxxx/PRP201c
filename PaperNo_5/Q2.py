import re

file = input('Enter file: ')
if len(file) == 0: file = 'Trace.txt'

fh = open(file)
mydict = dict()
for f in fh:
    if f.startswith('Name:'):
        tmp = f.strip().split()[1].split("-")[0]
        mydict[tmp] = mydict.get(f.split()[1].split("-")[0], 0) + 1

print('Troubleshoot wired LAN related issues:')
#print('Country\tCount')
for k,v in sorted(mydict.items()):
    print(k + ": " + str(v))