#!/usr/bin/python3

import sys

def write(filename):
	f = open(filename,'w')
	for val in range(5):
		f.write(str(val) + '\n')
	f.close()
	print('file opwration over')

def main():
	write(sys.argv[1])
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/Workingwithfile/readFunction# ./write.py one.txt 
# file opwration over
# root@deb1:~/Workingwithfile/readFunction# cat one.txt 
# 0
# 1
# 2
# 3
# 4

