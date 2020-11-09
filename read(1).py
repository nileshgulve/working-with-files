#!/usr/bin/python3
def main():
	var1 = open('one.txt',mode = 'r')
	print(dir())
	print(type(var1))
	var1.read()
	var1.close()

if __name__ == '__main__':
	main()

#root@deb1:~/Workingwithfile/readFunction# ./read.py 
#['var1']
#<class '_io.TextIOWrapper'>

