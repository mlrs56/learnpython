while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Pleade enter a number for your age.')

while True:
	print('Select a new password(letters and numbers only):')
	passwor = input()
	if passwor.isalnum():
		break
	print('Passwords can only have letters and numbers.')