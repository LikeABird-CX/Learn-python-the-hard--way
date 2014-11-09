# coding: utf-8
def add (a, b):#加法函数
	print "ADDING %d + %d" % (a, b)
	return a + b#把a,b加起来，再把结果返回
	
def subtract(a, b):#减法函数
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b#把a,b相减，再把结果返回
	
def multiply(a, b):#乘法函数
	print "MULIPLYING %d * %d" % (a, b)
	return a * b#把a,b相乘，再把结果返回
	
def divide(a,b):#除法函数
	print "DIVIDING %d / %d" % (a, b)
	return a / b#把a,b相除，再把结果返回
	
	
print "Let's do some math with just functions!"

age = add(30, 5)#age=35
height = subtract(78, 4)#height=74
weight = multiply(90, 2)#weight=180
iq = divide(100, 2)#iq=50

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)



# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
#iq=50, iq/2=25, weight=180, multiply=180*25, height = 74, subtract =
#74 - 180 * 25, age = 35, add = 35 + 74 - 180 * 25 = -4391
#函数是自内而外开始运算的！
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
another_one = subtract(add(24,divide(34,100)),1023)

print "That becomes: ", what, "Can you do it by hand?"
print "That becomes: ", another_one, "Right?"
#输出自定义值： int(raw_input())整型值， float(raw_input())浮点值
