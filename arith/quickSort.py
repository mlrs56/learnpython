
# 快速排序

# 递推法
def sum1(arr):
	total = 0
	for x in arr:
		total += x
	return total

print(sum1([1,2,3,4]))


# 递归法
# list[1:] 从第二个元素开始截取列表
def sum2(list):
	if list == []:
		return 0
	return list[0] + sum2(list[1:])

print(sum2([1,2,3,4,9,0]))



# 递归计算列表包含的元素数
def count(list):
	if list == []:
		return 0
	return 1 + count(list[1:])


print(count([1,2,3,4,9,0]))



def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))







