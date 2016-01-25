from sys import argv

filename = argv[1]

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
