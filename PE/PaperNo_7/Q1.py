def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
    return sum == n

while True:
    n = input("Enter a positive integer number: ")
    try:
        n = int(n)
        if n < 1:
            print("The number must be positive.")
        else:
            break
    except:
        print("The number must be a positive number.")

print(f"The perfect numbers from 0 to {n}:")
for i in range(n+1):
    if is_perfect(i):
        print(i, end=" ")