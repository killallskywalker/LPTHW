from sys import argv

script , filename = argv

file = open(filename)
wordcount = {}

print "Here is your filename %s" %filename
if "skywalker" in open(filename).read(): #read to read word in file
	print "Yes the force is strong with this one"
else:
	print "Nope there is no force in this one"

file.close()