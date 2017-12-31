
# copy文件

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from "+from_file + " to " + to_file)


# we could do tese two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
print("The input file is types lone "+str(len(indata)))

print("Does the output file exist?" + str(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")


input()
out_file = open(to_file,'w')
out_file.write(indata)
print("Alright, all done.")

out_file.close()
in_file.close()








