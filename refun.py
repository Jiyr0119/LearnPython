# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)

# print(fact(5))
# print(fact(9))

def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)

print(fact(5))

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)#a上只有1个盘子
    else:#a上有2个盘子
        move(n-1,a,c,b)#把a上的n-1块移动到b
        move(1,a,b,c)#把a上的最后一块移动到c
        move(n-1,b,a,c)#把b上的n-1块移动到c

move(3,'A', 'B', 'C')