n = int(input())

def specific_numbers(n):
    for i in range(0, n + 1, 12):
        yield i
x = specific_numbers(n)
for i in x:
    print(i, end =" ")