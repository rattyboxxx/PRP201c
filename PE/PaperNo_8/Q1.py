def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    n = input("Enter a positive integer number: ")
    while True:
        try:
            n = int(n)
            if n > 0:
                print(f"Fibonacci sequence 1 - {n}:")
                res = [fib(i) for i in range(n + 1)]
                print(str(res)[1:-1])
                break
        except:
            continue


if __name__ == "__main__":
    main()
