def convert(n):
    if n <= 0: return None
    res = ''
    mydict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    while n > 0:
        if n % 16 < 10:
            res = str(n%16) + res
        else:
            res = mydict[n%16] + res
        n //= 16
    return res

while True:
    n = input('Enter a positive integer number: ')
    try:
        n = int(n)
        if n <= 0:
            print('The number must be positive.')
        else:
            break
    except:
        print('The number must be a positive number.')

print(n, 'is converted into hexadecimal:', convert(n))
