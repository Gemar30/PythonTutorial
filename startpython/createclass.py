# Class Construction
#class NewClass:

  #  def newFunc(self):
      #  return 'Python is fun!'
# Object Creation
#newObj = NewClass()

# Display the result
#print(newObj.newFunc())

# CREATE MORE OBJECTS
#class NewClass:
#    def NewHello(self):
#        return 'Hello from NewHello function'

# first object
#first_object = NewClass()
#print(first_object.NewHello())

# second object
#second_object = NewClass()
#print(second_object.NewHello())

# MULTI FUNCTIONS

''' class DoMath:

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y
    
    def multiplication(self, x, y):
        return x * y

#first object
first_object = DoMath()
print(first_object.addition(5,6))
print(first_object.subtraction(7,8))
print(first_object.multiplication(10,11)) 

# second object
second_object = DoMath()
print(second_object.addition(20,21))
print(second_object.subtraction(25,20))
print(second_object.multiplication(20,30)) '''

# INIT FUNCTION

# using __init__ method

''' class NewClass:

    def __init__(self):
        self.a = "Hello"
    
    def hi(self):
        return "hi there!"
    
#first object

first_object = NewClass()

# display the result
print(first_object.a)
print(first_object.hi()) '''

''' class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def newHi(self):
        print("Hi, My name is " + self.name)
    
    def newAge(self):
        print("My age is "+ str(self.age))

o1 = Player("Developer", 21)
o1.newHi()
o1.newAge() '''






        