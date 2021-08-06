#Net ID: hnasir4
#GNumber: G01112406
#Lab Section: 218
# Name: <Hammadullah Nasir>
# G#: <G01112406>
# Lab 10
# Due Date: 11/12/18
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def get(xs, index, response = None):
    try:
        if xs[index] in xs:
            return xs[index]
    except:
        return response

def classify(input_string):
    numbers = []
    strings = []
    s = input_string.split()
    for i in s:
        try:
            numbers.append(int(i))
        except:
            strings.append(i)
    return (numbers, strings)

def shelve(inventory, product_list):
    for i in product_list:
        if i[0] in inventory:
            inventory[i[0]] = inventory[i[0]] + i[1]
            if inventory[i[0]] < 0:
                raise ValueError ("negative amount for %s" % (i[0]))
            continue
        else:
            inventory[i[0]] = i[1]
            if inventory[i[0]] < 0:
                raise ValueError ("negative amount for %s" % (i[0]))
            else:
                continue
    return None

