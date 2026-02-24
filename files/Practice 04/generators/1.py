n = int(input())
numbers = list(x * x for x in range(1, n + 1))
print(numbers)

def squares(n):
    for i in range(n+1):
        yield (i**2)
print(" ".join(str(x) for x in squares(n)))
