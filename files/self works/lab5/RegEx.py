import re 
# txt = ["канат", "крот" , "кукует" , "к-1-т"]
# for word in txt:
#     x = re.findall("^к...т$", word)
#     if x:
#         print(x)

# txt = ["XY-567", "12-999", "A-123", "AB123"]
# for word in txt:
#     x = re.findall(r"\w{2}-\d{3}", word)
#     if x:
#         print(x)"

# txt = ["ID:123", "PO:777", "ID:4"]
# for word in txt:
#     x=re.search(r"ID:(\d+)", word)
#     if x:
#         print(x.group(1))

# txt = "Свяжитесь с нами по номеру 123-456-789 или 999-000-111."

# x = re.sub(r"\d+-\d+-\d+","[REDACTED]", txt)
# print(x)

# txt = "Привет! Как дела? #Python2024$"
# x = re.sub(r"[^A-Za-zА-Яа-я ]+","",txt)
# print(x)

# log_entry = "2026-03-01 12:00:02 [ERROR] Database connection failed"

#  x = re.search(r"(\d{4}-\d{2}-\d{2}).*\[(\w+)\]", log_entry)
#  print(x.group(1))
#  print(x.group(2))

# text = "I love python. PYTHON is great! Python is easy."

# pattern = "python"

# x = re.findall(pattern, text, flags=re.IGNORECASE)
# print(x)

# url = "https://example.com/page1"
# url1 = "http://test.ru/login"

# x = re.search("(?:https?://)([\w.-])", url)
# print(x)

# tags = "python; java,  c++;ruby php"

# x = re.split("[;,\s]+", tags)
# print(x)

login = "Mirasstur228_"

x = re.match(r"^[A-Za-z][\w]{2,9}$", login)
print(x)
