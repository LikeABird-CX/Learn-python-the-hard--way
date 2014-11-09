# coding:utf-8
## Animal is-a objeact (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		### 调用父类函数 hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")
	
## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and his salary is-a 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## Fish has-a flipper
flipper = Fish()

## Salmon has-a crouse
crouse = Salmon()

## Halibut has-a harry
harry = Halibut()
