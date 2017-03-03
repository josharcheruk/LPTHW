from sys import argv
# Add the 'title' argument to argv
script, user_name, title = argv
# This make a variable called 'prompt' which we set to what we want. Then, when
# inside the raw_input() function, we insert the variable to output whatever 
# prompt is set to. So the prompt will be >  with a space. You can shange all 
# prompts in one place using this method. 

# Add couple extra right angle brackets to prompt

prompt = '>>> '

# Add extra agrv variable to various areas (for study drills)

print "Hi %s (%s), I'm the %s script." % (user_name, title, script)
print "I'd like to ask you a few questions."
print "Do you like me %s (%s)?" % (user_name, title)
likes = raw_input(prompt)

print "Where do you live %s (%s)?" % (user_name, title)
lives = raw_input(prompt)

print "What kind of computer do you have %s (%s)?" % (user_name, title)
computer = raw_input(prompt)

print """
Alright, so you have said %r about liking me.
You live in %r (not sure where that is).
And you have a %r computer. Nice.
""" % (likes, lives, computer)
