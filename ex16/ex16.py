from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want to do that, hit CTRL+c (^c.)"
print "If you do want to do that, hit RETURN."

raw_input("Hit 'RETURN' to continue, ctrl+c to cancel...")

print "Opening the file..."
# 'w' is an arguement that puts open() into write mode. It opens by default to 
# read mode so to allow right later, you need to set the write flag when you 
# actually open the file object. A file object with 'w' can't be written to.
# CAUTION - using 'w' will truncate the file if it already exists!!
target = open(filename, 'w')
# Truncate basically deletes the contents of the file, be careful!


print "Truncating the file. Goodbye!"
# The following line is not necessary, opening the file with the 'w' argument
# will truncate the file anyway if the file exists, and if it doesn't then it
# would be blank anyway.
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these lines to the file."

# See the following StackOverflow for more info on why the method below is the 
# correct one to take to solve this problem
# The quick answer is use %s as it doesn't add quotes, you need '' around the 
# first bit as \n has no meaning outside a string and you wrap the whole thing
# inside the target.write() brackets or you'll try and execute it outside of
# the write method - so it will do nothing as write has 'finished'
# http://stackoverflow.com/questions/8691311/python-how-to-write-multiple-strings-in-one-line

target.write('%s\n%s\n%s\n' % (line1, line2, line3))

print "And finally, we'll close it."
target.close()
