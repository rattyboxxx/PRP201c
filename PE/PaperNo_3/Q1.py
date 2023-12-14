import math

def checkPerfect(n):
    if (n < 2): return False
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0: sum += i
    return n == sum

def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

while True:
    n = str(input('Enter a positive integer number: '))
    try:
        n = int(n)
        if n < 1: print('The number must be positive.')
        else: break
    except:
        print('The number must be a positive number.')

print('The perfect numbers from 0 to ' + str(n) + ":")
for i in range(n+1):
    if checkPrime(i): print(i, end=" ")
