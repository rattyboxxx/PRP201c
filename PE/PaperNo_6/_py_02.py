file = input('Enter file name: ')
if len(file) == 0: 
    file = 'mbox-short.txt'
fhand = open(file)
result=0
count =0
for line in fhand:
    if "X-DSPAM-Confidenece:" in line:
        a = line.find(":")
        result += float(line[a:].strip())
        count+=1
print("Average spam confidence: ",result/count)
