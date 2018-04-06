def power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s

print(power(2,6))

def enroll(name,gender,age=6,city='BeiJing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('Jonathan','man',city='Shanxi')

def add_end(L=[]):
	L.append('end')
	return L

# print(add_end([1,2,3]))
def add_end0(L= None):
	if L is None:
		L = []
	L.append('end')
	return L
# print(add_end())
# print(add_end())
# print(add_end())

# print(add_end0())
# print(add_end0())

def calc(*numbers):
	sum = 0
	for n in numbers:
		# print(n)
		# print(sum)
		sum += n*n
	return sum

num = [1,2,3]
print(calc(*num))

extra = {'city'}
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name',name,'age',age,'other',kw)

person('jonathon',18)
person('Adam', 45, gender='M', job='Engineer')
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)