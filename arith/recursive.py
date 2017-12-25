
# 递归

# 编写递归函数时，必须告诉它何时停止递归。
# 正因为如此，每个递归函数都有两部分：基线条件（basecase）和递归条件（recursive case）
# 递归条件指的是函数调用自己，而基线条件则指的是函数不再调用自己，从而避免形成无限循环


def countdown(i):
	print(i)
	if i<=1:	# 基线条件
		return
	else:		# 递归条件
		countdown(i-1)

# countdown(10)




# 调用另一个函数时，当前函数暂停并处于未完成状态
# 这个栈用于存储多个函数的变量，被称为调用栈
# 栈有两种操作：压入和弹出。
# 所有函数调用都进入调用栈
# 调用栈可能很长，这将占用大量的内存

def fact(x):
	if x==1:
		return 1
	else:
		return x * fact(x-1)

print(fact(3))















