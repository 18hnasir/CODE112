#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 4
# Due Date: 10/28/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def show(map): #format string in a specific way
	list1 = []
	s = ""
	large = map[0][0]
	for i in map:
		for k in i:
			if k > large:
				large = k
	if large >= 100:  #depending on the largest value, the amount of spaces will differ
		for i in range(len(map)):
			c = 0
			for k in map[i]:
				if k == map[i][0] and c == 0:
					if k >= 10:
						s += " " + str(k)
					else:
						s += "  " + str(k)
					c += 1
				else:
					if k >= 100:
						s += " " + str(k)
					else:
						s += "   " + str(k)
			s += "\n"
		return s
	elif large >= 10:
		for i in range(len(map)):
			c = 0
			for k in map[i]:
				if k == map[i][0] and c == 0:
					s += " " + str(k)
					c += 1
				else:
					if k >= 10:
						s += " " + str(k)
					else:
						s += "  " + str(k)
			s += "\n"
		return s
	else:
		for i in range(len(map)):
			c = 0
			for k in map[i]:
				if k == map[i][0] and c == 0:
					s += str(k)
					c += 1
				else:
					s += " " + str(k)
			s += "\n"
		return s
def highest_point(map):
	high = map[0][0]
	position1 = 0
	row = 0
	column = 0
	constant = map[0]
	ck = 0 #used to determine whether the list is the same as the last
	for i in map:
		if constant == i and 0 in i:
			ck += 1
		else:
			break
	if ck > 1:
		return None

	for i in range(len(map)):
		position2 = 0
		for k in map[i]:
			if k > high:
				high = k
				row = position1
				column = position2
			position2 += 1
		position1 += 1
	return (row, column)

def on_map(map, r, c): #make sure that position is on the map
	if r < 0 or c < 0: #make sure the postion does not contain a negative value
		return False
	if len(map) > r: 
		h = 0
		for i in range(len(map)):
			if len(map[i]) > c:
				h += 1
			else:
				continue
		if h == 0:
			return False
		else:
			return True
	else:
		return False

def is_map(map):
	if map == []:
		return False
	#test 1: are all values non negatives and are ints, not strings or bools
	for i in map:
		for k in i:
			if type(k) == str or type(k) == bool:
				return False
			elif type(k) == float or k < 0:
				return False
			continue
	#test 2: has at least on row and one column and is same lenght as others
	for i in map:
		if len(i) > 1:
			continue
		else:
			return False
	for i in map:
		l = len(map[0])
		if len(i) == l:
			continue
		else:
			return False
	return True

def neighbors(map, r, c): #get locations around the postion given
	if on_map(map, r, c) == True:
		xs = []
		if r == 0 or r == (len(map) - 1):
			if r == 0:
				for i in range(len(map[r])):
					if i <= (c + 1) and i >= (c - 1):
						xs.append((r, i))
					else:
						continue
				for i in range(len(map[r])):
					if i <= (c + 1) and i >= (c - 1):
						xs.append((r + 1, i))
					else:
						continue
			else:
				for i in range(len(map[r])):
					if i <= (c + 1) and i >= (c - 1):
						xs.append((r - 1, i))
					else:
						continue
				for i in range(len(map[r])):
					if i <= (c + 1) and i >= (c - 1):
						xs.append((r, i))
					else:
						continue
		else:
			for i in range(len(map[r])):
				if i <= (c + 1) and i >= (c - 1):
					xs.append((r - 1, i))
				else:
					continue
			for i in range(len(map[r])):
				if i <= (c + 1) and i >= (c - 1):
					xs.append((r, i))
				else:
					continue
			for i in range(len(map[r])):
				if i <= (c + 1) and i >= (c - 1):
					xs.append((r + 1, i))
				else:
					continue
	else:
		return []

	xs.remove((r,c))
	return xs

def water_adjacent(map, r, c):
	k = ()
	if on_map(map, r, c) == True:
		for i in neighbors(map, r, c):
			k = i #to acquire each tuple value
			p1 = k[0] #set position 1 to index 0 in tuple
			p2 = k[1] #set position 2 to index 1 in tuple
			if map[p1][p2] == 0: #if the neighbor values are water then return True
				return True
			continue
		return False
	else:
		return False

def count_coastline(map):
	count = 0 
	for i in range(len(map)):
		for k in range(len(map[i])):
			x = map[i][k]
			if x > 0:
				if water_adjacent(map, i , k) == True:
					count += 1
				else:
					continue
			else:
				continue
	return count

def on_ridge(map, r, c):
	if on_map(map, r, c) == True:
		x = map[r][c]
		#checking to see if it is a ridge by values next to each other
		if map[r][c - 1] < x and map[r][c + 1] < x:
			return True
		#checking up and down
		elif map[r - 1][c] < x and map[r + 1][c] < x:
			return True
		#checking diagonal slope down
		elif map[r - 1][c - 1] < x and map[r + 1][c + 1] < x:
			return True
		#checking diagonal slope up
		elif map[r - 1][c + 1] < x and map[r + 1][c - 1] < x:
			return True
		else:
			return False
	else:
		return False

def is_peak(map, r , c):
	h = 0 #determines if all tuples pass the test
	if on_map(map, r, c) == True:
		x = map[r][c]
		for i in neighbors(map, r, c):
			k = i 
			l = len(neighbors(map, r, c))
			p1 = k[0] 
			p2 = k[1] 
			if x > map[p1][p2]:
				h += 1
			else:
				break
		if h == l:
			return True
		return False
	else:
		return False

def join_map_side(map1, map2):
	final = []
	if len(map1) == len(map2):
		for i in range(len(map1)):
			xs = (map1[i] + map2[i])
			final.append(xs)
		return final
	else:
		return None

def join_map_below(map1, map2): #join 2 maps together
	for i in range(len(map1)):
		if len(map1[i]) == len(map2[i]):
			continue
		else:
			return None
	final = map1 + map2
	return final

def crop(map, r1, c1, r2, c2):
	list1 = [] #to place all the rows in 
	final_crop = [] #the final cropped version
	if r2 > len(map):
		r2 = len(map) - 1
	if c2 > len(map[0]):
		c2 = len(map[0]) - 1
	if r1 > r2 or c1 > c2:
		return []
	for i in range(r1,r2 + 1):
		list1.append(map[i])

	for i in range(len(list1)):
		mock = [] #to append the cropped row into final_crop
		for k in range(len(list1[i])):
			if k >= c1 and k <= c2:
				mock.append(list1[i][k])
		final_crop.append(mock)
	return final_crop

def flooded_map(map, rise): 
	final_flooded = [] 
	for i in range(len(map)):
		mock = [] #to append the list into the final list
		for k in map[i]:
			if k <= rise: #determines whether to append a 0 or new flooded value into list
				mock.append(0)
			elif k > rise:
				k -= rise
				mock.append(k)
		final_flooded.append(mock)

	return final_flooded

def flood_map(map, rise): #same as previous function but modifies original map
	for i in range(len(map)):
		for k in range(len(map[i])):
			if map[i][k] <= rise:
				map[i][k] = 0
			elif map[i][k] > rise:
				map[i][k] -= rise				

	return None

def find_land(map, r, c, dir):
	total = 0 
	land = False #to see if it is land
	if map[r][c] > 0:
		return 0
	if dir == "N": #c is the same
		if r == 0:
			return None
		for i in range(len(map)):
			r -= 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "NE": # r is lowered and c is increased
		if r == 0 and c == len(map[0]) - 1:
			return None
		for i in range(len(map) - 2):
			r -= 1
			c += 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "E":#r is the same
		if c == len(map[0]) - 1:
			return None
		for i in range(len(map[r])):
			c += 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "SE": #r is increased and c is decreased
		if r == len(map) - 1 and c == len(map[0]) - 1:
			return None
		for i in range(len(map) - 2):
			r += 1
			c -= 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "S": #c is the same
		if r == len(map) - 1:
			return None
		for i in range(len(map)):
			r += 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "SW": #r is increased and c is decreased
		if r == len(map) - 1 and c == 0:
			return None
		for i in range(len(map) - 2):
			r += 1
			c -= 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "W": #r is the same
		if c == 0:
			return None
		for i in range(len(map[r])):
			c -= 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	elif dir == "NW": #r is decreased and c is increased
		if r == 0 and c == 0:
			return None
		for i in range(len(map) - 2):
			r -= 1
			c -= 1
			if map[r][c] >= 0:
				total += 1
				if map[r][c] > 0:
					land = True
					break
	if land == True:
		return total
	else:
		return None

def reorient(map):
	final = []
	k = 0 #to determine what index value we are at
	for i in range(len(map[0])):
		list1 = []
		p1 = len(map) - 1
		for i2 in range(len(map)):
			list1.append(map[p1][k])
			p1 -= 1
		final.append(list1)
		if k != len(map[0]) - 1:
			k += 1
	if len(final) == len(map[0]):
		return final
	else:
		del final[-1]
	return final















