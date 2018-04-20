def test():
	n=0
	i=[1]
	while n<10:
		n = n + 1
		yield i
		a = [0] + i
		b = i + [0]
		i = [a[c] + b[c] for c in range(0,len(a))]

data = test()
print(next(data))
for i in data:
	print(i)

# a = [1,2,3,4,5,6,7,8,9]
#
# b = [2,3,4,5,6,7,8,9,10]
#
# c = [a[i] + b[j] for i in range(0,len(a)) for j in range(0,len(b))]
#
# print(c)