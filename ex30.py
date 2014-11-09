# coding:utf-8
people = 30
cars = 40
trucks =15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
#问题1，elif和else是什么作用
#答：elif指第二种情况，else是指其他情况
#问题2，改变cars、people和trucks的数量，观察每一个if语句输出情况
#尝试使用一些像cars > people or trucks < cars复杂的布尔代数
#对每一句进行注释