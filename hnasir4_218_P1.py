#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 1
# Due Date: 09/09/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

#Task 1: Calculate total cost in knuts for the following items

#Defining function to take in the number of hats, telescopes, and canary cream
def checkout(num_hats, num_tels, num_creams):

	#Converting cost of hats, telescopes, and creams into knuts
	hat_total = ((num_hats * 2) * 17) * 29
	tel_total = ((num_tels * 12) *29) + (num_tels * 26)
	cream_total = ((num_creams * 7) * 29)

	#Calculating total cost in knuts and returning the value
	total = hat_total + tel_total + cream_total
	return total


#Task 2: Shows how many minutes there are for a given duration
#Displayed in fortnights, days, hours, and minutes

#Defining function to give total minutes and calculate them into 4 categories
def timing(minutes):

	#using minutes given to calculate how many fortnights there are in that given minute
	#then using the remainder operator to show how many minutes left to do next operation
	total_fortnights = minutes // 20160
	minutes = minutes % 20160
	total_days = minutes // 1440
	minutes = minutes % 1440
	total_hours = minutes // 60
	minutes = minutes % 60
	total_minutes = minutes

	#Returning the final values for fortnights, days, hours, and minutes
	return (total_fortnights, total_days, total_hours, total_minutes)
