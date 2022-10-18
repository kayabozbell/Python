import random as r

A = ["Rock", "Paper", "Scissors"]
a = "Devam"
while a == "Devam":
    computer_decision = A[r.randint(0, 2)]
    your_decision = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

    if your_decision == "0":
        print("Your decision is \"Rock\".")
        if computer_decision == "Rock":
            print("Computer decision is \"Rock\".\nDraw!")
        elif computer_decision == "Paper":
            print("Computer decision is \"Paper\".\nYou Lost!")
        elif computer_decision == "Scissors":
            print("Computer decision is \"Scissors\".\nYou Win!")
    elif your_decision == "1":
        print("Your decision is \"Paper\".")
        if computer_decision == "Rock":
            print("Computer decision is \"Rock\".\nYou win!")
        elif computer_decision == "Paper":
            print("Computer decision is \"Paper\".\nDraw!")
        elif computer_decision == "Scissors":
            print("Computer decision is \"Scissors\".\nYou Lost!")
    elif your_decision == "2":
        if computer_decision == "Rock":
            print("Computer decision is \"Rock\".\nYou Lost!!")
        elif computer_decision == "Paper":
            print("Computer decision is \"Paper\".\nYou Win!")
        elif computer_decision == "Scissors":
            print("Computer decision is \"Scissors\".\nDraw!")
    a = input("Devam etmek için \"Devam\" yazınız. ")


