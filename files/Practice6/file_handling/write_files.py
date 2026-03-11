with open(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt") as f:
    print(f.read())
    f.close()

print("\nafter adding text\n")

with open (r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt", "a") as f:
    f.write("\nI writing this text using append mode and .write() method")
    f.close()
print("-"*100)

with open(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\sample.txt") as f:
    print(f.read())
    f.close()
    
# m = open(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfile.txt","x")
t = open(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfile.txt", "a")
s = input("\nPlease write ur text: ")
t.write(s)
