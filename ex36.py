from sys import argv

script, user_name = argv

print "Hello, Mr.%s, Welcome to 'Cops and robbers'." % user_name
print "Of course, you are a dangerous robber.Good luck!"
print "Let's play a interesting game."

i = 0
number = []
while i < 30:
	i = i + 1
	number.append(i)
			
	print "The number is:", number
	

		
def wharf():
	print "you get into the wharf and jump into a motorboat."
	print "You drive the motorboat and you runaway succeed."
	print "Lucky.Now you are safety.You count money happy."
	
	
	
		
def start():
	print "You drive a Toyota and there are some police cars behind you."
	print "You are in Road 36."
	print "There is a traffic light."
	print "Are you waiting for a moment or going on? "
	
	choice = raw_input("> ")
	
	if choice == "wait":
		emergency()
	elif choice == "go on":
		smart()
	else:
		print "Mistake. Please make your decision."
		start()
	
def smart():
	print "You're acting like a crazy guy."
	print "There is a crossroad, which one do you like best?"
	
	choice = raw_input("right, left or straight?")
	
	if choice == "left":
		emergency()
	elif choice == "right":
		print "The road is blocked.But there is a narrow road only walk."
		print "Hi, guy. There is a wharf!"
		wharf()
		
	elif choice == "straight":
		print "You are clever."
		print "You are still in Road 36."
		choose()
	else:
		print "Mistake.Please make your decision."
		smart()
		
def choose():
	print "An interesting game."
	print "There is a way to left or right. "
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		emergency()
	elif choice == "right":
		print "Hi, guy.There is a wharf!"
		wharf()
	else:
		print "Mistake.Please make your decision."
		choose()
		
def emergency():
	print "There are two polices are waiting for you."
	print "There are some police cars at the back."
	print "What should you do?"
	
	choice = raw_input("> ")
	
	if choice == "fight":
		dead()
	elif choice == "run":
		catch("There are six polices.You can't run away.")
	elif choice == "give up":
		catch()
	else:
		emergency()
		
def catch(what):
	print what, "You are catched."	
		
def dead():
	print "You are so brave and you die of polices' gun."
	print "The end."
		
start()
	





