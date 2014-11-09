#-*- coding: utf-8 -*
x = "There are %d types of people." % 10 #定义变量x为
binary = "binary"#定义变量binary为
do_not = "don't"#定义变量do_not为
y = "Those who know %s and those who %s." % (binary, do_not)#定义变量y为

print x #打印变量x
print y #打印变量y

print "I said: %r." % x#打印含有变量x的格式化字符的字符串
print "I also said: '%s'." % y#打印含有变量y的格式化的字符串

hilarious = False  #定义hilarious为false
joke_evaluation = "Isn't that joke so funny?! %r" #定义joke_evaluation 为一段字符串

print joke_evaluation % hilarious# 打印含有变量hilarious的格式化字符的字符串

w = "This is the left side of..." #定义w为一串字符串
e = "a string with a right side." #定义e为一串字符串

print w + e #打印w + e的更长的字符串
