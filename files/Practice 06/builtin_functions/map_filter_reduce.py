# Using - map(...)

prices_kzt = [4500, 9000, 13500]
prices_ucd = list(map(lambda x: x / 500, prices_kzt))
print(prices_ucd)


# Using - filter(.....)

nums = [1 , 2, 3 , 4, 5, 6, 7, 8]
primes = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), nums))
print(primes)

# Using - reduce(func, list)

from functools import reduce
nums = [1,2,3,4,5] #1*2=2 -> 2*3=6 -> 6*4=24 -> 24*5=120
product = reduce(lambda x, y: x*y, nums)
print(product)
