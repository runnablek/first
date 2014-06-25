# -*- coding: UTF-8 -*-

def test01():
	flag = True
	if flag :
		print ("flag is {}".format(flag))
	else :
		print ("flag is false!!")

	nn = 15

	if x < 0:
		print('negative number')
	elif x == 0:
		print('zero')
	elif x < 10:
		print('under ten')
	else:
		print('bigger than ten')
	



def test02():


	import sys	
	''' comment...
	'''
	print(sys.platform + " Hello world!!")

	import os	
	filename = os.environ.get('PYTHONSTARTUP')
	print("file name is {}".format(filename))


def test03():
	a = 3
	b = 2
	print ("test.. 03", a, b, a+b)


def test04():
	for i in ['aa','bb','cc','dd']:
		print (i, end='\t')
		print ('')


def test05(talk):
	print (talk)
	return True


def test06():
	print(17/3)
	print(17//3)
	print(17%3)
	print(2+3*5)
	print(5**2)
	print(2**7)
	print(3 * 3.3 - 1)
	print(3 * 'sorry' + ' sorry...')
	print('Py' 'thon')
	#       01234567890
	word = 'Python very easy'
	print (word[0], word[1], word[-2])
	print (word[1:8])
	print (word[:2])
	print (word[7:])	
	# word[0] = 'J'  not support
	# string is immutable, but lists are a mutable type.
	word2 = 'J' + word[1:]
	print(word2)
	print(len(word2))


def test07():   # list example

	sort_numbers = [8,4,2,1,8,16,32]
	print(sort_numbers)
	print(sort_numbers[0])
	print(sort_numbers[3:])	
	sort_numbers += [64,128,256]
	print(sort_numbers)

	sort_numbers.append(512)
	sort_numbers.append(1024)	
	sort_numbers.append(sort_numbers[-1] * 2)
	sort_numbers.sort()	
	print(sort_numbers)	

	print(type(sort_numbers))
	#           0   1   2   3   4   5   6
	letters = ['a','b','c','d','f','g','h']
	print(type(letters))
	print(letters)
	letters[2:5] = ['C','D','F']
	print(letters)

	#nested lists

	mixed_str = [sort_numbers, letters]


	print(mixed_str)
	print(mixed_str[0][3])

def test08():
	a, b = 0, 1;
	while b < 10:
		print(b, end='\t')
		a, b = b , a+b
	print()

def sleep_in(weekday, vacation):
	'''
	The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
	We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 

	sleep_in(False, False) ¡æ True
	sleep_in(True, False) ¡æ False
	sleep_in(False, True) ¡æ True		
	'''

	if weekday == False or vacation == True:
		return True
	else:
		return False

def array_count9(nums):
	cnt = 0
	for cha in nums:
		if cha == 9:
			cnt += 1
	return cnt


def hello_name(name):
	print('Hello '+ name + '!')

	
def lucky_sum(a,b,c):
	lsum = [a,b,c]
	sum = 0;
	for a in lsum:
		if a != 13:
			sum += a
		else:
			break
	return sum

def test09():
	words = ['cat', 'dog', 'lion', 'turtle']
	for w in words:
		print(w, len(w))

	words.insert(1, '  flower  ')

	for w in words[:]:
		print(w, len(w))	

def test10(): # range 
	for i in range (5,10):
		print(i)

	print(list(range(10)))		


def test11():

	for i in range(1,11):

		if i % 2 == 0:
			if i > 5:
				print('mod 2 is zero and bigger than 5')
		else:
			print ('mod 2 is not zero', i)


def test12(a, b=3, c='aaaa'):
	print("Reading parameters A value")
	if a in ('y','Y','yes','YES'):
		print('You choice YES', a, b, c)			
	else:
		print('You choice NO')

def test13(a,b): # double return value
	return a**2, b**b


def cheeseshop(kind, *arguments, **keywords):
	print(type(kind), kind)
	print(type(arguments), arguments)
	print(type(keywords), keywords)

	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	keys = keywords.keys()
	for kw in keys:
		print(kw, ":", keywords[kw])	
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ":", keywords[kw])

def test14(a, b, *cc):
	print(a, b)
	print(type(a), type(b), type(cc))

	cc.ins


def main ():

	test14('a','bb', 'ccc','dddd','eeeee')

	#test01()
	#test02()
	#test03()
	#test04()
	#test05('i call function number 05')
	#test06()
	#test07()
	#test08()
	#print(sleep_in(False, False))
	#print(sleep_in(True, False))
	#print(sleep_in(False, True))
	#print(lucky_sum(1,13,3))
	#test09()
	#test10()
	#test11()
	#test12('yes', c='bbbbbb')

	#a,b = test13(4,4)
	#print(a, b)
	'''
	cheeseshop("Limburger",
	           "It's very runny, sir.",
	           "It's really very, VERY runny, sir.",
	           shopkeeper="Michael Palin",
	           client="John Cleese",
	           sketch="Cheese Shop Sketch")
	'''


if __name__ == '__main__' :
	main()
