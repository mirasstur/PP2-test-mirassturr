import re
output_path = r"C:\Users\Miras\Documents\githowto\githowto\files\Practice 05\output.txt"

outputer = ""

with open(r"C:\Users\Miras\Documents\githowto\githowto\files\Practice 05\raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
    total_amount = 0
    x = re.findall(r"Стоимость\s*\n\s*([\d, ]+)",text,flags=re.MULTILINE)
    # print("_"*100)
    # print("Prices of Products")
    
    outputer += ("_"*100) + "\n"
    outputer += ("Prices of Products\n")
    
    
    for p in x:
        # print(p) # all prices
        outputer += str(p) + "\n"
    x = re.findall(r"\d+\.\n(.+)",text,flags=re.MULTILINE)
    # print("-"*100)
    # print("---------Names of products----------")
    
    outputer += ("-"*100) + "\n"
    outputer += "---------Names of products----------" + "\n"
    
    for n in x:
        outputer += str(n) + "\n"
    x = re.findall(r"Стоимость\s*\n\s*([\d ]+)",text,flags=re.MULTILINE)
    for p in x:
        # print(p)
        th = p.split()
        if len(th) > 1:
            total_amount+=int(th[0])*1000 + int(th[1])
        else: total_amount+=int(th[0])
    x = re.findall(r"ИТОГО:\s*\n\s*([\d ]+)", text, flags=re.MULTILINE)
    # print("ИТОГО: ", x)
    # print("-"*100)
    # print("Total amount = ",f"{total_amount:.2f} тг")
    outputer += ("-"*100) + "\n"
    outputer += "Total amout = " + str(f"{total_amount:.2f} тг") + "\n"
    
    
    x = re.findall(r"Время:\s*(\d+.\d+.\d+ \d+:\d+:\d+)",text,flags=re.MULTILINE)
    for tm in x:
        # print("Date and Time: ",tm)
        outputer += "Date and Time: " + tm + "\n"
    x = re.findall(r"Оператор фискальных данных:\s*([^d]{16})",text,flags=re.MULTILINE)
    for pay in x:
        # print("Payment method: ",pay)
        outputer += "Payment method: " + pay + "\n"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(outputer)
    
    
