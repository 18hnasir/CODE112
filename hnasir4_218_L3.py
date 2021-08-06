#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 3
# Due Date: 09/17/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

# TASK 0 (example)

# EXAMPLE: this function is implemented for you, to show 
# what a function definition looks like, and how the
# 'student' added four lines to complete the definition.

def is_even(n):
	# at the end, we'll return whatever current value
	# that's in ans as our return value. Somewhere in 
	# this function, you should re-assign it to be
	# either True or to False.
	ans = None
	
	# make decisions with if-else structures to determine
	# whether n is even (divisible by two) or not. Then,
	# set ans to equal True or equal False as your answer.
	
	# YOUR CODE GOES HERE. (Since it's an example, we've
	# already written "your code" - four lines).
	
	if n % 2 == 0 :
		ans = True
	else:
		ans = False
	
	# make this the last line of your function definition
	return ans


#Task 2: Function is used to determine what letter grade is received with a given value

#Define a function that takes in a score an integer and outputs in the letter grade with that score. 
def letter_grade(score):

	#Using a nested if statement to determine what grade category the score fits into and returning it
	if score >= 98:
		return "A+"
	elif score >= 92:
		return "A"
	elif score >= 90:
		return "A-"
	elif score >= 88: 
		return "B+"
	elif score >= 82:
		return "B"
	elif score >= 80:
		return "B-"
	elif score >= 78:
		return "C+"
	elif score >= 72:
		return "C"
	elif score >= 70:
		return "C-"
	elif score >= 60:
		return "D"
	elif score < 60:
		return "F"

#Task 3: Function is used to take the two biggest values out of a given three and add them.

#Defining a function that takes in 3 values and adds the two biggest out of the 3
def sum2biggest(a, b, c):

	#using nested if statements in order to determine the 2 largest values and returing sum.
	if a >= b >= c:
		sum = a + b
		return sum
	elif a >= b <= c:
		sum = a + c
		return sum
	elif b >= a <= c: 
		sum = b + c
		return sum
	elif b >= a >= c:
		sum = a + b
		return sum

