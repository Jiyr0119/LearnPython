# LearnPython

# 字符串
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

# 数组
list和tuple是python内置的有序集合，list可变，tuple不可变。

# 判断
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>

# 判断数据类型  
	isinstance(object, classinfo)
	数字分为 int 和 float，暂未发现二者共同的有效父类。可以用 (int, float) tuple 来判断是否为数字（int 或 float）   
	isinstance(3.0, (int, float))    Truez

	字符串，分为 str 和 unicode，二者均继承自 basestring
	isinstance(u'3.0', unicode)
	True
	isinstance('3.0', str)
	True