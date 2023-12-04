# Ghi chu: Theo nhu sample output thi em hieu la cac tu duoc coi la
# ordered word khi cac chu cai cua no xuat hien theo thu tu tang dan
# cua BANG MA ASCII, chu khong phai chi theo ALPHABET.
# Don cu nhu trong sample output co tu 'You', thi neu theo alphabet
# thi 'Y' phai dung sau 'o', nen no khong the la ordered word.
# Vay nen em nghi no la sap theo bang ma ASCII
# Nhung neu the thi trong file words.txt co 1 so tu nhu 'a', 'in',
# 'To' cung thoa man yeu cau nhung lai khong duoc liet ke trong
# sample output.
# Vay nen bai lam cua em ket qua se khac sample output, mong cac thay co
# cham bai xem lai sample output giup em voi a. Em xin cam on

def check(s):
    n = len(s)
    for i in range(n-1):
        if s[i] > s[i+1]: return False
    return True

file = input('Enter file: ')
if len(file) == 0: file = 'words.txt'
# Mac dinh o day khi mo file la file txt se o cung folder voi file py,
# neu khong cung folder thi se khong the mo duoc
fh = open(file)

res = list()

for f in fh:
    s = f.strip().split()
    for ele in s:
        if check(ele):
            res.append(ele)

print('The ordered words:')
print(res)
