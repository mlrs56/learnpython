#! python3
# pw.py

PASSORDS = {'email': 'F9090', 'blog': 'VmVm', 'luggage': '12345'}
import sys,pyperclip

if len(sys.argv)<2:
	print('Usage: python pw.py [account] 0 copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSORDS:
	pyperclip.copy(PASSORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
print('There is no account named ' + account)