#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Project 6
# Due Date: 12/08/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

class Line: #Contructor of the Telephone line
	def __init__(self, name, area_code, number, is_active=True):
		self.name = name
		self.area_code = area_code
		self.number = number
		self.is_active = is_active
	def __str__(self):
		return (str(self.area_code)+"-"+str(self.number)+"("+self.name+")")
	def __repr__(self):
		return ("Line(\'"+self.name+"\', "+str(self.area_code)+", "+str(self.number)+")")
	def __eq__(self, other):
		x = 0
		if self.area_code == other.area_code:
			x += 1
		if self.number == other.number:
			x += 1
		if x == 2:
			return True
		else:
			return False
	def activate(self): #activates phone plans 
		self.is_active = True
		return None
	def deactivate(self): #deactivates phone plans
		self.is_active = False
		return None

class Call: #Set up the caller and callee, sets a line between two callers
	def __init__(self, caller, callee, length):
		if length < 0:
			raise CallError("negative call length: "+str(length))
		self.caller = caller
		self.callee = callee
		self.length = length
		if self.caller.is_active == False or self.callee.is_active == False:
			raise CallError("line "+str(self.caller.area_code)+"-"+str(self.callee.number)+"("+self.callee.name+") not active")
		if self.caller.area_code == self.callee.area_code and self.caller.number == self.callee.number:
			raise CallError("line "+str(self.caller.area_code)+"-"+str(self.caller.number)+"("+self.caller.name+") cannot call itself")
	def __str__(self):
		return ("Call("+repr(self.caller)+", "+repr(self.callee)+", 20)")
	def __repr__(self):
		return ("Call("+repr(self.caller)+", "+repr(self.callee)+", 20)")
	def is_local(self): #helps determine if the call is local between the caller and callee
		if self.caller.area_code == self.callee.area_code:
			return True
		return False

class CallError(Exception): #an exception handler for CallErrors in future classes
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		return ("CallError: "+self.msg)
	def __repr__(self):
		return ("CallError(\'"+self.msg+"\')")

class PhonePlanError(Exception): #an exception handler for PhonePlanErros in future classes
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return ("PhonePlanError: "+self.msg)
	def __repr__(self):
		return ("PhonePlanError(\'"+self.msg+"\')")
class PlanType: #used to determine what plan type the calls have
	def __init__(self, basic_rate, default_mins, rate_per_min, has_rollover=True):
		self.basic_rate = basic_rate
		self.default_mins = default_mins
		self.rate_per_min = rate_per_min
		self.has_rollover = has_rollover
	def __str__(self):
		return ("PlanType("+str(self.basic_rate)+"0, "+str(self.default_mins)+", "+str(self.rate_per_min)+"0, "+str(self.has_rollover)+")")
	def __repr__(self):
		return ("PlanType("+str(self.basic_rate)+"0, "+str(self.default_mins)+", "+str(self.rate_per_min)+"0, "+str(self.has_rollover)+")")

class PhonePlan: #contains a list of lines and calls, has multiple uses such making a call and paying balances
	def __init__(self, type, lines = None):
		self.type = type
		if lines == None:
			self.lines = []
		else:
			self.lines = lines
		self.calls = []
		self.balance = 0
		self.rollover_mins = 0
		self.mins_to_pay = 0
	def __str__(self):
		return ("PhonePlan("+repr(self.type)+", "+str(self.lines)+", "+str(self.calls)+")")
	def __repr__(self):
		return ("PhonePlan("+repr(self.type)+", "+str(self.lines)+", "+str(self.calls)+")")
	def activate_all(self):
		for i in self.lines:
			i.is_active = True
	def deactivate_all(self):
		for i in self.lines:
			i.is_active = False
	def add_call(self, call): #add a call to the calls list based on certain conditions
		s = 0
		for i in self.lines:
			if call.caller == i:
				s += 1
			elif call.callee == i:
				s += 1
		if s == 0:
			raise PhonePlanError("call cannot be added")
		if s == 2 or Call.is_local(call) == True:
			self.calls.append(call)
			return None
		else:
			self.mins_to_pay += call.length
			self.calls.append(call)
		return None
	def remove_call(self, call):
		if call in self.calls:
			self.calls.remove(call)
			return None
		else:
			raise PhonePlanError("no such call to remove")
	def add_calls(self, calls):
		s = 0
		for i in calls:
			try:
				self.add_call(i)
				s += 1
			except:
				continue
		return s
	def make_call(self, caller, callee, length): #make a call by setting up your own call variable and sending it to the add call method
		c = Call(caller, callee, length)
		try:
			self.add_call(c)
		except CallError:
			return False
		except PhonePlanError:
			return False
		return True
	def mins_by_line(self, line):
		s = 0
		if line in self.lines:
			for i in self.calls:
				if line == i.caller or line == i.callee:
					s += i.length
				continue
			return s
		else:
			return 0
	def calls_by_line(self, line):
		s = 0
		if line in self.lines:
			for i in self.calls:
				if line == i.caller or line == i.callee:
					s += 1
				continue
			return s
		else: 
			return 0
	def add_line(self, line):
		for i in self.lines:
			if Line.__eq__(i, line) == False:
				continue
			else:
				raise PhonePlanError("duplicated line to add")
		self.lines.append(line)
		return None
	def remove_line(self, line):
		if line in self.lines:
			self.lines.remove(line)
			i = 0 #to keep up with the iteration of the list
			while i < len(self.calls):
				if self.calls[i].caller in self.lines:
					i += 1
				elif self.calls[i].callee in self.lines:
					i += 1
				else:
					self.calls.remove(self.calls[i])
		else:
			raise PhonePlanError("no such line to remove")
	def calculate_bill(self): #used to calculate the total for a bill and update certain variable on certain conditions
		if self.mins_to_pay <= self.type.default_mins:
			self.balance = self.type.basic_rate
			if self.type.has_rollover == True:
				self.rollover_mins = self.type.default_mins - self.mins_to_pay
			else:
				self.rollover_mins = 0
			self.mins_to_pay = 0
		else:
			self.mins_to_pay = self.mins_to_pay - self.rollover_mins 
			if self.mins_to_pay <= self.type.default_mins:
				self.balance = self.type.basic_rate
				self.rollover_mins = self.type.default_mins - self.mins_to_pay
				self.mins_to_pay = 0
			else:
				self.balance = self.type.basic_rate + ((self.mins_to_pay - self.type.default_mins) * self.type.rate_per_min)
				self.rollover_mins = 0
				self.mins_to_pay = 0
		if self.balance > (4 * self.type.basic_rate):
			for i in self.lines:
				Line.deactivate(i)
		self.calls = []
		return None
	def pay_bill(self, amount = None): #used to pay the bill or alter the self.balance variable based on how much you need to pay
		if amount == None:
			if self.balance <= 0:
				return None
			else:
				self.balance -= self.balance
		elif amount < 0:
			raise ValueError("amount to pay cannot be negative")
		else:
			self.balance -= amount
			if self.balance <= (4 * self.type.basic_rate):
				for i in self.lines:
					Line.activate(i)
			else:
				return None




			












