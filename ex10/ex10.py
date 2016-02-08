# \t mean a tab is inserted
tabby_cat ="\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat 
print backslash_cat
print fat_cat

# This is an annoying spinning star thing that never quits
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

# New code with format strings and escape characters

escape = '\nAh! \nhow \nmany \nnew \nlines \nin \nthis \nlist: %s'

print escape % ('\n\tLoads!\n\tAnd some more')

# Study drill code with double/single quotes and %s or %r

print 'Didn\'t you see %r, that\'s %r ' % ("Michael\'s tops", "crazy")
print 'Didn\'t you see %s, that\'s %s ' % ("Michael\'s tops", "crazy")