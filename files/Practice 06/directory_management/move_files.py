import shutil
from pathlib import Path

source_file = Path("report_2024.pdf")
# source_file.write_text("Bla Bla bla bla blaa blaaaa bla")
# dest_dir = Path("Archive")

# dest_dir.mkdir(exist_ok=True)
# if source_file.exists():
#     new_loc = shutil.move(str(source_file), str(dest_dir))
#     print(f"File Successfully moved in: {new_loc}")
# else:
#     print("File not found!")
    
if source_file.exists():
    shutil.rmtree(source_file)
else:
    print("File not found!")