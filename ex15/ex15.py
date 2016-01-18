# Imports the argv (argument variable) module/library 
from sys import argv
# 'creates' two argument variables. It seems that if you use argv, you MUST use
# at least 1 argument variable for the name of you script in order for the 
# script to run properly, or more specifically you need to create two to allow
# the script to be the first arguement
script, filename = argv
# Sets variable 'txt' to function 'open()' which itself pulls in the filename
# arguement variable. This creates a 'file object' upon which further functions
# can be called. Basically 'txt' becomes a file object of the file provided
# in the argument variable. 
txt = open(filename)

print "Here's your file %r:" % filename
# NEW - .read() is a function/method applied to the variable 'txt'. From above 'txt'
# is the file object of the file provided in the argument variable. .read() is 
# simply an instruction to read the contents of the file. As this is used in 
# conjunction with 'print' function, the content are written to the screen. 
print txt.read()

# The below is the above repeated with alternative variable/file object names 
# instead of the file being provided via argument variable, it's provided 
# by the user via an input prompt after the script runs.
print "Type the filename again:"
file_again = raw_input(">>> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
