with open("numbers.txt", "r") as file:
    lst = list()
    for line in file:
        lst = lst + line.strip().split(", ")
    print(f"The origin numbers: {str(lst)}")
    print("The sorted numbers: [", end="")
    lst = [str(i) for i in sorted([int(i) for i in lst], reverse=True)]
    print(", ".join(lst) + "]")
