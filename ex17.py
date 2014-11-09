# coding:utf-8
from sys  import argv
from os.path import exists#将文件名字字符串作为参数，如果文件存在的话，返回True=

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = infile.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit TETURN to cntinue, CTRL -C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
