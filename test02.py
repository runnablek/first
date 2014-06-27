
def test01():
	x = 10 * 3.25
	y = 200 * 200
	s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
	print(s)
	print(str(1/7))

	for x in range(12):  # same  "str, repr"
		print(str(x).rjust(3), end='\t')
	print()

	for x in range(12):  
		print(repr(x).rjust(3), end='\t')
	print()		
			
	print('12'.zfill(5))
	print('-3.14'.zfill(7))
	print('3.14159265359'.zfill(5))

	print('This {food} is {adjective}.'.format(food='spam', 
			adjective='absolutely horrible'))

	print('The story of {0}, {1}, and {other}.'.format('Bil	l', 'Manfred',
			other='Georg'))

	import math
	print('The value of PI is approximately {0:.3f}.'.format(math.pi))	

	print('The value of PI is approximately {}.'.format(math.pi))
	# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) 
	# can be used to convert the value before it is formatted:
	print('The value of PI is approximately {!r}.'.format(math.pi))	

	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
	for name, phone in table.items():
		 print('{0:10} ==> {1:10d}'.format(name, phone))

	table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
	print('{1} Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
	      'Dcab: {0[Dcab]:d}'.format(table, 'test str'))

	print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

def test02(): # file open.... write by json type



	f = open('temp', 'w')

	for i in range(11):
		f.write('writting temp file {}\n'.format(i))

	#import json

	#a = [1, 'simple', 'list']
	#json.dumps(a,f)


def main():

	test02()
	#test01()

	
	




if __name__ == '__main__' :
	main()

