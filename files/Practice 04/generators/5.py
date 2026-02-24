def numbers(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
x = numbers(n)
for i in x:
    print(i, end = " ")