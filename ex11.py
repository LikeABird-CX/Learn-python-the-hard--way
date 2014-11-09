# coding: utf-8
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

raw_input_A = raw_input("raw_input: ")#可以接受任何类型的输入

input_A = input("Input: ")#只能接受Python合法的表达式，输入字符串时必须用引号括起来
raw_input_B = raw_input("raw_input: ")#type(raw_input_B)用来判断类型的

input_B = input("input: ")#type（input_B）


