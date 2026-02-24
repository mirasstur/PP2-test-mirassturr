def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(",".join(str(x) for x in even_numbers(n)))