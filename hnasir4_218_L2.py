#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 2
# Due Date: 09/10/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
 
def add3(x, y, z):
	# at the end, we'll return whatever current value
	# that's in ans as our return value. It's often
	# useful to create the variable with a starting 
	# value and then update it later on with reassignments
	# as needed.
	ans = 0
	
	# make decisions and perform calculations using all the 
	# coding tricks you've learned so far. Since we're
	# writing a function, all our code is indented inside
	# the function to the same amount.
	
	# YOUR CODE GOES HERE. (Since it's an example, we've
	# already written "your code" - four lines).
	
	ans = x + y + z
		
	# make this the last line of your function definition,
	# so that the function sends whatever value ans has
	# as the output.
	return ans

#TASK 1:Function is used to calculate the total inches there are in the given feet and inches

#Defining function to take in value of total feet and inches 
def inch_height(num_feet, num_inches):

	#Calculating total inches and returning the total
	total = num_feet * 12 + num_inches
	return total


#Task 2:Function is used to calculate the total cost for a gas fillup

#Defining function to take in value for the price per gallon and number of gallons
def gas_cost(price_per_gallon, num_gallons):

	#Calculating the total cost and returning the value
	total_gas = price_per_gallon * num_gallons
	return total_gas

	
