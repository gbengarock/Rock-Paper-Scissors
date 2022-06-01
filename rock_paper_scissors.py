from random import randint

#moves for the playes
moves = ["rock","paper","scissors"]
while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or enter 'quit' to the game):  ")
    
    if player == "quit":
        print("the game has ended...")
        break

    elif player == computer:
        print("Tie!!")
    
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "beats", player)
        
        else:
            print("you win!", player, "beats", computer)

    elif player == "paper":
        if computer == "scissors": 
             print("you lose!", computer, "beats", player)
        
        else:
            print("you win!", player, "beats", computer)

    elif player == "scissors":
        if computer == "rock": 
             print("you lose!", computer, "beats", player)
        
        else:
            print("you win!", player, "beats", computer)
    
    else:
        print("given input is invalid...")