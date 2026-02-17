import sys
input_data = sys.stdin.read().splitlines()
n = int(input())
nums = {}
output = []
for _ in range(n):
    a = input().split()
    com = a[0]
    if com == "set":
        k = a[1]
        v = a[2]
        nums[k] = v
    else:
        k = a[1]
        if k in nums:
            output.append(nums[k])
        else: output.append("KE: no key",k,"found in the document")
sys.stdout.write("\n".join(output))