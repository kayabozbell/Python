print('''  
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    
''')



print("Welcome to Treasure Island.\n"
      "Your mission is to find the treasure.")
road = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if road == "right":
    print("You fell into a hole. Game over. ")
elif road == "left":
    choice1 = input("You came to a Lake. There is an island in the middle of the lake.Type \"wait\" to wait for a boat"
                    ".Type \"swim\" to swim across.\n")
    if choice1 == "swim":
        print("You got attacked by crocodile. Game over.")
    elif choice1 == "wait":
        choice2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                        "one blue. Which color do you choose ?\n")
        if choice2== "red":
            print("It is a room full of fire. Game over.")
        elif choice2=="yellow":
            print("You find the treasure! You win!")
        elif choice2=="blue":
            print("You enter a room of beasts. Game over.")