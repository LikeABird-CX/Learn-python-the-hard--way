# coding:utf-8
# 从sys中导入exit功能
from sys import exit

#定义一个函数gold_room
def gold_room():
	#打印一段字符串
	print "This room is full of gold. How much do you take?"
	
	#输入字符,并且赋值给choice
	choice = raw_input("> ")
	#if语句判断输入的字符串是否包含"0"和"1"
	if "0" in choice or "1" in choice:
		#将字符串转换为数值型，并赋值给how_much
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
	#内嵌if语句，判断how_much是否小于50
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		# exit the program
		exit(0)
	else:
		dead("You greedy bastard!")
	
# define another function:bear_room
def bear_room():
	# print some strings
	print "There is a bear here."
	print "The bear had a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	# while-loop
	while True:
		#input something
		choice = raw_input("> ")
		
		# if-statements,if you input "take honey",then...
		if choice == "take honey":
			# call dead function
			dead("The bear looks at you then slaps your face off.")
		# case 2: if you input "taunt bear",then...
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			
			bear_moved = True
		#case 2-1: if you input "taunt bear", then...
		elif choice == "taunt bear" and bear_moved:
			#call dead function
			dead("The bear gets pissed off and chews your leg off.")
		#case 2-2: if you input "open door", then...
		elif choice == "open door" and bear_moved:
			#call gold_room function
			gold_room()
		# case 3:
		else:
			print "I got no idea idea what that means."

# define another function:cthulhu_room 			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	# input,
	choice = raw_input("> ")
	
	#case 1: if you input "flee",then...
	if "flee" in choice:
		# call start() function 
		start()
	#case 2: if you input "head", then
	elif "head" in choice:
		# call dead function
		dead("Well that was tasty!")
	# case 3:
	else:
		# call cthulhu_room function again
		cthulhu_room()
		
# define another function: dead()
def dead(why):
	print why, "Good job!"
	# exit the program
	exit(0)

# define another function: start()
def start():
	print "You are in a dark room."
	print "There is door to your right and left."
	print "Which one do you take?"
	# input,
	choice = raw_input("> ")
	
	# case 1: if you choose left, then...
	if choice == "left":
		# call function: bear_room()
		bear_room()
	# case 2: if you choose right, then...
	elif choice == "right":
		# call function: cthulhu_room()
		cthulhu_room()
	# case 3:
	else:
		#call function dead()
		dead("You stumble around the room until you starve.")
		
start()
# Quenstion: What does exit() do?
# Answer: On many operating systems a program can abort with exit(0), and the 
#		  number passed in will indicate an error or not. If you do exit(1) then 
#		  it will be an error, but exit(0) will be a good exit. the reason it's 
#		  backward from normal boolean logic (with 0==False is that you can use
#         different numbers to indicate different error results. You can do 
#		  exit(100)for a different error result than exit(2) or exit(1).