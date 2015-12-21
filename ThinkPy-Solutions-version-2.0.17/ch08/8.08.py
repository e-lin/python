#
# Exercise 8
# Read the documentation of the string methods at
# http://docs.python.org/2/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you
# understand how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing.
# For example, in find(sub[, start[, end]]), the brackets indicate
# optional arguments. So sub is required, but start is optional,
# and if you include start, then end is optional.
#

# str.replace
name = "Peggy"
print name.replace('g','d',2)

#str.strip
print '   spacious   '.strip()
print 'www.example.com'.strip('cmowz.')

#str.lstrip
print '   spacious   '.lstrip()
print 'www.example.com'.lstrip('cmowz.')

#str.rstrip
print '   spacious   '.rstrip()
print 'mississippi'.rstrip('ipz')