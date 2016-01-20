name = 'Josh Archer'
age = 30
height = 178 # centimetres 
weight = 92 # kilograms
eyes = 'hazel'
teeth = 'white'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d centimetres tall." % height
print "He weights %d kg." % weight
print "Actually that's not that heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are always %s as he doesn't drink coffee!" % teeth

# This line is tricky, try to get it exactly right.
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)

print "If you'd like the numbers in imperial, then lets see..."
# This uses one of the different format characters '%r', which prints exactly
# what you input.
print '''%r weights %r pounds, he's %r inches tall (and unfortunately for him) 
is still %r years old.''' % (name, weight * 2.2, height * 0.39370, age)
# Trying this with the new format() syntax
print '''{!r} weights {!r} pounds, he's {!r} inches tall (and unfortunately for him) 
is still {!r} years old.''' .format(name, weight * 2.2, height * 0.39370, age)