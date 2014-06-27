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
	sleep_in(False, False) -> True
	sleep_in(True, False)  -> False
	sleep_in(False, True)  -> True
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

	
def test15(n): # lambda expressions
	return lambda x: x+n

def test16():
	"""
	why don't go away??!?!?

	go run!!
	"""

	a = 1

	# no  __doc__
	"""
	Are u ok?
	"""
	pass


def test17(ham: 42, eggs: int = 'spam') -> "Nothing to see here": 
    #print("Annotations:", test17.__annotations__)
    #print("Arguments:", ham, eggs)
    print(ham, eggs, type(ham), type(eggs))
    print("Annotations:", test17.__annotations__)
    print("Arguments:", ham, eggs)
    #print(ham, eggs, type(ham), type(eggs))


def test18(): # datatype list  functions
    a = [3,2,1]
    print(a.count(3), len(a))    
    #a.append([4,5,6]) # adding item in end of list, orginal type
    print(a)
    a.extend([4,5,6]) # diffent append...
    a.extend('y')
    a.extend('z')    
    a.extend('y')    
    print(a.count(3), len(a))        
    print(a)    
    a.remove('y') # remove first item in list
    print(a)
    print(a.pop())  # get last item and remove that item
    print(a)    
    print('index', a.index('z')) # error if no tiem
    a.remove('z')
    a.sort()
    print('after sort', a) 
    a.reverse()
    print('after revserse', a)     
    b = a.copy() # same b = a 
    print('b', a, b)     
    del a[:]    
    a.clear() # same above  del a[:]
    print(a)


def test19(): # Using list as Queues 
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    print(queue)    
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    print(queue.popleft())                 # The first to arrive now leaves
    print(queue.popleft())                 # The second to arrive now leaves
    print(queue)

def test20():
    a = []
    for x in range(10):
        a.append(x**2)

    b = [x**2 for x in range(10)]
    print(a, b) # equle a, b

    c = list(map(lambda x: x**2, range(10))) # equle a,b
    print(c)


    d = [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y] # wow .. very awsome exp
    print('d :', d)

    e  = []
    for x in [1,2,3]:
        for y in [1,2,3]:
            if x != y:
                e.append((x, y))

    print('e :', e) # equle d


    vec = [-4, -2, 0, 2, 4]

    ved = [x*2 for x in vec]
    print('ved :', ved)

    vee = [x**2 for x in ved if x > 0]
    print('vee :', vee)    

    vef = [(x, x**3) for x in range(10)]
    print('vef :', vef)

    veg = [[1,2,3], [4,5,6], [7,8,9]]
    veh = [num for elem in veg for num in elem]
    print('veg :', veg)    
    print('veh :', veh)

    from math import pi    
    pia = [str(round(pi, i)) for i in range(1, 6)]
    print('pia :', pia)

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    transposed =  []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print('trans... :', transposed)

    ff = [1,2,3,5,65,4,3,3,6,6,34,23,-3]
    del ff[0]
    print('ff :', ff)
    del ff[2:4]
    print('ff :', ff)    
    del ff  # not use the name hereafter

def test21():  # tuples exam

    t = 1,2,3,4,'heelo'
    print(type(t), t[0])

    a, b, c , d, e = t
    print(type(a), type(e))

    u = t,'aa','bb','cc','dd'
    print('u :', u)

    # tuples are not changed ( immutable )

    v = [(1, 2, 3), (1, 2, 3)] # "[]" -> list,   "()" --> tuple
    print(v, type(v))  # list
    print(v[0], type(v[0])) # tuple

    empty = ()
    signleton = 'hello'    , # not trailing comma.. -> make tuple

    print(len(empty), len(signleton), type(empty), type(signleton))

def test22(): # set exam
    
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket) # show that duplicates have been removed

    if 'orange' in basket:
        print('orange in basket is true')

    a = set('12345')
    b = set('45678')
    print('a :', a)                                  # unique letters in a
    print('a-b :', a - b)
    print('a|b :', a | b)
    print('a&b :', a & b)
    print('a^b :', a ^ b)        

def test23(): # dictionary
    tel = {'jack': 1234, 'john': 4567, 'lee': 9500, 'gon': 1209 }
    tel['choi'] = 8066
    print(tel, type(tel))
    del tel['john']
    tel['choi'] = 8067 # can be change
    print(tel)    

    a = sorted(tel.keys())
    print('a :', a, type(a))

    if 'choi' in tel:
        print('tel have choi')

    tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(tel)

    ddb = {x: x**2 for x in range(3,10)}
    print(ddb)


def test24(): # looping techniques
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():  # items
        print(k)

    for i, v in enumerate(['a','bb','ccc']):  # enumerate
        print(i, v)

    questions = ['name', 'quest', 'favorite color']        
    answers = ['lancelot', 'the holy grail', 'blue']    
    for q, a in zip(questions, answers): # zip
        print('what is your {0}? Is is {1}'.format(q, a))

    for i in range(0, 11, 3):
        print(i)

    for i in reversed(range(0, 11, 2)):
        print(i)        

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(basket):
        print(f, end='\t')


def test25():
    str1, str2, str3 = '','aaa','bbbb'
    print(str1, str2, str3)

    # comparing
    if (1, 2, 3)              < (1, 2, 4):
        print('true 1')
    if [1, 2, 3]              < [1, 2, 4]:
        print('true 2')        
    if 'ABC' < 'C' < 'Pascal' < 'Python':
        print('true 3')                
    if (1, 2, 3, 4)           < (1, 2, 4):
        print('true 4')                
    if (1, 2)                 < (1, 2, -1):
        print('true 5')                
    if (1, 2, 3)             == (1.0, 2.0, 3.0):
        print('true 6')                
    if (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4):
        print('true 7')                

def test26(): # module
    import fibo  # lookup file 'fibo.py'
    print(fibo.fib(10))
    print(fibo.fib2(10))    
    print(dir(fibo))

    fibo._ver_ = 2.0

    '''
    print(fibo.__builtins__
        , fibo.__cached__
        , fibo.__doc__        
        , fibo.__file__        
        , fibo.__loader__        
        , fibo.__name__        
        , fibo.__package__        
        , fibo.__spec__
        )
    '''

    print(fibo.__name__,     fibo.__cached__, fibo.__doc__, fibo.__file__, fibo.__loader__, fibo.__package__)
    print(fibo.__spec__, fibo._ver_)

    import builtins

    print(dir(builtins))



def test27(): # module 2
    from fibo import fib, fib2
    print(fib(10))
    print(fib2(10))    


def test28():
    import sys
    #print(dir(sys))
    print(sys.path)

    import baseball.hanwha.jung
    baseball.hanwha.jung.hit()

    import baseball.lotte.park
    baseball.lotte.park.hit()
    baseball.lotte.park.hit()    


def test29():

    import baseball.hanwha.jung
    import baseball.hanwha.lee    
    #from baseball.hanwha import *
    


def main ():

	test29()

	#test28()

	#test27()

	#test26()

	#test25()

	#test24()

	#test23()

	#test22()

	#test21()

	#test20()

	#test19()

	#test18()

	test17('aaaa', eggs='wonderful')

    #test17(43)
	#print(test16.__doc__)

	#f = test15(33)
	#print(f(1), f(3))
	

	#test14('a','bb', 'ccc','dddd','eeeee')

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
