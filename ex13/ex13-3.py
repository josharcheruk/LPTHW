from sys import argv

script, car, food, country = argv

car = raw_input("What is your favorite color? ")
food = raw_input("What is your favorite number? ")
country = raw_input("What is your favorite shape? ")

print """
This program is called %s and it's going to ask you some
questions about your favourite things.
""" % script

print "Your favorite car is a:", car
print "Your favorite food is:", food
print "Your favorite country is:", country