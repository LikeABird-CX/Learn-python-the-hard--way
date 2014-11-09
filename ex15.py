# coding:utf-8
from sys import argv#从sys代码库中导入argv功能

script, filename = argv#定义argv的参数的个数，及参数变量

txt = open(filename)#open用来打开一个文件类型，open（name[, mode[, buffering]]） 
                    #把open打开并且读取的file object赋值给txt，  
print "Here's your file %r:" % filename#打印出argv的第一个参数，即文件名
print txt.read()#txt实际上是一个file类型， 所以调用file.read()方法
 
print "Type the filename again:"#打印一个字符串
file_again = raw_input("> ")#使用raw_input打印出提示符，把提示读取到的用户输入赋值给file_again
 
txt_again = open(file_again)#接下来还是调用open函数，及把读取到的file object类型付给txt_again
 
print txt_again.read()#调用file.read()方法，打印出txt_again中内容
