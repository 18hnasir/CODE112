#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 11
# Due Date: 11/26/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

class Grade:
	def __init__(self, kind, name, percent):
		if kind != "test" and kind != "lab" and kind != "project" and kind != "final":
			raise GradingError("no Grade kind " + "\'" + kind + "\'")
		else:
			self.kind = str(kind)
			self.name = str(name)
			self.percent = int(percent)
	def __str__(self):
		return (self.kind + ":" + self.name + "(" + str(self.percent) + "%)")
	def __repr__(self):
		return ("Grade(\'"+self.kind+"\', "+"\'"+self.name+"\', "+str(self.percent)+")")
	def __eq__ (self, other):
		return	self.kind==other.kind and self.name==other.name	and	self.percent==other.percent

class GradeBook:
	def __init__(self):
		self.grades = []
	def __str__(self):
		s = "GradeBook:\n"
		for i in self.grades:
			s += "	" + str(i) + "\n"
		return s
	def __repr__(self):
		return str(self)
	def add_grade(self, grade):
		self.grades.append(grade)
	def average_by_kind(self,kind):
		total = 0
		n = 0
		for i in self.grades:
			if i.kind == kind:
				total += i.percent
				n += 1
		if n != 0:
			return total/n
		else:
			return None
	def get_all_of(self, kind):
		l = []
		for i in self.grades:
			if i.kind == kind:
				l.append(i)
		return l
	def get_by_name(self, name):
		for i in self.grades:
			if i.name == name:
				return i
		raise GradingError("no Grade found named " + "\'" + name + "\'")
		

class GradingError(Exception):
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		return self.msg
	def __repr__(self):
		return ("GradingError('''" + self.msg + "''')")






