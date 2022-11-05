def play(player, computer):
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