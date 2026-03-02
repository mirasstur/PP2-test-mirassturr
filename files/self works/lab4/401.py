# def ans(a,b):
#     for i in range(a, b+1):
#         yield i*i

# a,b = map(int,input().split())

    # first = True
    # for e in ans(n):
    #     if first:
    #         print(e, end="")
    #         first = False
    #     else:
    #         print(",", e, sep="", end="")

# import math

# def ans(n,r):
#     for i in range(r):
#         yield n
        
# n = input()
# r = int(input())
# for e in ans(n,r):
#     print(e,end=" ")

# import json

# def apply_patch(source, patch):
#     for key, value in patch.items():
#         if value is None:
#             if key in source:
#                 del source[key]
#         elif isinstance(value, dict) and isinstance(source.get(key), dict):
           
#             source[key] = apply_patch(source.get(key, {}), value)
#         else:
            
#             source[key] = value
#     return source


# source = json.loads(input().strip())
# patch = json.loads(input().strip())

# result = apply_patch(source, patch)
# print(json.dumps(result, sort_keys=True, separators=(',', ':')))


# import json
# def srz(val):
#     return json.dumps(val, separators=(',',':'))

# ans = {}

# def drs(first, second, path=""):
#     dfs=[]
#     if isinstance(first, dict) and isinstance(second, dict):
#         keys = set(first.keys()) | set(second.keys())
#         for key in keys:
#             new_path = f"{path}.{key}" if path else key
#             if key not in first:
#                 dfs.append(f"{new_path} : <missing> -> {srz(second[key])}")
#             elif key not in second:
#                 dfs.append(f"{new_path} : {srz(first[key])} -> <missing>")
#             else:
#                 dfs.extend(drs(first[key], second[key], new_path))
#     else:
#         if first != second:
#             dfs.append(f"{path} : {srz(first)} -> {srz(second)}")
#     return dfs

# A = json.loads(input().strip())
# B = json.loads(input().strip())

# diffs = drs(A,B)
# if diffs:
#     for line in sorted(diffs):
#         print(line)
# else:
#     print("No differences")
                
                
# import json
# import re
# def find_value(data, pt):
#     parts = pt.split(".")
#     curr = data
#     try:
#         for part in parts:
#             key_match = re.match(r"([^\[]+)", part)
#             if not key_match:
#                 return "NOT_FOUND"
#             key = key_match.group(1)
#             curr = curr[key]
#             indices = re.findall(r"\[(\d+)\]", part)
#             for idx in indices:
#                 curr = curr[int(idx)]
#     except(KeyError, AttributeError, IndexError, TypeError):
#         return "NOT_FOUND"
#     return json.dumps(curr, separators=(',',':'), ensure_ascii=False)

# A = json.loads(input().strip())
# q = int(input())
# for i in range(q):
#     s = input()
#     print(find_value(A,s))
    
    
    
    