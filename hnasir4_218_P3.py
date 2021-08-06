#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 3
# Due Date: 10/07/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

#This function is used to calculate the total of the divisors from a given number n
def sum_divisors(n):

	#using a for loop in order to obtain all the positive divisors and add them to the total
	total = 0
	for i in range(n + 1):
		if i == 0:
			continue
		elif (n % i) == 0:
			total = i + total
		else:
			continue
	return total

#This function uses the Leibniz formula, given a value "precision"
#the function calculates the approximation of pi until the improvment of the
#approximation becomes smaller than the precision.
def pi(precision):
	total = 0
	improvement = 4.0
	old_total = 0
	k = 1.0
	increment = 1.0

	#using a while loop in order to make sure the improvment is greater than the
	#precision and then calculating the total
	while improvement >= precision:
		if increment % 2.0 == 0:
			total = old_total - (4.0 / k)
		else:
			total = old_total + (4.0 / k) 
		old_total = total
		k += 2.0
		increment += 1.0
		improvement = (4 / k)
	#using an if else statement to calculate one more iteration based on the increment
	if increment % 2.0 == 0:
		total = old_total - (4.0 / k)
	else: 
		total = old_total + (4.0 / k)
	return total

#This function is used to give the difference of the biggest and smallest value
#in a list
def span(nums):

	#if no value is given then 0 is returned
	if nums == []:
		return 0
	#the max and min values are given the value of the first value in the list
	max = nums[0]
	min = nums[0]
	#using a for loop to assign the max with the biggest value in the list
	for i in nums:
		if i > max:
			max = i
		else:
			continue
	#using a for loop ot assign the min with the smallest value in a list
	for i2 in nums:
		if i2 < min:
			min = i2
		else:
			continue
	return max - min

#This function is used to count and return how many neighboring values
#there are that differ by one
def single_steps(nums):
	x1 = 0
	x2 = 0
	count = 0
	#if the list is empty then 0 is returned
	if nums == []:
		return 0
	#using a for loop in order to determine how many counts there are
	for i in range(len(nums)):
		if i == 0:
			x1 += 1
		elif ((nums[x1] - nums[x2]) == 1) or ((nums[x2] - nums[x1]) == 1):
			count += 1
			x1 += 1
			x2 += 1
		else:
			x1 += 1
			x2 += 1
	return count

#This function is used to remove all the duplicate values next to each other
#or echoes in a list and return a new list wiht only 1 of the values
def remove_echo(xs):
	xs2 = []
	oldi = None
	n = 0
	if xs == "[]":
		return []
	#using a for loop to add only one of the duplicated values onto a new list
	for i in xs:
		xs2.append(i)
		if i == oldi:
			del xs2[-1]
		else:
			oldi = i
	return xs2

#This function is used to gather all even values in a list of list of values
#and return the product
def even_product_2d(grid):
	grid2 = []
	if grid == [[]]:
		return 1
	#Using a for loop in order to obtain all the even values in a list and 
	#add them onto a new list
	for i in grid:
		for x in i:
			if x % 2 == 0:
				grid2.append(x)
			else:
				continue
	total = 1
	#Taking the even values from the new list and multiplying them together
	for i in grid2:
		total *= i
	return total




