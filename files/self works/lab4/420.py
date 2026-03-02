q = int(input())
g = n= 0
for i in range(q):
    var, x = input().split()
    if var == "global":
        g+=int(x)
    elif var == "nonlocal":
        n+=int(x)
print(g,n)