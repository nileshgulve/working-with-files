#!/usr/bin/python3
# Read function, read the entire file into one string
import sys,binascii
def print_file(filename):
	f = open(filename,mode='rb')
	content = f.read()
	print("The data type of variable 'content' is:",type(content))
	print("The length of variable 'content' is:",len(content))
	print("=" *50)
	print("%s" %content)
	print("* "*50)
	print("Printing the hex value: ")
	print("%s"%(binascii.hexlify(content)))
	print("#" *50)
	f.close()

def main():
	print_file(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# oot@deb1:~/Workingwithfile/readFunction# ./read-with-binary-mode.py one.txt 
# The data type of variable 'content' is: <class 'bytes'>
# The length of variable 'content' is: 4
#==================================================
# b'abc\n'
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#P rinting the hex value: 
# b'6162630a'
##################################################

