#-*- coding: utf-8 -*
formatter = "%r %r %r %r"#定义变量formatter

print formatter % (1, 2, 3, 4)#print "%r %r %r %r" % (1, 2, 3, 4)这段字符的缩写
print formatter % ("one", "two", "three", "four")#同上
print formatter % (True, False, False, True)#同上
print formatter % (formatter, formatter, formatter, formatter )#同上
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)#同上，用逗号不换行
#Why dodo have to put quotes around "one" but not around True or False?
#-That's because Python recognizes True and False as keywords representing the concept of true and false.
#-If you put quotes around them then they are turned into strings into strings and won't work right. 
#-You'll learn more about how these work in Exercise 27
