#Full rock paper sissor game

user_move = input("Enter your move = Rock , Paper , Scissor = ")

import random
moves = ["Rock", "Paper", "Scissor"]
com_move = random.choice(moves).capitalize()

print(f"Your Choice : {user_move} / Computer choice : {com_move}")

if com_move == user_move :
    print("the Match is Tied")
elif user_move == "Scissor" :
    if com_move == "Rock":
        print("Rock Breaks the Scissor : Computer Wins ")
    else : print("Scissor cuts the Paper : User Wins")
elif user_move == "Rock" :
    if com_move == "Scissor" :
        print("Rock breaks the Scissor : User Wins")          
    else : print("Paper covers the rock : Computer Wins")
elif user_move == "Paper" :
    if com_move == "Scissor" :
        print("Scissor cuts the paper : Computer Wins")        
    else : print("Paper covers the Rock : User Wins")    