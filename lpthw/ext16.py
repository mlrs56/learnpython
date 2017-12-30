
# 读写文件

from sys import argv

script,filename = argv

print("We're goint to erase ",filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you want that, hit RETURN.")

input("?")
print("Opening the file...")
target = open(filename,'w')
print("Truncating the file. Goodbye!")
target.truncate()


def writeLine(str):
	target.write(str)
	target.write("\n")

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")
writeLine(line1)
writeLine(line2)
writeLine(line3)

print("And finally, we close it.")
target.close()




