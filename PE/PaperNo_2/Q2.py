# input will be a string, like '[1, 2, 3, 4, 5]', and this line code below will seperate them into elements and append it to a list
lst = [int(x) for x in str(input('Input list: '))[1:-1].split(", ")]
n = len(lst)

for i in range(n):
    min = None
    for j in range(i, n):
        if min is None:
            min = j
        elif lst[min] > lst[j]:
            min = j
    lst[i], lst[min] = lst[min], lst[i]

print('Sorted array')
for i in lst:
    print(i)
