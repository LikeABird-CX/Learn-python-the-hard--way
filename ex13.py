# coding: utf-8
from sys import argv#从python库中导入一个模组

script, first, second, third = argv#这句可以调出脚本的名字，并充当argv的第一个参数
#而不要你为它传递一个参数，而且第一个参数是必须的
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

