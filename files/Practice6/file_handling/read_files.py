with open (r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt") as f:
    print(f.readline())
    print(f.read(5))
    f.close()
    
with open (r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt") as f:
    print(f.readline())
    print(f.readline())
    f.close()
print("-"*100)
with open (r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt") as f:
    for x in f:
        print(x)
    f.close()
