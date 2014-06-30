class MyClass:
	""" A simple example class """
	i = 12345

	def __init__(self):
		self.data = []

	def f(self):
		return 'hello world'



class Complex:
	def __init__(self, realpart = 1, imagpart = 2):
		self.r = realpart
		self.i = imagpart

	
def test01():
	x = MyClass()
	print(type(x), x, type(x.f), x.i)
	y = Complex(3.0, -4.5)
	print(y, type(y), y.r, y.i)
	z = Complex()


def test02():
	x = MyClass()
	x.counter = 1
	while x.counter < 10:
	    x.counter = x.counter * 2
	print(x.counter)
	del x.counter

def test03():

	x = MyClass()
	y = MyClass()
	x.cnt = 5
	x.cnt = x.cnt ** 2
	print(x.cnt)
	print(type(x), type(x.cnt))

	
	y.cnt = 10 * 3
	print(y.cnt)
	print(x.cnt, y.cnt)

	del x.cnt, y.cnt
	
def test04(): # Method Object

	x = MyClass()
	xf = x.f
	print(xf())


class Dog:

    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)


def test05():

	d = Dog('Fido')
	e = Dog('Buddy')

	d.add_trick('roll over')
	e.add_trick('play dead')

	print(d.tricks)





class Bag: # Methods may call other methods by using method attributes of the self argument:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)


class Pack(Bag): # Inheritance, override mthod

	def add(self, x):
		self.data.append(x**2)

	def prit(self):
		print(self.data)



class WhatSome(Dog, Pack): # Multiple Inheritance

	def wow(self):
		self.w = 1111



def test06():

	p = Pack()
	p.add(2)
	p.add(3)
	p.addtwice(4)
	p.prit()


	w = WhatSome('curt')



class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


class Employee:
    pass


def test07():

	john = Employee() # Create an empty employee record

	# Fill the fields of the record
	john.name = 'John Doe'
	john.dept = 'computer lab'
	john.salary = 1000

	print(dir(john))


class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass


def test08():


	for cls in [B, C, D]:
	    try:
	        raise cls()
	    except D:
	        print("D")
	    except C:
	        print("C")
	    except B:
	        print("B")


def test09(): # iterators

	for element in [1, 2, 3]:
	    print(element)
	for element in (1, 2, 3):
	    print(element)
	for key in {'one':1, 'two':2}:
	    print(key)
	for char in "123":
	    print(char)

	s = 'abc'
	it = iter(s)
	print(it)
	print(next(it))
	print(next(it))
	print(next(it))
	print(dir(it))



class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def test10():

	rev = Reverse('spam')
	print(iter(rev))

	for char in rev:
		print(char)

def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]


def test11():

	for c in reverse('golf'):
		print(c)


def test12():

	a = sum(i*i for i in range(10))   
	print(a)
	xvec = [10, 20, 30]
	yvec = [7, 5, 3]

	b = sum(x*y for x,y in zip(xvec, yvec))
	print(b)


	from math import pi, sin
	sine_table = { x: sin(x*pi/180) for x in range(0,91)}
	print(sine_table, type(sine_table))
	
	

	data = 'golf'
	dd = list(data[i] for i in range(len(data)-1, -1, -1))

	print(dd, type(dd))


def main():

	test12()
	#test11()


	#test10()
	#test09()
	#test08()
	#test07()
	#test06()
	#test05()
	#test04()
	#test03()
	#test02()
	#test01()


	




if __name__ == '__main__':
	
	main()

