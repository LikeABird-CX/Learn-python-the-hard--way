# coding:utf-8
# this one is like your scripts with argv
def print_two(*args):#*args的*是告诉python让它把所有的参数都接受进来，然后放到名字叫args的列表去
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
	
	
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("Frist!")
print_none()