number: int = int(input("Enter a number: "))

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def get_pattern(n):
    pattern = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            pattern += str(j)
        pattern += "\n"
    return pattern

result = get_pattern(number)
print(result)


