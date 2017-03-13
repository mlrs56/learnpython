def spam():
	eggs = 'spam local'
	print(eggs)

def bacom():
	eggs = 'bacon local'
	print(eggs)
	spam()
	print(eggs)

eggs = 'global'
bacom()
print(eggs)