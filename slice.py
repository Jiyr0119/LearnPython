# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])

# r = []
# n =3
# for i in range(n):
#     r.append(L[i])
# print(r)

L = list(range(100))
print(L[::2])

S = ' hello,world, ,'
print(S[:3])

def trim(s):
    try:
        while s[0] == ' ':
               s = s[1:]
        while s[-1] == ' ':
               s = s[:-1]
        return s
    except IndexError:
        return ''


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')