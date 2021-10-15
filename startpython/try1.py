''' try:
    print(a)
except NameError:
    print("Variable a is not defined")
except:
    print('This is an exception')'''


''' try:
    print("Hello")
except:
    print("An error or something went wrong")
else:
    print("Everything is good and nothing went wrong")'''


'''try:
    print("Hello")
except:
    print("An error or something went wrong!")
finally:
   print ("Exception handling is completed")'''

# RAISING EXCEPTION

''' a = -3

if a < 0:
    raise Exception("Sorry, no numbers below zero here!")'''

a = "Hello"

if not type(a) is int:
    raise TypeError("Only integer numbers are allowed here!")