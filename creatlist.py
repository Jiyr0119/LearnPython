import os

arr0 = list(range(1,11))
print(arr0)

L = []
for x in range(1,11):
    L.append(x*x)
print(L)

arr1 = [x*x for x in range(1,11)if x%2 == 0]
print(arr1)

arr2 = [m+n for m in 'ABC' for n in 'XYZ']
print(arr2)

arr3 = [d for d in os.listdir('.')]
print(arr3)

D = {'x':'A','y':'B','z':'C'}
for k,v in D.items():
    print(k,'=',v)

arr4 = [k+'='+v for k,v in D.items()]
print(arr4)

L1 = ['Hello', 'World', 18, 'Apple', None]
arr5 = [s.lower() for s in L1 if isinstance(s,str)]
print(arr5)