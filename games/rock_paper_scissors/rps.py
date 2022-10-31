import random

items_list = ["rock","paper","scissors"]

while True:
    computer = random.choice(items_list)
    player = None
    while player not in items_list:
        player = input("enter your choice")

    print("computer choice is: ",computer)
    print("player choice is: ",player)

    if player == computer:
        print("it's a tie")
    elif player == "rock":
        if computer == "paper":
            print("computer wins")
        else:
            print("player wins")
    elif player == "paper":
        if computer == "rock":
            print("player wins")
        else:
            print("computer wins")
    else:
        if computer == "rock":
            print("computer wins")
        else:
            print("player wins")

    leave = input("you want to leave? ")
    if leave == "y":
        break