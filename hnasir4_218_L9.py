#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 9
# Due Date: 11/05/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

from math import sqrt, pow

def counts(xs):
	if xs == [] or xs == "":
		return {}
	list1 = [] #contains all the different values in xs
	list2 = [] #contains the values of the key
	final = {}
	c = xs[0]
	list1.append(c)
	for i in xs:
		if i != c:
			c = i
			list1.append(c)
		continue
	for i in list1:
		if list1.count(i) > 1:
			list1.remove(i)
		continue
	for i in list1:
		count = xs.count(i)
		list2.append(count)
	x = 0
	for i in list1:
		final[i] = list2[x]
		x += 1
	return final

def weeklies(plants_d):
	final = []
	for key, values in plants_d.items():
		if values == 'weekly':
			final.append(key)
		continue
	final.sort()
	return final

def closest(d, what, here):
	what_list = [] #Values
	here_list = [] #Keys
	for key, values in d.items():
		here_list.append(key)
		what_list.append(values)
	if what in what_list:
		short_initial_value = []
		key_initial_value = []
		location = []
		distance = 0
		dict1 = {}
		for i in range(len(what_list)):
			if what == what_list[i]:
				location.append(here_list[i])
			continue
		for i in range(len(location)):
			x2 = location[i][0]
			y2 = location[i][1]
			key_initial_value.append((x2, y2))
			distance = sqrt(pow((x2 - here[0]), 2) + pow((y2 - here[1]), 2))
			short_initial_value.append(distance)
			dict1[location[i]] = distance
		short = short_initial_value[0]
		k = key_initial_value[0]
		for key, values in dict1.items():
			if short > values:
				short = values
				k = key
			continue
		return k
	else:
		return None

def file_counts(filename):
	list1 = []
	file = open(filename)
	x = file.readlines()
	for i in x:
		list1.append(int(i))
	file.close()
	final = counts(list1)
	return final
