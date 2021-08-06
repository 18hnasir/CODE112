#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 2
# Due Date: 09/23/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

#PROJECT TASKS:functions below determine which cell phone plan is best for GMU students based on their info.

#Define a function to determine whether a student obtains a 20% discount on the basic plan
def discount(age, major, is_in_military, gpa):

	#using if else statements to see if the student info. qualifies them for the discount
	if major == "Computer Science" and gpa >= 3.5:
		return True
	elif is_in_military == True or age >= 65:
		return True
	return False

#Define a function used to calculate the total for each plan based on the number of minutes
#and number of texts the students want
def calculate_cost(plan, num_minutes, num_texts):

#Using if else statements for each plan to determine the final cost based on the number of minutes
#and num of texts the user wants and returning the final value
	if plan == "basic":
		if num_minutes > 100 or num_texts > 1000:
			if num_minutes > 100 and num_texts > 1000:
				return (((num_minutes%100)*1.50)+((num_texts%1000)*0.75))+15.0
			elif num_minutes > 100 and num_texts <= 1000:
				return ((num_minutes % 100) * 1.50)+15.0
			elif num_minutes <= 100 and num_texts > 1000:
				return ((num_texts % 1000) * 0.75)+15.0
		return 15.0
			
	elif plan == "standard":
		if num_minutes > 175 or num_texts > 1500:
			if num_minutes > 175 and num_texts > 1500:
				return (((num_minutes%175)*1.25)+((num_texts%1500)*0.50))+20.0
			elif num_minutes > 175 and num_texts <= 1500:
				return ((num_minutes % 175) * 1.25)+20.0
			elif num_minutes <= 175 and num_texts > 1500:
				return ((num_texts % 1500) * 0.50)+20.0
		return 20.0

			
	elif plan == "premium":
		if num_minutes > 250 or num_texts > 2000:
			if num_minutes > 250 and num_texts > 2000:
				return (((num_minutes%250)*1.0)+((num_texts%2000)*0.25))+25.0
			elif num_minutes > 250 and num_texts <= 2000:
				return ((num_minutes % 250) * 1.0)+25.0
			elif num_minutes <= 250 and num_texts > 2000:
				return ((num_texts % 2000) * 0.75)+25.0
		return 25.0

#Define a function to output a plan that is best for the user based on their info.
def cost_efficient_plan(age,major,is_in_military,gpa,num_minutes,num_texts):

	#Calculating cost for each plan based on the number of minutes and texts the user wants
	basic_total = calculate_cost("basic", num_minutes, num_texts)
	standard_total = calculate_cost("standard", num_minutes, num_texts)
	premium_total = calculate_cost("premium", num_minutes, num_texts)

	#Using previous functin to determing if user gets basic discount and then updating 
	#the basic_total value by taking the 20% off
	if discount(age, major, is_in_military, gpa) == True:
		basic_total = basic_total - (basic_total * 0.2)

	#Using if else statements to output which plan is best for them based on the final cost
	if basic_total == standard_total:
		return "standard"
	elif basic_total == premium_total:
		return "premium"
	elif standard_total == premium_total:
		return "premium"
	elif basic_total < 20:
		return "basic"
	elif standard_total < 25:
		return "standard"
	else:
		return "premium"

