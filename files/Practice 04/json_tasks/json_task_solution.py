import json

with open("sample_data.json", "r") as f:
    a = json.load(f)
print("Interface Status")
print("="* 100)
print(f"{'DN':<50}{'Description':<30}{'Speed':<10}{'MTU':<10}")
print("-"* 45,"-"* 30,"-"* 10,"-"* 10 )
for x in a["imdata"]:
    if "description" in x["l1PhysIf"]["attributes"]:
        print(f"{str(x["l1PhysIf"]["attributes"]["dn"]):<50}{str(x["l1PhysIf"]["attributes"]["description"]):<30}{str(x["l1PhysIf"]["attributes"]["speed"]):<10}{str(x["l1PhysIf"]["attributes"]["mtu"]):<10}")
    else:
        print(f"{str(x["l1PhysIf"]["attributes"]["dn"]):<50}{' ':<30}{str(x["l1PhysIf"]["attributes"]["speed"]):<10}{str(x["l1PhysIf"]["attributes"]["mtu"]):<10}")
