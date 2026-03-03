import re
text = input()
patt = re.compile(r"[\w]+")
x = re.findall(patt, text)
print(len(x))