def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some maths with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Study drill 3 alteration

print "Here's study drill 3 for you:"

study = add(age, multiply(weight, subtract(height, divide(iq, 2)))) 

print "Here's what we get when we switch the multiple and divide functions:", study 

# Study drill 4 alteration

print "Here's study drill 4 for you:"
print "First the new variables..."

knife = divide(20, 2)
fork = multiply(5, 4)
spoon = add(40, 20)
spork = subtract(230, 8)

print " And now lets do through the new puzzle..."

cutlery = subtract(spork, add(spoon, multiply(fork, divide(knife, 2))))

print "Here's the answer to study drill 4:", cutlery
