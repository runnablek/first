# -*- coding: UTF-8 -*-




def main ():

	import sys	
	''' comment...
	'''

	print(sys.platform + " Hello world!!")


def test01():


	flag = True
	if flag :
		print ("flag is {}".format(flag))



def test02():

	import os	
	filename = os.environ.get('PYTHONSTARTUP')
	print("file name is {}".format(filename))




if __name__ == '__main__' :
	main()
	test01()
	test02()

