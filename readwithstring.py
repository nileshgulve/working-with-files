#!/usr/bin/python3
# Read function, read the entire file into one string
import sys
def print_file(filename):
	f = open(filename)
	print("The data type of variable 'f' is ",type(f))
	print("=" *50)
	string = f.read()
	print("The data type of 'string' is",type(string))
	print("* "*50)
	print(repr(string))
	print("#" *50)
	print(string)
	f.close()

def main():
	print_file(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/Workingwithfile/readFunction# ./readwithstring.py two.txt 
# The data type of variable 'f' is  <class '_io.TextIOWrapper'>
# ==================================================
# The data type of 'string' is <class 'str'>
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
# 'Line 1\nLine 2\nLine 3\nLine 4\n\n'
##################################################
# Line 1
# Line 2
# Line 3
# Line 4


