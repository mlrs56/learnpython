
# 字符串
name = 'Zophie'
for i in name:
	print('***' + i + '***')


# 元组
eggs = ('hello', 42, 0.5)
for i in eggs:
	print('***' + str(i) + '***')


# 用list()和tuple()函数转换类型
t1 = tuple(['cat', 'dog', 5])
t2 = list(('cat', 'dog', 5))
t3 = list('hello')
print(t1)
print(t2)
print(t3)
