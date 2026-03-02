import importlib

        

q = int(input())
for i in range(q):
    m,pat = input().split()
    try:
        modu = importlib.import_module(m)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    try:
        atr = getattr(modu, pat)
        if callable(atr):
            print("CALLABLE")
        else: print("VALUE")
    except AttributeError:
        print("ATTRIBUTE_NOT_FOUND")
        
