from sys import argv

eat, food, echo, tree = argv

print "The script is called:", eat
print "Your first variable is called:", food
print "Your second variable is called:", echo
print "Your third variable is called:", tree

raw_input(food)
print "You like to eat: %s" % food
