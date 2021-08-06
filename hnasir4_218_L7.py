#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 7
# Due Date: 10/22/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def rank3(x, y, z, ascending = True):
	list1 = [x, y, z]
	list2 = []

	big = max(list1)
	small = min(list1) 

	list2.extend((big,small))

	list1.remove(big)
	list1.remove(small)

	middle = list1[0]
	if ascending == True:
		return((small, middle, big))
	else:
		return((big, middle, small))

def remove(val, xs, limit = None):
	if (limit == None) or (limit > len(xs)):
		for i in range(5):
			for i in xs:
				if i == val:
					xs.remove(val)
				continue
	else:
		times = 0
		while limit > times:
			xs.remove(val)
			times += 1
	return None

def filter_chars(msg, keeps = None):
	list1 = []
	xs = msg
	if keeps != None: 
		for i in msg:
			if i in keeps:
				list1.append(i)
			else:
				continue
	else:
		for i in msg:
			if (i.isupper() == True) or (i.islower() == True):
				list1.append(i)
			else:
				continue
	return "".join(list1)

def relocate_evens(data, new_home = []):
	if new_home == []:
		new_home = []
		for i in data:
			if i % 2 == 0:
				new_home.append(i)
			continue
		for i in new_home:
			if i in data:
				data.remove(i)
			continue
	else:
		for i in data:
			if i % 2 == 0:
				new_home.append(i)
			continue
		for i in new_home:
			if i in data:
				data.remove(i)
			continue
	return new_home








		