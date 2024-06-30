import random
while True:
    print("Welcome to Rock, Paper, Scissors!")
    user = input("Enter action(rock/paper/scissors):")
    actions=["rock","paper","scissors"]
    comp=random.choice(actions)
    print("You chose",user, "\nComputer chose",comp)
    if (user==comp):
        print("It's a tie!")
    elif(user=="rock" and comp=="paper"):
        print("Paper wraps the rock! \nComputer wins")
    elif(user=="rock" and comp=="scissors"):
        print("Rock smashes scissors! \nUser wins")
    elif(user=="paper" and comp=="scissors"):
        print("Scissors cuts the paper! \nComputer wins")
    elif(user=="paper" and comp=="rock"):
        print("Paper wraps the rock! \nUser wins")
    elif(user=="scissors" and comp=="rock"):
        print("Rock smashes the scissors! \nComputer wins")
    else:
        print("Scissors cut the paper! \nComputer wins")
    
    play_again=input("Play again(yes/no): ")
    if(play_again=="no"):
        break

    print("Thanks for playing!")