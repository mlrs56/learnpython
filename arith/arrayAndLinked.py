

# 链表的每个元素都存储了下一个元素的地址，从而使一系列随机的内存地址串在一起
# 链表的优势在于插入元素方面

# 需要同时读取所有元素时，链表效率很高：你读取第一个元素，根据其中的地址再读取
# 第二个元素，以此类推。但如果你需要跳跃，链表的效率真的很低。

# 在数组中插入元素时，运行时间为O(n)

# 	  | 数组 | 链表
# 读取| O(1) | O(n)
# 插入| O(n) | O(1)
# 删除| O(n) | O(1)

# 链表擅长插入和删除，而数组擅长随机访问


# 用于找出数组中最小元素的函数
def findSmallest(arr):
	smallest = arr[0]	#存储最小的值
	smallest_index = 0	#存储最小元素的索引
	for i in range(1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

# 使用这个函数编写选择排序算法
def selectionSort(arr):		#对数组进行排序
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)	#找出数组中最小元素,并将其加入到新数组中
		newArr.append(arr.pop(smallest))
	return newArr


print(selectionSort([5,3,6,2,10]))




