# Treasure Island Day 3
print('''888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P  d8P  Y8b    "88b88K     888  888888P  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 ''')

print("Welcome to treasure island!")
print("Your mission is to find the treasure. ")

cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
if cross_road.lower() == "left":
    lake = input('You come to a lake.  There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if lake.lower() == "wait":
        choose_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if choose_color.lower() == "yellow":
            print("Congratulations! You win the game! Thank you!")
        
        elif choose_color.lower() == "blue" or choose_color.lower() == "red":
            print("You enter a room of beast. Game Over")
        else:
            print("You chose a door that doesn't exist")
    else:
        print("Game Over")
else:
    print("Game Over")



