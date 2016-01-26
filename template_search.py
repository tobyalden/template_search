import re
from sys import argv

filename = argv[1]
search = argv[2]
template = open(filename)

filenames = []

print "Searching %r..." % filename
for index, line in enumerate(template):
	if search in line : print index, line,
	if 'extends' in line : 
		match = re.search('\"(.*?)\"|\'(.*?)\'', line)
		filenames.append(match.group(match.lastindex))

print(filenames)
template.close()
