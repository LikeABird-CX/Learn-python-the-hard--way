# coding:utf-8
from ex25 import *
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

#five = 10 - 2 + 3 - 5
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    #jars = jelly_beans \ 1000
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
#print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#start_point = start_point / 10
start_anther_point = start_point / 10

print "We can also do that this way:"
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_anther_point)

#sentence = "All god\tthings come to those who weight."
sentence = "All good things come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
#prin sorted_words
print sorted_words

#print_irst_and_last(sentence)
print_first_and_last(sentence)

#print_first_a_last_sorted(senence)
print_first_and_last_sorted(sentence)