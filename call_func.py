import math
def my_func(x):
	if not isinstance(x,(int,float)):
		raise TypeError("Fail operand type")
	if x>=0:
		return x
	else:
		return -x

def move(x,y,step,angle=0):
	nx = x+step*math.cos(angle)
	ny = y-step*math.sin(angle)
	return nx,ny

r = move(100,100,60,math.pi/6)
print(r)

def quadratic(a, b, c):
    arg_dict = locals()
    for x in arg_dict:
        if not isinstance(arg_dict[x],(int, float)):
            raise TypeError('Bad operand type')

    delta = b**2 - 4*a*c
    return ( -b + math.sqrt(delta) ) / (2*a), ( -b - math.sqrt(delta) ) / (2*a)
print(quadratic(2,3,1))
print(quadratic(1, 3, -4))