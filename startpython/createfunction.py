# CREATE FUNCTIONS
#def hello_function():
#    print("Hello from this function!")

# function calling
#hello_function()
#hello_function()
#hello_function()

# ARGUMENTS
#def hello_function(name = "Gemar"):
 #   print("Hello " + name)
#hello_function('Ronaldo')
#hello_function('Messi')
#hello_function()

#PARALIST
#def foods(fruit):
#    for x in fruit:
#        print("This fruit is " + x)
#my_fruits = ["fig", "apple", "banana"]
#foods(my_fruits)

# RETURNING VALUE

def numbers(x):
    return 10 * x

print(numbers(5))
print(numbers(6))
print(numbers(7))

# KEY VALUE ARGS

#def fruits(fruit1, fruit2, fruit3):
#    print("The first fruit is " + fruit1)
#    print("The second fruit is " + fruit2)
#    print("The third fruit is " + fruit3)

#fruits(fruit1 = 'banana', fruit2 = 'apple', fruit3 = 'lemon')

# ARBITRARY ARG
def new_function(*fruits):
    print("The fruit is " + fruits[0])

new_function('banana','apple','fig')

# RECURSION

#def new_recursion(n):
#    if(n>0):
#        result = n + new_recursion(n-1)
#        print(result)
#    else:
#        result = 0
#    return result

#print("\n\n recursion results")
#new_recursion(8)

# LAMBDA FUNCTION
a = lambda x: x + 20
print(a(30))

# LAMBDA ARGS

store_lambda = lambda x, y : x * y
print(store_lambda(10,11))

store_args = lambda x, y, z : x + y + z
print(store_args(10,10,10))

# Anonymous Function
def new_multiplied(k):
   return lambda x: x * k

new_double = new_multiplied(2)
new_triple = new_multiplied(3)

print(new_double(2))
print(new_triple(12)) 

def showPerson(*args):        
    for i in args:        
        print(i) 
showPerson(name="Emma", age="25")