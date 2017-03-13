import sys

def collztz(number):
	if number%2==0:
		try:
			number = int(number/2)
			print(number)
			return number
		except ZeroDivisionError:
			print('Error! by zero divilid', ...)
	else:
		number = 3*number +1
		print(number)
		return number

print('Enter number:')
try:
	t1 = int(input())
except ValueError:
	print('Must inut Number')
	t1 = int(input())

while True:
	if t1 == 1:
		sys.exit()
	else :
		t1 = collztz(t1)