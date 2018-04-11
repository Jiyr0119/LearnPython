# def f1(a,b,c=0,*args,**kw):
#     print("a==",a,"b==",b,"c==",c,"args==",args,"kw==",kw)

# def f2(a,b,c=0,*,d,**kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)

# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}

# f1(*args, **kw)

# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args,**kw)

def product(*num):
    if len(num) == 0:
        raise TypeError('兄弟填个数')
    s = 1
    for n in num:
        if not isinstance(n, (int, float)):
            raise TypeError('让你填数，螺旋爆炸')
        s = s*n
        print(n)
    return s

# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')