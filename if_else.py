ages = input('age:')
age = int(ages)
if age > 18:
	print('adult')
elif age >6:
	print('teenager')
else:
	print('kid')

birth = input('birth:')
year = int(birth)
if year > 2000:
	print('00后')
elif year >= 1990:
	print('90后')

height = input('height:')
weight = input('weight:')
H = int(height)/100
W = int(weight)
bmi = W/(H*H)
print('您的体质指标为%.2f'%bmi)
if bmi <= 18.5:
	print('过轻')
elif bmi <=25:
	print("正常")
elif bmi <=28:
	print("过重")
elif bmi <=32:
	print("肥胖")
else:
	print("严重肥胖")


