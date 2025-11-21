def count_odd(nums):
    return len([n for n in nums if n % 2 == 1])

res = count_odd([x**2 for x in range(10)])

print(res)