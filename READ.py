#!/usr/bin/python3

import sys
def print_file(filename):
	f = open(filename)
	print("The data type of variable 'f' is ",type(f))
	print('='*50)
	for line in f:
		print(line,end='')
		print("The data type of 'line' is",type(line))
	f.close()

def main():
	print_file(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/Workingwithfile/readFunction# ./READ.py two.txt 
# The data type of variable 'f' is  <class '_io.TextIOWrapper'>
# ==================================================
# Line 1
# The data type of 'line' is <class 'str'>
# Line 2
# The data type of 'line' is <class 'str'>
# Line 3
# The data type of 'line' is <class 'str'>
# Line 4
# The data type of 'line' is <class 'str'>

# The data type of 'line' is <class 'str'>

