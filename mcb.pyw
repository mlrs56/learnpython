#! python3
# mcb.pwy 保存剪切板  
# Usage:py.exe mcb.pwy save <keyword> - Saves clipboard to key word
# 		py.exe mcb.pwy <keyword> - Loads keyword to clipboard
# 		py.exe mcb.pwy list - Loads all keywords to clipBoard

import shelve,pyperclip,sys
mcbShelf = shelve.open('mcb')

# TODO:Save clipboard content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# TODO:List keywords and load content.
	if sys.argv[1].lower=='list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

