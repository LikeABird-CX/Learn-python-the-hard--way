# coding: utf-8
from sys import argv#从sys导入argv功能

script, input_file = argv#定义argv参数，有两个，其中input_file需要给定

def print_all(f):#定义读取文件内容的函数
    print f.read()
	
def rewind(f):#定义一个返回文件开始的函数
    f.seek(0)#seek（0）处理的是字节，只是转到文件的0byte的位置

def print_a_line(line_count, f):#定义一个打印指定行号的内容函数，有两个参数，第一个参数韦行号，第二个参数为文件
    print line_count, f.readline()#返回文件中行的内容，保留换行符
	                              #readline()里边的代码会扫描文件的每一个字节，直到找到一个\n为止，
								  #然后它停止读取文件，并且返回此前的文件内容。文件f会记录每次调用
								  #readline()后的读取位置，这样它久可以在下次被调用时读取接下来的一行了
								  

current_file = open(input_file)

print "First let's print the whole file:";

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)#返回到文件的开始

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)