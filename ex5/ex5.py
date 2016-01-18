my_name = 'Josh Archer'
my_age = 30
my_height = 178 # centimetres 
my_weight = 92 # kilograms
my_eyes = 'hazel'
my_teeth = 'white'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d centimetres tall." % my_height
print "He weights %d kg." % my_weight
print "Actually that's not that heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are always %s as he doesn't drink coffee!" % my_teeth

# This line is ticky, try to get it exactly right.
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "If you'd like the numbers in imperial, then lets see..."
print "%r weights %r pounds, he's %r inches tall (and unfortunately for him) is still %r years old." % (my_name, my_weight * 2.2, my_height * 0.39370, my_age)
