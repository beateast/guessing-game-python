from ast import While


def numberguesing():
    num = 5
    
    chance = 0

    while chance < 5 :

        gues = input("Enter your any number")
    
        if num == gues:
         print("You have won the game")
         break
        

        if not chance < 5 :
          print("you lose the game")

numberguesing()