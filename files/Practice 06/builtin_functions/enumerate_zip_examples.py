# Using - zip(list1, list2)

names = ["Miras", "Aidyn", "Ermek", "Jan"]
orders = ["Capuccino", "Latte", "Raff"]

pairs = list(zip(names, orders))
print(pairs)

# Using - enumurate() --> 
# return pair(index, value)

for id, name in enumerate(names):
    print(f"{id}: {name}")
    
for id, name in enumerate(orders, start=1):
    print(f"Order |{id}|: {name}")

