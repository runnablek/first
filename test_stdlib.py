
def internetAccess():

	from urllib.request import urlopen
	for line in urlopen('http://www.naver.com'):
		#line = line.decode('utf-8')  # Decoding the binary data to text.
		print(line)


def dateTime():

	from datetime import date
	now = date.today()
	print(now)
	
	a = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
	print(a)


	# dates support calendar arithmetic
	birthday = date(1964, 7, 31)
	age = now - birthday
	print(age.days)






def main():

	dateTime()

	#internetAccess()







if __name__ == "__main__":
	main()