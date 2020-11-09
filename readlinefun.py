#!/usr/bin/python3

import sys
def print_file(filename):
	f = open(filename)
	print("The data type of variable 'f' is ",type(f))
	print("=" *50)
	lines = f.readlines()
	print("The data type of 'lines' is",type(lines))
	print("* "*50)
	print(lines)
	print("#" *50)
	for line in lines:
		print(line,end='')
		print(type(line))
	f.close()

def main():
	print_file(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/Workingwithfile/readFunction# ./readlinefun.py two.txt 
# The data type of variable 'f' is  <class '_io.TextIOWrapper'>
# ==================================================
# The data type of 'lines' is <class 'list'>
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
# ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', '\n']
##################################################
# Line 1
# <class 'str'>
# Line 2
# <class 'str'>
# Line 3
# <class 'str'>
# Line 4
# <class 'str'>

<class 'str'>



