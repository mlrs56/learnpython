
from sys import argv

script,filename = argv

txt = open(filename)

print("Here's your file",filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(filename)

print(txt_again.read())







