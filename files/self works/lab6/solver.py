n = int(input())
nums = list(map(int,input().split()))
truthy = sum(bool(e) for e in nums)
print(truthy)
