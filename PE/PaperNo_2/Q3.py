# input will be a string, like '[1, 2, 3, 4, 5]', and this line code below will seperate them into elements and append it to a list
lst = [int(x) for x in str(input('Input list: '))[1:-1].split(", ")]
n = len(lst)

pos1 = int(input('pos1: '))
pos2 = int(input('pos2: '))

if pos1 < 1 or pos1 > n or pos2 < 1 or pos2 > n:
    print('Error!')
else:
    lst[pos1-1], lst[pos2-1] = lst[pos2-1], lst[pos1-1]
print(lst)
