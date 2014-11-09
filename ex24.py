# coding:utf-8
print 'let\'s practice everything.'
print 'you\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted 
connot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an wxplanation
\n\t\twhere there is none.
"""

print "-" * 14
print poem
print "-" * 14


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#Question:
#How come you call the variable jelly_beans but the name beans later?
#	That's part of how a function works. Remember that inside the function the variable is 
#temporary, and when you rerurn it then it can be assigned to a variable for later. I'm just 
#making a new variable named beans to hold the return value.
