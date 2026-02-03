import math

n = int(input())
a = list(map(int,input().split()))
nums = {}
for e in a:
    if e in nums:
        nums[e] += 1
    else: 
        nums[e] = 1
vmax = -1001
for k in nums:
    if (nums[k]>vmax):vmax=nums[k]
print(vmax)