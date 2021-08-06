def middle(a, b, c):
	if a < b < c:
		return b
	elif a < c > b:
		return a
	elif c > a < b:
		return c
	elif a > c > b:
		return c
	elif a > b > c:
		return b
	elif a == b == c:
		return a
	elif a == b and (b < c or b > c):
		return b
	elif b == c and (b < a or b > a):
		return b
	elif a == c and (a > b or a < b):
		return a

