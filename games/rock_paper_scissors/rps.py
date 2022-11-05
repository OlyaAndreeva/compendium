import random
from fun import play


items_list = ["rock","paper","scissors"]

while True:
    computer = random.choice(items_list)
    player = None
    while player not in items_list:
        player = input("enter your choice")

    print("computer choice is: ",computer)
    print("player choice is: ",player)

    play(player, computer)

    leave = input("you want to leave? ")
    if leave == "y":
        break