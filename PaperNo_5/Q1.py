def convert(n):
    if n <= 0: return None
    res = ""
    while n > 0:
        res = str(n%2) + res
        n //= 2
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

print(n, 'is converted into binary:', convert(n))
