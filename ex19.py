# coding: utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):#定义一个函数，函数中有两个参数
   print "You have %d cheeses!" % cheese_count#打印第一个参数值
   print "You have %d boxes of crackers!" % boxes_of_crackers#打印第二个参数值
   print "Man that's enough for a party!"
   print "Get a blanket. \n"#打印一个字符串并换行
   
   
print "We can just give the function numbers directly:"#打印提示语
cheese_and_crackers(20, 30) #调用函数，并直接给定两个参数的值


print "OR, we can use variables from our script:"#打印提示语
amount_of_cheese = 10#定义两个变量，并赋值，尽量采用与函数参数不一样的名字
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)#函数的参数可以是表达式


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)#函数的参数可以是变量表达式
