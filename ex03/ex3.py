print "I will now count my chickens:"

print "Hens", 25 + 30 / 6

# % and * have identical priority so do from left to right. - is lower priority so...
# 3 * 25 = 75 >>> 75 % 4 = 3 >>> 100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

print "I will now count the eggs:"

# 4 % 2 = 0 and 1 / 4 = 0 too because without a decimal place it's a non-floating point
# number so it only deals in whole numbers...
# 6 - 5 + 0 - 0 + 6 = 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6
print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater than or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
