import os
# os.remove(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfile.txt")

if os.path.exists(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfile.txt"):
    os.remove(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfile.txt")
else:print("No such file found")

if os.path.exists(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfold"):
    os.rmdir(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice6\file_handling\myfold")
else:print("No such folder found")