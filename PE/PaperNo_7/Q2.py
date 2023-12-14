name = input("Enter file:")
name = "DNSList.txt"

mydict = dict()

file = open(name)
for line in file:
    if line.startswith("Location:"):
        if "United" in line:
            mydict["United"] = mydict.get("United", 0) + 1
        else:
            country = line[10:].strip()
            mydict[country] = mydict.get(country, 0) + 1

print("DNS server list:")
print("Country\tCount")
for key, value in sorted(mydict.items()):
    print(key, value, sep="\t")

file.close()