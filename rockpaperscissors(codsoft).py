import random
print("\t\t\t***WELCOME TO THE GAME***\n")
select=str(input("Do you want to continue game : "))
if select=="yes":
    print("loading the game ....")
    game=["rock","paper","scissors"]
    #players names
    playerName=str(input("Enter your name : "))
    #displaying players names
    print("Player1 : ",playerName)
    print("Player2 : computer")
    #players choosing their option
    playerOption=str(input("Enter your option : "))
    computerOption=random.choice(game)
    print("\nPlayer1 choosed : ",playerOption)
    print("Computer choosed : ",computerOption)
    #calculating results
    if playerOption==computerOption:
        print("It's a tie")
    elif playerOption=="rock" and computerOption=="paper":
        print("\n\tComputer wins")
    elif playerOption=="rock" and computerOption=="scissors":
        print("\n\t",playerName,"wins")
    elif playerOption=="paper" and computerOption=="rock":
        print("\n\t",playerName,"wins")
    elif playerOption=="paper" and computerOption=="scissors":
        print("\n\tComputer wins")
    elif playerOption=="scissors" and computerOption=="rock":
        print("\n\tComputer wins")
    elif playerOption=="scissors" and computerOption=="paper":
        print("\n\t",playerName,"wins")
    else:
        print("Error")
else:
    print("Closing the game")
    
