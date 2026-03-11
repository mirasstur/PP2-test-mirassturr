import os

current = os.getcwd()
print(f"I m here: -> {current}")

# os.chdir("C:\Users\Miras\Documents\githowto\githowto\files\Practice6\builtin_functions")
# os.mkdir("test_folder")
# os.makedirs("projects/python/scripts", exist_ok=True)

content = os.listdir(".")
print(f"In this folder: {content}")


folder = "Working with folder & files"
if folder not in os.listdir():
    os.mkdir(folder)
    print(f"Folder {folder} created!")
    
os.chdir(folder)
print(f"We are in the: {os.getcwd()}")

os.makedirs("lesso1/homework", exist_ok=True)

os.chdir("..")
print(f"We came back to: {os.getcwd()}")

#----------------------------------------------------------------------------------
print("-"*80)
from pathlib import Path
base_dir = Path("MyProject with pathlib")
#MyProject/data/logs
log_dir = base_dir / "data" / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
print(f"path created!: {log_dir}")

file_path = Path("downloads/report_2024.pdf")
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent)
