# -*- coding: utf-8 -*-

# names = ["michael","bob","tracy"]
# for name in names:
# 	print("hello,"+name)

# sum = 0
# for x in range(101):
# 	sum = sum+x
# print(sum)

# arr = list(range(10))
# print(arr)

# sum = 0
# n = 99
# while n > 0:
# 	sum = sum+n
# 	n = n-2
# print(sum)

# do while

# n = 1 
# while n<=100:
# 	print(n)
# 	n =n+1
# print("end")

# n = 1
# while n<=100:
# 	if n > 10:
# 		break
# 	print(n)
# 	n = n+1
# print('end')

# continue
n = 0
while n<10:
	n = n+1
	print(n)

n = 0
while n<10:
	n = n+1
	if n % 2 == 0:
		continue
	print(n)