import math

#二分查找法实现

def binary_search(list,item):
	low = 0
	high = len(list)-1
	while low<=high:	#只要范围没有缩小到只包含一个元素,就检查中间的元素
		mid = math.floor((low+high)/2)
		guess = list[mid]
		if guess == item:	#找到了元素
			return mid
		if guess > item:	#猜的数字大了
			high = mid - 1
		else:
			low = mid + 1	#猜的数字小了
	return None	#没有指定元素

my_list = [1,3,5,7,9]	#来测试一下

print(binary_search(my_list, 10))	#别忘了索引从0开始,第2个位置的索引为1















