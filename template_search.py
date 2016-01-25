from sys import argv

filename = argv[1]
search = argv[2]
template = open(filename)

print "Searching %r..." % filename
for index, line in enumerate(template):
	if search in line : print index, line,

template.close()
