str1= input("Input String 1: ")
str2= input("Input String 2: ")
numbool=False
existbool1=False
existbool2=False
anagram =True
#dam bao 2 day co do dai bang nhau
if len(str1) ==len(str2):
    numbool =True
#dam bao cac ky tu co trong str1 phai co trong str2 va nguoc lai
for i in range(len(str1)) :
    for j in range(len(str2)) :
        if str1[i] == str2[j]:
            existbool1 =True

for i in range(len(str2)) :
    for j in range(len(str1)) :
        if str1[i] == str2[j]:
            existbool2 =True
#dam bao str1 va str2 phai la su sap xep xao tron cua string 1
    if str1==str2:
        anagram = False
if numbool and existbool1 and existbool2 and anagram:
    print("Anagram(",str1,',',str2,')->',True)
else:
    print("Anagram(",str1,',',str2,')->',False)

