#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 5
# Due Date: 11/11/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def read_votes(filename):
	d = {}
	l = [] #to place the candidate tuples in  
	l2 = [] #to place all thee candidates in alphabetical order
	file = open(filename)
	x = file.readlines()
	del x[0] #get rid of header line
	state = "AL" #variable to identify if in the same state
	for i in x:
		st = i.strip("\n") #take off the \n on each line
		s = st.split(",") #split each piece into a list
		if s[0] != state:
			while len(l) != 0:
				l2.append(min(l)) #to start placing the names in alphabetical order
				l.remove(min(l))
			d[state] = l2 #once state changes, it will create the dictionary entry for the first state
			l = [] #empty list again and add new info for another state
			l2 = []
			state = s[0] #state gets the value of the new state
			name = s[1]
			party = s[2]
			popular_votes = int(s[3])
			electoral_votes = int(s[4])
			candidate = (name, party, popular_votes, electoral_votes)
			l.append(candidate)
			continue
		name = s[1]
		party = s[2]
		popular_votes = int(s[3])
		electoral_votes = int(s[4])
		candidate = (name, party, popular_votes, electoral_votes)
		l.append(candidate) #append candidate info into l
	d[state] = l2 #makes the last dictionary entry for the last state
	file.close()
	return d

def write_votes(db,filename):
	l = [] #to add string into list
	file = open(filename, "w")
	for key in db.keys(): #to keep the same key when making the string
		for value in range(len(db[key])): #to add the values into a string
			for i in range(4):
				l2 = [] #to add the individual values into list to get out of tuple
				l2.append(str(db[key][value][i]))
			s = key + " ,".join(l2)
			l.append(s)
	for i in l:
		file.writelines(i + "\n")

def read_abbreviations(filename): #ITS GOOD
	d = {}
	file = open(filename)
	x = file.readlines()
	del x[0] #get rid of header line
	for i in x:
		st = i.strip("\nÂ\xa0") #take off the \n on each line
		s = st.split(",") #split each piece into a list and get rid of Â\xa0
		d[s[0]] = s[1]
	file.close()
	return d

def add_candidate(db, state, name, party, popular_votes, electoral_votes): #ITS GOOD
	candidate = (name, party, popular_votes, electoral_votes)
	x = False #to check to see if name is in the db
	if state in db: #checks to see if state is in the db
		for key in db.keys():
			if key == state: #in order to see how many tuples that one state has
				for i in db[key]: #to go through the values in that key
					if name == i[0]: #to update the info
						for k in range(len(db[key])):
							if name == db[key][k][0]:
								index = k #to get the index of the value you are replacing
								break
							continue
						db[key].remove(i)
						db[key].insert(index,candidate)
						x = True
						break
				if x == False:
					for i in range(len(db[key])):
						if db[key][i][0] < name: #to place in alphabetical order
							if i == len(db[key]) - 1:
								db[key].insert(i + 1, candidate)
							continue
						elif db[key][i][0] > name:
							db[key].insert(i, candidate)
							break
						
			continue
	elif state not in db:
		db[state] = [candidate]
	return None

def remove_candidate(db, name, state = None): #ITS GOOD
	if state != None: #to see if a state was inputed
		for key in db.keys():
			if key == state: #check to see if the name is in the state given
				for i in db[key]: #goes through every value in that key
					if name == i[0]:
						db[key].remove(i) #removes that candidates info
						if len(db[key]) == 0:
							del db[key]
							return None
						else:
							return None
			continue
	else: #if state is not given then take out all occurence of the candidate
		for key in db.keys():
			for i in db[key]:
				if name == i[0]:
					db[key].remove(i) #get rid of all occurences of the candidate
					if len(db[key]) == 0:
						del db[key]
					continue
				continue
		return None
	return False

#{'AL': [('Trump', 'REP', 1318255, 9), ('Clinton', 'DEM', 729547, 0)}

def incorporate_precinct(db, name, state, popular_votes_increment): #ITS GOOD
	x = False #to check to see if name is in the db
	if state in db: #checks to see if state is in the db
		for key, values in db.items():
			if key == state: #in order to see how many tuples that one state has
				for i in db[key]:
					if name == i[0]:
						x = True
						nv = i[2] + popular_votes_increment #to get new value of P votes
						if nv <= 0:
							break
						candidate = (i[0], i[1], nv, i[3]) #make new tuple to add to values
						for k in range(len(db[key])):
							if name == db[key][k][0]:
								index = k #to get the index of the value you are replacing
								break
							continue
						db[key].remove(i) #get rid of old tuple 
						db[key].insert(index,candidate) #place in new tuple with correct order
						return None
				if x == False: #if name is not found then returns false
					return False
				else:
					for i in db[key]:
						if name == i[0]:
							db[key].remove(i)
							if len(db[key]) == 0:
								del db[key]
							return None
			continue
	elif state not in db:
		return False

def merge_votes(db, name1,name2, new_name, new_party, state = None): # 4 / 8
	n1 = [] #to keep candidate 1 info in
	n2 = [] #to keep candiate 2 info in
	x = False #to check to see if name is in the db
	t = 0 #to see if there is only one candidate in that state
	s1 = 0
	s2 = 0
	if state != None: 
		for key in db.keys():
			if key == state: #in order to see how many tuples that one state has
				for i in db[key]:
					if name1 == i[0]:
						x = True #used to show that a candidate exists in the db
						t += 2
						n1.append(i)
						s1 = i 
						continue
					if name2 == i[0]:
						x = True
						t += 3
						n2.append(i)
						s2 = i
						continue
					continue
			continue
		db[state].remove(s1)
		db[state].remove(s2)
		if x == False:
			return None
		if t < 5: #if only on candidate is present in the state
			if t == 2: #t determines which list got a tuple
				new_p_vote = n1[0][2]
				new_e_vote = n1[0][3]
			else:
				new_p_vote = n2[0][2]
				new_e_vote = n2[0][3]
			candidate = (new_name, new_party, new_p_vote, new_e_vote)
			db[state].append(candidate)
			return None
		new_p_vote = n1[0][2] + n2[0][2] #to merge the electoral and popular votes
		new_e_vote = n1[0][3] + n2[0][3]
		candidate = (new_name, new_party, new_p_vote, new_e_vote)
		db[state].append(candidate)
		return None
	elif state == None: #to get merge candidates in all states
		for key in db.keys():
			for i in db[key]:
				if name1 == i[0]:
					x = True
					t += 2
					n1.append(i)
					db[key].remove(i)
					continue
				if name2 == i[0]:
					x = True
					t += 3
					n2.append(i)
					db[key].remove(i)
					continue
				continue
			if x == False:
				return None
			if t < 5: #if only on candidate is present in the state
				if t == 2: #t determines which list got a tuple
					new_p_vote = n1[0][2]
					new_e_vote = n1[0][3]
				else:
					new_p_vote = n2[0][2]
					new_e_vote = n2[0][3]
				candidate = (new_name, new_party, new_p_vote, new_e_vote)
				db[state].append(candidate)
				continue
			new_p_vote = n1[0][2] + n2[0][2] #to merge the electoral and popular votes
			new_e_vote = n1[0][3] + n2[0][3]
			candidate = (new_name, new_party, new_p_vote, new_e_vote)
			db[key].append(candidate)
	return None

def number_of_votes(db, name, category = "poplar", numbering = "tally", state=None): #ITS GOOD
	p_e = [] #to place the candidates votes in 
	total_popular = 0
	total_electoral = 0 #candidates total in a state
	whole_popular = 0 #total popular votes 
	whole_electoral = 0
	total = 0 #used to calculate the percent if needed
	x = 0 #to determine if all parameters are correct
	b = False #to determine if the name is in the db
	if category == "popular" or category == "electoral":
		x += 1
	if numbering == "tally" or numbering == "percent":
		x += 1 
	if state in db or state == None:
		x += 1
	if x == 3: #if 3 of 4 parameters check out then we go into the code
		if state != None:
			for key, values in db.items():
				if key == state: #to get all occurence of the candidate in that state
					for i in db[key]:
						whole_electoral += i[3]
						whole_popular += i[2]
						if name == i[0]:
							b = True
							total_popular = i[2]
							total_electoral = i[3]
					if category == "electoral":
						if numbering != "tally":
							final = (float(total_electoral / whole_electoral)) * 100
							return round(final, 2)
						else: 
							return total_electoral
					else:
						if numbering != "tally":
							final = (float(total_popular / whole_popular)) * 100
							return round(final, 2)
						else:
							return total_popular
				continue
			if b == False:
				return False
		else:
			for key, values in db.items(): #to get all occurences of the candidate in db
				for i in db[key]:
					whole_popular += i[2]
					whole_electoral += i[3]
					if name == i[0]:
						b = True
						total_popular += i[2]
						total_electoral += i[3]
					continue
			if category == "electoral":
				if numbering != "tally": #for percents
					final = (float(total_electoral / whole_electoral)) * 100
					return round(final, 2)
				else: #for tallies
					return total_electoral
			else: #for popular votes
				if numbering != "tally": #percents
					final = (float(total_popular / whole_popular)) * 100
					return round(final, 2)
				else: 
					return total_popular

		if b == False:
			return False
	else: 
		return False


def popular_votes_performance(db, name, numbering, order = "max"): #ITS GOOD
	x = 0 #to check to see if the candidate is in the db
	ra = read_abbreviations("abbreviations.csv") #to have a db of the spelled out abbreviated values
	d = {} #to place that state and p votes
	total = 0 #used for calculating the percent
	final = 0
	biggest = 0
	smallest = 0
	if order == "max" or order == "min":
		for key, values in db.items():
			for i in db[key]: #to check to see if the candidate is in the db
				if name == i[0]:
					x += 1
				continue
		if x >= 1:
			if numbering == "tally": #for tallies
				if order == "max": #for max
					for key, values in db.items():
						for i in db[key]:
							if name == i[0]:
								d[key] = i[2]
							continue
					biggest = hs["GA"]
					state = "GA"
					for key, values in d.items():  #obtains the value of the abbreviated state
						if values > biggest:
							biggest = values
							state = key
						continue 
					return ra[state] #return the state spelled out from the abbrevaited db
				else: #for min
					for key, values in db.items():
						for i in db[key]:
							if name == i[0]:
								d[key] = i[2]
							continue
					smallest = d["GA"]
					state = "GA"
					for key, values in d.items():  #obtains the value of the abbreviated state
						if values < smallest:
							smallest = values
							state = key
						continue 
					return ra[state] #return the state spelled out from the abbrevaited db
			else: #for percents
				if order == "max":
					for key, values in db.items():
						total = 0
						final = 0
						for i in db[key]: #to obtain the total p votes in that state
							total += i[2]
						for i in db[key]: #to find the candidate
							if name == i[0]:
								final = (float(i[2] / total)) * 100
								d[key] = final
							continue
					for key, values in d.items():  #obtains the value of the abbreviated state
						if values > biggest:
							biggest = values
							state = key
						continue 
					return ra[state] #return the state spelled out from the abbrevaited db
				else:
					for key, values in db.items():
						total = 0
						final = 0
						for i in db[key]: #to obtain the total p votes in that state
							total += i[2]
						for i in db[key]: #to find the candidate
							if name == i[0]:
								final = (float(i[2] / total)) * 100
								d[key] = final
							continue
					smallest = d["GA"]
					state = "GA"
					for key, values in d.items():  #obtains the value of the abbreviated state
						if values < smallest:
							smallest = values
							state = key
						continue 
					return ra[state] #return the state spelled out from the abbrevaited db
		else:
			return False
	else:
		return False

def candidates_difference(db, name1, name2, order = "smallest"): #ITS GOOD
	b = False #this is to determine if both candidates did not compete in any state
	ra = read_abbreviations("abbreviations.csv") #to have a db of the spelled out abbreviated values
	d = {} #to create a dictionary of the states and the differences
	small = 0
	biggest = 0
	state = None
	if order == "smallest" or order == "largest":
		for key in db.keys():
			x = 0 #to check to see if the candidate is in the db
			total = 0 #used for calculating the percent
			for i in db[key]: #to check to see if the both candidates are in the same state 
				if name1 == i[0]:
					x += 1
				if name2 == i[0]:
					x += 1
				continue
			if x == 2:
				b = True
				for i in db[key]: #to get the total p votes in a state
					total += i[2]
				for i in db[key]: #to get the p votes for the candidates
					if name1 == i[0]:
						n1 = float(i[2] / total) * 100 #to find the percent in name1
					if name2 == i[0]:
						n2 = float(i[2] / total) * 100 #to find the percent in name2
					continue
				if n1 >= n2: #to determine the bigger num of the two to make a positive subtraction
					difference = n1 - n2
					d[key] = difference
				else: 
					difference = n2 - n1
					d[key] = difference
			else:
				continue
		if b == False:
			return False
		else:
			if order == "smallest":
				small = d["GA"]
				state = "GA"
				for key, values in d.items():  #obtains the value of the abbreviated state
					if values < small:
						small = values
						state = key
					continue 
				return ra[state] #return the state spelled out from the abbrevaited db
			else: #biggest 
				biggest = d["GA"]
				state = "GA"
				for key, values in d.items():  #obtains the value of the abbreviated state
					if values > biggest:
						biggest = values
						state = key
					continue 
				return ra[state] #return the state spelled out from the abbrevaited db 
	else: 
		return False




#get = {'GA': [('Allen', 'W', 5, 0), ('Buchanan', 'W', 31, 0), ('Byrne', 'W', 8, 0), ('Castle', 'W', 1110, 0), ('Clinton', 'DEM', 1877963, 0), ('Collins', 'W', 22, 0), ('Cubbler', 'W', 24, 0), ('Elliott', 'W', 15, 0), ('Fox', 'W', 78, 0), ('Hoefling', 'W', 70, 0), ('Johnson', 'LIB', 125306, 0), ('Kotlikoff', 'W', 34, 0), ('Maturen', 'W', 151, 0), ('McMullin', 'W', 13017, 0), ('Muhammad', 'W', 30, 0), ('Smith', 'W', 53, 0), ('Stein', 'W', 7674, 0), ('Trump', 'REP', 2089104, 16), ('Urbach', 'W', 5, 0), ('Wilson', 'W', 32, 0)], 'RI': [('Abstain', 'W', 5, 0), ('AnyoneElse', 'W', 7, 0), ('Belichek', 'W', 19, 0), ('Biden', 'W', 160, 0), ('Bloomberg', 'W', 32, 0), ('Brady', 'W', 86, 0), ('Buffet', 'W', 5, 0), ('Buffett', 'W', 7, 0), ('Bush', 'W', 71, 0), ('Carson', 'W', 66, 0), ('Castle', 'W', 52, 0), ('Chaffee', 'W', 8, 0), ('Chrisley', 'W', 19, 0), ('Christ', 'W', 70, 0), ('Christie', 'W', 11, 0), ('Clinton', 'DEM', 252525, 4), ('CohenT', 'W', 18, 0), ('CooperA', 'W', 5, 0), ('Cruz', 'W', 46, 0), ('DeLaFuente', 'ADP', 671, 0), ('Duck', 'W', 18, 0), ('Fecteau', 'W', 8, 0), ('Fiorina', 'W', 12, 0), ('GodAlmighty', 'W', 20, 0), ('GodHelpUs', 'W', 5, 0), ('Gowdy', 'W', 8, 0), ('Harambe', 'W', 15, 0), ('Healey', 'W', 5, 0), ('Hoefling', 'W', 7, 0), ('Huckabee', 'W', 9, 0), ('Johnson', 'LIB', 14746, 0), ('Kaine', 'W', 7, 0), ('Kasich', 'W', 695, 0), ('Kenniston', 'W', 6, 0), ('LaRiva', 'W', 8, 0), ('Lincoln', 'W', 13, 0), ('Maturen', 'W', 34, 0), ('McCain', 'W', 124, 0), ('McMullin', 'W', 773, 0), ('Me', 'W', 6, 0), ('Mouse', 'W', 79, 0), ('Murray', 'W', 5, 0), ('NA', 'W', 6, 0), ('Neuman', 'W', 8, 0), ('NoConfidence', 'W', 15, 0), ('NoOne', 'W', 8, 0), ('None', 'W', 19, 0), ('NoneOfTheAbove', 'W', 70, 0), ('Norton', 'W', 6, 0), ('Nutz', 'W', 6, 0), ('ObamaB', 'W', 13, 0), ('ObamaM', 'W', 34, 0), ('Pence', 'W', 291, 0), ('Pope Francis', 'W', 7, 0), ('Powell', 'W', 41, 0), ('RandPaul', 'W', 18, 0), ('Reagan', 'W', 5, 0), ('Reed', 'W', 5, 0), ('Rice', 'W', 26, 0), ('Romney', 'W', 273, 0), ('RonPaul', 'W', 11, 0), ('Roosevelt', 'W', 6, 0), ('Rubio', 'W', 99, 0), ('Ryan', 'W', 249, 0), ('Sanders', 'W', 3497, 0), ('Scattered', 'W', 2121, 0), ('Stein', 'GRE', 6220, 0), ('Supreme', 'W', 17, 0), ('Trump', 'REP', 180543, 0), ('UnityLoveHarmony', 'W', 5, 0), ('Ventura', 'W', 8, 0), ('Warren', 'W', 12, 0), ('Washington', 'W', 5, 0), ('Webb', 'W', 7, 0), ('WilliamsR', 'W', 7, 0)], 'NJ': [('Castle', 'CON', 6161, 0), ('Clinton', 'DEM', 2148278, 14), ('DeLaFuente', 'ADP', 1838, 0), ('Johnson', 'LIB', 72477, 0), ('Kennedy', 'SWP', 2156, 0), ('LaRiva', 'SLP', 1682, 0), ('Moorehead', 'WW', 1749, 0), ('Stein', 'GRE', 37772, 0), ('Trump', 'REP', 1601933, 0)], 'FL': [('Basiago', 'W', 24, 0), ('Castle', 'CPF', 16475, 0), ('Clinton', 'DEM', 4504975, 0), ('DeLaFuente', 'RPF', 9108, 0), ('Duncan', 'W', 25, 0), ('Fox', 'W', 2, 0), ('Gyurko', 'W', 19, 0), ('Johnson', 'LBF', 207043, 0), ('Kotlikoff', 'W', 74, 0), ('Stein', 'GPF', 64399, 0), ('Trump', 'REP', 4617886, 29), ('Valdivia', 'W', 9, 0)], 'NC': [('Clinton', 'DEM', 2189316, 0), ('Johnson', 'LIB', 130126, 0), ('Scattered', 'W', 47386, 0), ('Stein', 'W', 12105, 0), ('Trump', 'REP', 2362631, 15)], 'CA': [('Clinton', 'DEM', 8753792, 55), ('Johnson', 'LIB', 478500, 0), ('Kotlikoff', 'W', 402, 0), ('LaRiva', 'PAF', 66101, 0), ('Maturen', 'W', 1316, 0), ('McMullin', 'W', 39596, 0), ('Sanders', 'W', 79341, 0), ('Stein', 'GRE', 278658, 0), ('Trump', 'REP/AIP', 4483814, 0), ('White', 'W', 84, 0)], 'MS': [('Castle', 'CON', 3987, 0), ('Clinton', 'DEM', 485131, 0), ('DeLaFuente', 'ADP', 644, 0), ('Hedges', 'P', 715, 0), ('Johnson', 'LIB', 14435, 0), ('Stein', 'GRE', 3731, 0), ('Trump', 'REP', 700714, 6)], 'OH': [('Bell', 'W', 9, 0), ('Bickelmeyer', 'W', 6, 0), ('Castle', 'W', 1887, 0), ('Clinton', 'DEM', 2394164, 0), ('Duncan', 'N', 24235, 0), ('Fox', 'W', 5, 0), ('Hartnell', 'W', 589, 0), ('Hoefling', 'W', 268, 0), ('Jaynes', 'W', 8, 0), ('Johnson', 'N', 174498, 0), ('Keniston', 'W', 114, 0), ('Kirschner', 'W', 15, 0), ('Kotlikoff', 'W', 90, 0), ('Maldonado', 'W', 18, 0), ('Maturen', 'W', 552, 0), ('McMullin', 'W', 12574, 0), ('Moorehead', 'W', 19, 0), ('Schriner', 'W', 62, 0), ('Smith', 'W', 62, 0), ('Stein', 'GRE', 46271, 0), ('Stroh', 'W', 30, 0), ('Thomson', 'W', 6, 0), ('Trump', 'REP', 2841005, 18)], 'MA': [('AllOthers', 'W', 50488, 0), ('Clinton', 'DEM', 1995196, 11), ('Feegbeh', 'W', 28, 0), ('Johnson', 'LIB', 138018, 0), ('Kotlikoff', 'W', 28, 0), ('McMullin', 'W', 2719, 0), ('Moorehead', 'W', 15, 0), ('Stein', 'GR', 47661, 0), ('Trump', 'REP', 1090893, 0)], 'SD': [('Castle', 'CON', 4064, 0), ('Clinton', 'DEM', 117458, 0), ('Johnson', 'LIB', 20850, 0), ('Trump', 'REP', 227721, 3)], 'WV': [('Basiago', 'W', 4, 0), ('Buchanan', 'W', 3, 0), ('Castle', 'CON', 3807, 0), ('Clinton', 'DEM', 188794, 0), ('DeLaFuente', 'W', 3, 0), ('Duncan', 'W', 1, 0), ('Hartnell', 'W', 1, 0), ('Hoefling', 'W', 10, 0), ('Johnson', 'LIB', 23004, 0), ('Kotlikoff', 'W', 4, 0), ('LaRiva', 'W', 2, 0), ('Limbaugh', 'W', 3, 0), ('Maldonado', 'W', 1, 0), ('McMullin', 'W', 1104, 0), ('Moreau', 'W', 216, 0), ('PerryDarryl', 'W', 2, 0), ('Smith', 'W', 2, 0), ('SmithW', 'W', 13, 0), ('Stein', 'MTP', 8075, 0), ('Trump', 'REP', 489371, 5), ('White', 'W', 2, 0), ('Williams', 'W', 1, 0)], 'AR': [('Castle', 'CON', 4613, 0), ('Clinton', 'DEM', 380494, 0), ('Hedges', 'IND', 4709, 0), ('Johnson', 'LIB', 29949, 0), ('Kahn', 'IND', 3390, 0), ('McMullin', 'BFA', 13176, 0), ('Stein', 'GRE', 9473, 0), ('Trump', 'REP', 684872, 6)], 'DE': [('Buchanan', 'W', 4, 0), ('Castle', 'W', 74, 0), ('Clinton', 'DEM', 235603, 3), ('DeLaFuente', 'W', 3, 0), ('Duncan', 'W', 1, 0), ('Hartnell', 'W', 3, 0), ('Hoefling', 'W', 7, 0), ('Johnson', 'LIB', 14757, 0), ('Kahn', 'W', 1, 0), ('LaRiva', 'W', 3, 0), ('Limbaugh', 'W', 3, 0), ('Locke', 'W', 1, 0), ('Maldonado', 'W', 1, 0), ('McMullin', 'W', 706, 0), ('Other', 'W', 1407, 0), ('PerryDarryl', 'W', 1, 0), ('Scott', 'W', 2, 0), ('Smith', 'W', 3, 0), ('Sood', 'W', 1, 0), ('Stein', 'GRE', 6103, 0), ('Stout', 'W', 1, 0), ('Trump', 'REP', 185127, 0), ('White', 'W', 2, 0)], 'NH': [('Biden', 'W', 55, 0), ('Bush', 'W', 230, 0), ('Carson', 'W', 83, 0), ('Christie', 'W', 23, 0), ('Clinton', 'DEM', 348526, 4), ('Cruz', 'W', 129, 0), ('DeLaFuente', 'ADP', 678, 0), ('Johnson', 'LIB', 30777, 0), ('Kasich', 'W', 1365, 0), ('McCain', 'W', 127, 0), ('McMullin', 'W', 1064, 0), ('Paul', 'W', 98, 0), ('Pence', 'W', 937, 0), ('Romney', 'W', 540, 0), ('Rubio', 'W', 136, 0), ('Ryan', 'W', 280, 0), ('Sanders', 'W', 4493, 0), ('Scattered', 'W', 2411, 0), ('Stein', 'GRE', 6496, 0), ('Supreme', 'W', 58, 0), ('Trump', 'REP', 345790, 0)], 'NM': [('Castle', 'CON', 1514, 0), ('Clinton', 'DEM', 385234, 5), ('DeLaFuente', 'ADP', 475, 0), ('Johnson', 'LIB', 74541, 0), ('LaRiva', 'PSL', 1184, 0), ('McMullin', 'BFA', 5825, 0), ('Stein', 'GRE', 9879, 0), ('Trump', 'REP', 319667, 0)], 'NV': [('Castle', 'IAP', 5268, 0), ('Clinton', 'DEM', 539260, 6), ('DeLaFuente', 'NPY', 2552, 0), ('Johnson', 'LIB', 37384, 0), ('NoneofTheseCandidates', 'W', 28863, 0), ('Trump', 'REP', 512058, 0)], 'CT': [('Basiago', 'W', 42, 0), ('Blumenthal', 'W', 12, 0), ('Buchanan', 'W', 19, 0), ('Castle', 'W', 147, 0), ('Clinton', 'DEM', 897572, 7), ('CooperJ', 'W', 57, 0), ('Cummings', 'W', 5, 0), ('DeLaFuente', 'W', 12, 0), ('Deame', 'W', 13, 0), ('Evans', 'W', 44, 0), ('Fox', 'W', 3, 0), ('Hoefling', 'W', 31, 0), ('Johnson', 'LIB', 48676, 0), ('Klojzy', 'W', 6, 0), ('Kotlikoff', 'W', 23, 0), ('LaRiva', 'W', 41, 0), ('Maldonado', 'W', 4, 0), ('McMullin', 'W', 2108, 0), ('Schoenke', 'W', 15, 0), ('Skewes', 'W', 4, 0), ('Smith', 'W', 12, 0), ('Stein', 'GRE', 22841, 0), ('Trump', 'REP', 673215, 0), ('Wu', 'W', 18, 0)], 'PA': [('Castle', 'CON', 21572, 0), ('Clinton', 'DEM', 2926441, 0), ('Johnson', 'LIB', 146715, 0), ('Kahn', 'W', 3, 0), ('Kasich', 'W', 302, 0), ('McMullin', 'W', 6472, 0), ('Sanders', 'W', 6060, 0), ('Scattered', 'W', 37239, 0), ('Stein', 'GRE', 49941, 0), ('Trump', 'REP', 2970733, 20)], 'KS': [('Basiago', 'W', 6, 0), ('Castle', 'W', 646, 0), ('Clinton', 'DEM', 427005, 0), ('DeLaFuente', 'W', 3, 0), ('Hedges', 'W', 3, 0), ('Hoefling', 'W', 45, 0), ('Johnson', 'LIB', 55406, 0), ('Kahn', 'W', 2, 0), ('LaRiva', 'W', 7, 0), ('Maturen', 'W', 214, 0), ('McMullin', 'W', 6520, 0), ('PerryDarryl', 'W', 1, 0), ('Schriner', 'W', 3, 0), ('Smith', 'W', 6, 0), ('Sood', 'W', 10, 0), ('Stein', 'IND', 23506, 0), ('Sterling', 'W', 1, 0), ('Trump', 'REP', 671018, 6)], 'CO': [('Atwood', 'APV', 337, 0), ('Castle', 'AMC', 11699, 0), ('Clinton', 'DEM', 1338870, 9), ('DeLaFuente', 'W', 1255, 0), ('Fox', 'W', 2, 0), ('Hedges', 'P', 185, 0), ('Hoefling', 'AMP', 710, 0), ('Johnson', 'LIB', 144121, 0), ('Keniston', 'VPA', 5028, 0), ('Kennedy', 'SWP', 452, 0), ('Kopitke', 'IAP', 1096, 0), ('Kotlikoff', 'KFP', 392, 0), ('LaRiva', 'SLP', 531, 0), ('Lohmiller', 'W', 3, 0), ('Lyttle', 'NRP', 382, 0), ('Maldonado', 'IPC', 872, 0), ('Maturen', 'ASP', 862, 0), ('McMullin', 'UN', 28917, 0), ('Nieman', 'W', 1, 0), ('PerryBrian', 'W', 4, 0), ('PerryDavid', 'W', 11, 0), ('Scott', 'UN', 749, 0), ('Silva', 'NTP', 751, 0), ('Smith', 'UN', 1819, 0), ('Soltysik', 'SOC', 271, 0), ('Stein', 'GRE', 38437, 0), ('Sterner', 'W', 6, 0), ('Trump', 'REP', 1202484, 0)], 'ND': [('Castle', 'CON', 1833, 0), ('Clinton', 'DNL', 93758, 0), ('DeLaFuente', 'ADP', 364, 0), ('Johnson', 'LIB', 21434, 0), ('Scattered', 'W', 6397, 0), ('Stein', 'GRE', 3780, 0), ('Trump', 'REP', 216794, 3)], 'UT': [('Baird', 'W', 9, 0), ('Basiago', 'W', 4, 0), ('Buchanan', 'W', 1, 0), ('Burton', 'W', 1, 0), ('Castle', 'CON', 8032, 0), ('Clinton', 'DEM', 310676, 0), ('DeLaFuente', 'UN', 883, 0), ('Giordani', 'IAP', 2752, 0), ('Hoefling', 'W', 6, 0), ('Johnson', 'LIB', 39608, 0), ('Kennedy', 'UN', 521, 0), ('Kotlikoff', 'W', 9, 0), ('McMullin', 'UN', 243690, 0), ('Moorehead', 'UN', 544, 0), ('Smith', 'W', 19, 0), ('Soltysik', 'W', 4, 0), ('Stein', 'UN', 9438, 0), ('Tittle', 'W', 1, 0), ('Trump', 'REP', 515231, 6), ('Valdivia', 'W', 1, 0)], 'IA': [('Castle', 'CON', 5335, 0), ('Clinton', 'DEM', 653669, 0), ('DeLaFuente', 'NP', 451, 0), ('Johnson', 'LIB', 59186, 0), ('Kahn', 'NPI', 2247, 0), ('LaRiva', 'PSL', 323, 0), ('McMullin', 'NP', 12366, 0), ('Scattered', 'W', 17746, 0), ('Stein', 'IG', 11479, 0), ('Trump', 'REP', 800983, 6), ('Vacek', 'LMN', 2246, 0)], 'NY': [('Asherie', 'W', 9, 0), ('Blickley', 'W', 2, 0), ('Buchanan', 'W', 58, 0), ('Canns', 'W', 5, 0), ('Carter', 'W', 18, 0), ('Castle', 'W', 955, 0), ('Clinton', 'DEM', 4556118, 29), ('CohenA', 'W', 33, 0), ('Connolly', 'W', 30, 0), ('DeLaFuente', 'W', 35, 0), ('Fried', 'W', 6, 0), ('Gyurko', 'W', 76, 0), ('Hartnell', 'W', 42, 0), ('Hoefling', 'W', 137, 0), ('Ingbar', 'W', 8, 0), ('Johnson', 'IDP', 176598, 0), ('Kahn', 'W', 72, 0), ('Keniston', 'W', 90, 0), ('LaRiva', 'W', 175, 0), ('Mackler', 'W', 15, 0), ('Maturen', 'W', 458, 0), ('McMullin', 'W', 10397, 0), ('Moorehead', 'W', 68, 0), ('Mutford', 'W', 85, 0), ('RobertsC', 'W', 88, 0), ('Scattered', 'W', 48343, 0), ('Schoenke', 'W', 3, 0), ('Scott', 'W', 3, 0), ('Soltysik', 'W', 36, 0), ('Stein', 'GRE', 107935, 0), ('Trump', 'REP', 2819533, 0), ('Valdivia', 'W', 4, 0), ('Welsh', 'W', 1, 0), ('Whitaker', 'W', 1, 0), ('Wolff', 'W', 5, 0)], 'AL': [('Clinton', 'DEM', 729547, 0), ('Johnson', 'IND', 44467, 0), ('Scattered', 'W', 21712, 0), ('Stein', 'IND', 9391, 0), ('Trump', 'REP', 1318255, 9)], 'VT': [('Belichek', 'W', 7, 0), ('Biden', 'W', 57, 0), ('Bloomberg', 'W', 22, 0), ('Brady', 'W', 9, 0), ('Bush', 'W', 79, 0), ('Carson', 'W', 61, 0), ('Castle', 'W', 63, 0), ('Clinton', 'DEM', 178573, 3), ('Cruz', 'W', 63, 0), ('DeLaFuente', 'IND', 1063, 0), ('Douglas', 'W', 75, 0), ('Epstein', 'W', 11, 0), ('Fiorina', 'W', 11, 0), ('Gabard', 'W', 17, 0), ('Huckabee', 'W', 11, 0), ('Johnson', 'LIB', 10078, 0), ('Kasich', 'W', 827, 0), ('Keniston', 'W', 3, 0), ('Kotlikoff', 'W', 3, 0), ('LaRiva', 'LBU', 327, 0), ('Leahy', 'W', 7, 0), ('Maturen', 'W', 14, 0), ('McCain', 'W', 76, 0), ('McMullin', 'W', 640, 0), ('Nader', 'W', 7, 0), ('NoName', 'W', 255, 0), ('ObamaB', 'W', 8, 0), ('ObamaM', 'W', 15, 0), ('Ortiz', 'W', 8, 0), ('Osborne', 'W', 2, 0), ('Pence', 'W', 298, 0), ('Powell', 'W', 25, 0), ('RandPaul', 'W', 26, 0), ('Rice', 'W', 18, 0), ('Romney', 'W', 120, 0), ('RonPaul', 'W', 25, 0), ('Rubio', 'W', 93, 0), ('Ryan', 'W', 208, 0), ('Sanders', 'W', 18218, 0), ('Scattered', 'W', 1478, 0), ('Smith', 'W', 1, 0), ('Soltysik', 'W', 2, 0), ('Stein', 'GRE', 6758, 0), ('Supreme', 'W', 10, 0), ('Trump', 'REP', 95369, 0), ('Tuttle', 'W', 6, 0), ('Warren', 'W', 13, 0), ('Weld', 'W', 5, 0), ('White', 'W', 2, 0)], 'TX': [('Castle', 'W', 4261, 0), ('Clinton', 'DEM', 3877868, 0), ('Cubbler', 'W', 314, 0), ('Fox', 'W', 45, 0), ('Hoefling', 'W', 932, 0), ('Johnson', 'LIB', 283492, 0), ('Kotlikoff', 'W', 1037, 0), ('Lee', 'W', 67, 0), ('Maturen', 'W', 1401, 0), ('McMullin', 'W', 42366, 0), ('Moorehead', 'W', 122, 0), ('Morrow', 'W', 145, 0), ('Soltysik', 'W', 72, 0), ('Steffes', 'W', 71, 0), ('Stein', 'GRE', 71558, 0), ('Trump', 'REP', 4685047, 36), ('Valdivia', 'W', 428, 0)], 'SC': [('Castle', 'CON', 5765, 0), ('Clinton', 'DEM', 855373, 0), ('Johnson', 'LIB', 49204, 0), ('McMullin', 'IDP', 21016, 0), ('Skewes', 'AM', 3246, 0), ('Stein', 'GRE', 13034, 0), ('Trump', 'REP', 1155389, 9)], 'ME': [('Castle', 'W', 333, 0), ('Clinton', 'DEM', 357735, 3), ('Fox', 'W', 7, 0), ('Johnson', 'LIB', 38105, 0), ('Kotlikoff', 'W', 16, 0), ('McMullin', 'W', 1887, 0), ('Stein', 'GI', 14251, 0), ('Trump', 'REP', 335593, 1)], 'HI': [('Castle', 'CON', 4508, 0), ('Clinton', 'DEM', 266891, 3), ('Johnson', 'LIB', 15954, 0), ('Stein', 'GRE', 12737, 0), ('Trump', 'REP', 128847, 0)], 'MN': [('Ball', 'W', 24, 0), ('Bartlett', 'W', 41, 0), ('Castle', 'CON', 9456, 0), ('Clinton', 'DFL', 1367716, 10), ('DeLaFuente', 'ADP', 1431, 0), ('Duncan', 'W', 1, 0), ('Gerhard', 'W', 1, 0), ('Hartnell', 'W', 2, 0), ('Hoefling', 'W', 28, 0), ('Johnson', 'LIB', 112972, 0), ('Keniston', 'W', 31, 0), ('Kennedy', 'SWP', 1672, 0), ('Koplitz', 'W', 2, 0), ('Kotlikoff', 'W', 17, 0), ('LaRiva', 'W', 12, 0), ('Lynch', 'W', 1, 0), ('Mallapadi', 'W', 2, 0), ('Maturen', 'W', 244, 0), ('McMullin', 'IDP', 53076, 0), ('Muffoletto', 'W', 29, 0), ('Payeur', 'W', 2, 0), ('Roberts', 'W', 1, 0), ('RobertsC', 'W', 15, 0), ('Robertson', 'W', 1, 0), ('Scattered', 'W', 26714, 0), ('Schriner', 'W', 4, 0), ('Schumacher', 'W', 1, 0), ('Sidner', 'W', 4, 0), ('Smith', 'W', 3, 0), ('Snell', 'W', 1, 0), ('Soltysik', 'W', 15, 0), ('Stein', 'GRE', 36985, 0), ('Trump', 'REP', 1322951, 0), ('Vacek', 'LMN', 11291, 0), ('Wettschreck', 'W', 4, 0), ('Wharton', 'W', 53, 0), ('White', 'W', 10, 0)], 'IN': [('BrownR', 'IND', 11, 0), ('Castle', 'W', 1937, 0), ('Clinton', 'DEM', 1033126, 0), ('DeLaFuente', 'W', 21, 0), ('Duncan', 'W', 25, 0), ('Fox', 'W', 1, 0), ('Hoefling', 'W', 269, 0), ('Jackson', 'W', 121, 0), ('Johnson', 'LIB', 133993, 0), ('Kelly', 'W', 44, 0), ('Kotlikoff', 'W', 49, 0), ('Maldonado', 'W', 7, 0), ('Mullis', 'W', 22, 0), ('Roberts', 'W', 148, 0), ('Soltysik', 'W', 57, 0), ('Stein', 'W', 7841, 0), ('Trump', 'REP', 1557286, 11)], 'DC': [('Clinton', 'DEM', 282830, 3), ('Johnson', 'LIB', 4906, 0), ('Scattered', 'W', 6551, 0), ('Stein', 'STG', 4258, 0), ('Trump', 'REP', 12723, 0)], 'AZ': [('Buchanan', 'W', 56, 0), ('Carter', 'DEM', 42, 0), ('Castle', 'W', 1058, 0), ('Clinton', 'DEM', 1161167, 0), ('Corsetti', 'W', 3, 0), ('DeLaFuente', 'W', 29, 0), ('Fox', 'W', 14, 0), ('Hartnell', 'W', 11, 0), ('Hoefling', 'W', 85, 0), ('In-Albon', 'W', 24, 0), ('Johnson', 'LIB', 106327, 0), ('Kotlikoff', 'W', 52, 0), ('Maldonado', 'W', 20, 0), ('McMullin', 'W', 17449, 0), ('Schoenke', 'W', 4, 0), ('Smith', 'W', 62, 0), ('Stein', 'GRE', 34345, 0), ('Steinacker', 'W', 4, 0), ('Tittle', 'W', 12, 0), ('Trump', 'REP', 1252401, 11)], 'OK': [('Clinton', 'DEM', 420375, 0), ('Johnson', 'LIB', 83481, 0), ('Trump', 'REP', 949136, 7)], 'KY': [('Castle', 'W', 438, 0), ('Clark', 'W', 2, 0), ('Clinton', 'DEM', 628854, 0), ('Cubbler', 'W', 6, 0), ('DeLaFuente', 'ADP', 1128, 0), ('Duncan', 'W', 2, 0), ('Ellis', 'W', 14, 0), ('Fox', 'W', 1, 0), ('Hartnell', 'W', 5, 0), ('Hoefling', 'W', 39, 0), ('Jackson', 'W', 18, 0), ('Johnson', 'LIB', 53752, 0), ('Keniston', 'W', 22, 0), ('Kotlikoff', 'W', 8, 0), ('Ling', 'W', 1, 0), ('Luesing', 'W', 6, 0), ('Maldonado', 'W', 2, 0), ('Maturen', 'W', 155, 0), ('McMullin', 'IND', 22780, 0), ('PerryDavid', 'W', 4, 0), ('Schoenke', 'W', 2, 0), ('Smith', 'W', 9, 0), ('Stein', 'GRE', 13913, 0), ('Stevens', 'W', 12, 0), ('Tittle', 'W', 1, 0), ('Trump', 'REP', 1202971, 8), ('White', 'W', 4, 0)], 'WI': [('Castle', 'CON', 12162, 0), ('Clinton', 'DEM', 1382536, 0), ('DeLaFuente', 'ADP', 1502, 0), ('Fox', 'W', 47, 0), ('Hoefling', 'W', 80, 0), ('Johnson', 'LIB', 106674, 0), ('Keniston', 'W', 67, 0), ('Kotlikoff', 'W', 15, 0), ('Maldonado', 'W', 4, 0), ('Maturen', 'W', 284, 0), ('McMullin', 'W', 11855, 0), ('Moorehead', 'WW', 1770, 0), ('Scattered', 'W', 22764, 0), ('Schoenke', 'W', 1, 0), ('Soltysik', 'W', 33, 0), ('Stein', 'WG', 31072, 0), ('Trump', 'REP', 1405284, 10)], 'MT': [('Basiago', 'W', 3, 0), ('Buchanan', 'W', 2, 0), ('Castle', 'W', 296, 0), ('Clinton', 'DEM', 177709, 0), ('DeLaFuente', 'ADP', 1570, 0), ('Hoefling', 'W', 10, 0), ('Johnson', 'LIB', 28037, 0), ('Kotlikoff', 'W', 7, 0), ('Maldonado', 'W', 1, 0), ('McMullin', 'W', 2297, 0), ('Morris', 'W', 1, 0), ('PerryDarryl', 'W', 1, 0), ('Schriner', 'W', 1, 0), ('Smith', 'W', 1, 0), ('Soltysik', 'W', 1, 0), ('Stein', 'GRE', 7970, 0), ('Trump', 'REP', 279240, 3)], 'WY': [('Castle', 'CON', 2042, 0), ('Clinton', 'DEM', 55973, 0), ('DeLaFuente', 'IND', 709, 0), ('Johnson', 'LIB', 13287, 0), ('Scattered', 'W', 6904, 0), ('Stein', 'IND', 2515, 0), ('Trump', 'REP', 174419, 3)], 'IL': [('Anderson', 'W', 61, 0), ('Breivogel', 'W', 12, 0), ('Brumfield', 'W', 5, 0), ('Castle', 'W', 1138, 0), ('Clinton', 'DEM', 3090729, 20), ('Fox', 'W', 3, 0), ('Harper', 'W', 1, 0), ('Hartnell', 'W', 6, 0), ('Hoefling', 'W', 175, 0), ('Johnson', 'LIB', 209596, 0), ('JohnsonN', 'W', 1, 0), ('Kotlikoff', 'W', 82, 0), ('Lee', 'W', 7, 0), ('Maldonado', 'W', 20, 0), ('McKee', 'W', 24, 0), ('McMullin', 'W', 11655, 0), ('Meluch', 'W', 3, 0), ('Morris', 'W', 10, 0), ('Roberts', 'W', 8, 0), ('Schoenke', 'W', 25, 0), ('Seeberg', 'W', 27, 0), ('SmithD', 'W', 4, 0), ('Stack', 'W', 10, 0), ('Stein', 'GRE', 76802, 0), ('Struck', 'W', 1, 0), ('Trump', 'REP', 2146015, 0), ('Tyree', 'W', 3, 0), ('Wysinger', 'W', 1, 0)], 'MD': [('Adams', 'W', 44, 0), ('Bolar', 'W', 7, 0), ('Boring', 'W', 53, 0), ('Bowhall', 'W', 7, 0), ('Boyles', 'W', 5, 0), ('Breivogel', 'W', 20, 0), ('BrownD', 'W', 15, 0), ('BrownT', 'W', 4, 0), ('Buchanan', 'W', 25, 0), ('Carlisle', 'W', 51, 0), ('Castle', 'W', 566, 0), ('Clinton', 'DEM', 1677928, 10), ('DeLaFuente', 'W', 14, 0), ('Duncan', 'W', 18, 0), ('Edgell', 'W', 1, 0), ('Flippin', 'W', 6, 0), ('Fox', 'W', 9, 0), ('Gates', 'W', 36, 0), ('Hartnell', 'W', 24, 0), ('Hedges', 'W', 5, 0), ('Hoefling', 'W', 42, 0), ('Jennings', 'W', 4, 0), ('Johnson', 'LIB', 79605, 0), ('Kahn', 'W', 18, 0), ('Keita', 'W', 2, 0), ('Kotlikoff', 'W', 73, 0), ('LaRiva', 'W', 48, 0), ('Locke', 'W', 10, 0), ('Maldonado', 'W', 12, 0), ('Maturen', 'W', 504, 0), ('McCarthy', 'W', 97, 0), ('McMullin', 'W', 9630, 0), ('Other', 'W', 33263, 0), ('Pendleton', 'W', 17, 0), ('Puskar', 'W', 7, 0), ('Reid', 'W', 53, 0), ('Schoenke', 'W', 3, 0), ('Schriner', 'W', 9, 0), ('Smith', 'W', 13, 0), ('SmithC', 'W', 11, 0), ('Soldjah', 'W', 13, 0), ('Soltysik', 'W', 6, 0), ('Stein', 'GRE', 35945, 0), ('Symonette', 'W', 10, 0), ('Terry', 'W', 1, 0), ('Thomas', 'W', 16, 0), ('Trump', 'REP', 943169, 0), ('Vakil', 'W', 1, 0), ('Valdivia', 'W', 11, 0), ('Vogel-Walcutt', 'W', 2, 0), ('White', 'W', 11, 0), ('Williams', 'W', 1, 0), ('Wysinger', 'W', 1, 0)], 'ID': [('Castle', 'IND', 4403, 0), ('Clinton', 'DEM', 189765, 0), ('Copeland', 'CON', 2356, 0), ('DeLaFuente', 'IND', 1373, 0), ('Johnson', 'LIB', 28331, 0), ('McMullin', 'IND', 46476, 0), ('Stein', 'IND', 8496, 0), ('Trump', 'REP', 409055, 4)], 'OR': [('Clinton', 'DEM', 1002106, 7), ('Johnson', 'LIB', 94231, 0), ('Miscellaneous', 'W', 72594, 0), ('Stein', 'PG/PRO', 50002, 0), ('Trump', 'REP', 782403, 0)], 'MO': [('Castle', 'CON', 13092, 0), ('Clinton', 'DEM', 1071068, 0), ('DeLaFuente', 'W', 6, 0), ('Hoefling', 'W', 48, 0), ('Johnson', 'LIB', 97359, 0), ('Kotlikoff', 'W', 28, 0), ('McMullin', 'W', 7071, 0), ('Schoenke', 'W', 3, 0), ('Stein', 'GRE', 25419, 0), ('Trump', 'REP', 1594511, 10)], 'VA': [('AllOthers', 'W', 33749, 0), ('Clinton', 'DEM', 1981473, 13), ('Johnson', 'LIB', 118274, 0), ('McMullin', 'IND', 54054, 0), ('Stein', 'GRE', 27638, 0), ('Trump', 'REP', 1769443, 0)], 'TN': [('Castle', 'W', 1584, 0), ('Clinton', 'DEM', 870695, 0), ('DeLaFuente', 'IND', 4075, 0), ('Fox', 'W', 6, 0), ('Hoefling', 'W', 132, 0), ('Johnson', 'IND', 70397, 0), ('Kennedy', 'IND', 2877, 0), ('Kotlikoff', 'W', 20, 0), ('Limbaugh', 'W', 53, 0), ('McMullin', 'W', 11991, 0), ('Schoenke', 'W', 3, 0), ('Smith', 'IND', 7276, 0), ('Stein', 'IND', 15993, 0), ('Trump', 'REP', 1522925, 11)], 'MI': [('Castle', 'UST', 16139, 0), ('Clinton', 'DEM', 2268839, 0), ('Fox', 'W', 10, 0), ('Hartnell', 'W', 39, 0), ('Hoefling', 'W', 95, 0), ('Johnson', 'LIB', 172136, 0), ('Kotlikoff', 'W', 87, 0), ('Maturen', 'W', 517, 0), ('McMullin', 'W', 8177, 0), ('Moorehead', 'W', 30, 0), ('Soltysik', 'NLP', 2209, 0), ('Stein', 'GRE', 51463, 0), ('Trump', 'REP', 2279543, 16)], 'AK': [('Castle', 'CON', 3866, 0), ('Clinton', 'DEM', 116454, 0), ('DeLaFuente', 'NAF', 1240, 0), ('Johnson', 'LIB', 18725, 0), ('Scattered', 'W', 9201, 0), ('Stein', 'GRE', 5735, 0), ('Trump', 'REP', 163387, 3)], 'NE': [('Clinton', 'DEM', 284494, 0), ('Johnson', 'LIB', 38946, 0), ('Scattered', 'W', 16051, 0), ('Stein', 'BP', 8775, 0), ('Trump', 'REP', 495961, 5)], 'WA': [('Castle', 'CON', 17623, 0), ('Clinton', 'DEM', 1742718, 8), ('Johnson', 'LIB', 160879, 0), ('Kennedy', 'SWP', 4307, 0), ('LaRiva', 'SLP', 3523, 0), ('Scattered', 'W', 107805, 0), ('Stein', 'GRE', 58417, 0), ('Trump', 'REP', 1221747, 0)], 'LA': [('Castle', 'CON', 3129, 0), ('Clinton', 'DEM', 780154, 0), ('Hoefling', 'LFC', 1581, 0), ('Jacob', 'LTC', 749, 0), ('Johnson', 'LIB', 37978, 0), ('Keniston', 'VP', 1881, 0), ('Kennedy', 'SWP', 480, 0), ('Kotlikoff', 'IOC', 1048, 0), ('LaRiva', 'SLP', 446, 0), ('McMullin', 'CCS', 8547, 0), ('Stein', 'GRE', 14031, 0), ('Trump', 'REP', 1178638, 8), ('White', 'SEA', 370, 0)]}




