
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

def test02(): # file write

	f = open('temp', 'w')
	for i in range(11):
		f.write('writting temp file {}\n'.format(i))

def test03(): # file read

	f = open('temp','r')

	for line in f:
		print(type(line), line, end='')



def test04():
	import json
	tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
	f = open('temp', 'wb')
	str = json.dumps(tel)
	f.write(str)

def test05():
	import json
	f = open('temp','r')
	tel = json.load(f)
	print(type(tel), tel)
	print(tel['guido'])


def test06(): # exceptions

	import sys

	try:
		f = open('temp')
		s = f.readline()
		i = int(s.strip())
	except OSError as err:
		print('os error: {}'.format(err))
	except ValueError:
		print('Could not conver data to an integer')
	except:
		print('Unexpected error:', sys.exc_info()[0])
		raise


	try:
		raise Exception('spam', 'eggs')
	except Exception as inst:
		print('type', type(inst))    # the exception instance
		print('args', inst.args)     # arguments stored in .args
		print('inst', inst)          # __str__ allows args to be printed directly,
		# but may be overridden in exception subclasses
		x, y = inst.args     # unpack args
		print('x =', x)
		print('y =', y)

def this_fails():
	x = 1/ 0


def test07():

	try:
		this_fails()
	except ZeroDivisionError as err:
		print('err.... ', err)


	raise('Hithere')


class MyError(Exception): # user-defined Exception
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def test08():

	try:
		raise MyError(2*2)
	except MyError as e:
		print('My exception occurred, value:', e.value)


	raise MyError('oops!')



def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)



def main():

	scope_test()


	#test08()
	#test07()
	#test06()
	#test05()
	#test04()
	#test03()
	#test02()
	#test01()


if __name__ == '__main__' :
	main()

