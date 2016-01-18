#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# We could do the following on one line how?
# in_file = open(from_file)
# indata = in_file.read()

#indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL+C to abort."
#raw_input()

#out_file = open(to_file, 'w').write(indata)

#print "Alright, all done."

# Can't close these files as one The expression open(...).write(...) calls 
# the write method on the open file object but the open file object itself 
# is then discarded again after the expression completes. While the expression
# is executed only the stack is referencing it.
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# Study drill calls for this to be one line so here's an attempt guided by
# StackOverflow (I must be becoming a real programmer if taking examples from 
# there! :-P

from sys import argv; spt, fr, to = argv; open(to, 'w').write(open(fr).read())
