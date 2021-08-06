#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 5
# Due Date: 10/01/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

#Function 1: is used to find the index of the key
def location(xs,key):
	#use a loop to locate the index of the key given and update the index value and return the final value
	index = 0
	for number in xs:
		if number == key:
			return index
		index += 1

#Function 2: is used to find the value of the fibonci number given the index number
def fibonacci(n):
	#use a loop to update fib_total and add it to the old_total giving the fibannci number
	#and return the final value back to the function
	old_total = 0
	x = 0
	for i in range(n + 1):
		if i == 0:
			fib_total = 1
			continue
		fib_total = old_total + fib_total
		old_total = fib_total - old_total
	return fib_total

#Function 3: function is used to obtain the largest integer whose square isn't bigger than n
def int_sqrt(n):
	#use a loop to find the integer squared that is less than n and returning the final value
	for i in range(n + 1):
		if (i * i) < n:
			continue
		else:
			if (i * i) > n:
				return i - 1
			return i

#Function 4: function is used to find the sum of all the even integers in a 2 dimensional list
def sum_evens_2d(xss):
	#Creating a list called total to place all even integers into the list
	total = 0
	
	#use a loop to obtain all even integers from the 2 dimensional list and then return the sum
	for i in xss:
		n2 = 0
		for x in i:
			if i[n2] % 2 == 0:
				total = i[n2] + total
				if len(i) > n2:
					n2 += 1
					continue
			elif len(i) > n2:
				n2 += 1
				continue
			else:
				break
	return total


