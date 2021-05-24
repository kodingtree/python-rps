import random
import time

# This file is made to play stone paper scissor with computer

time.sleep(1)
print("\nHello guys this is simple Stone Paper Scissor game.")
time.sleep(2)

print("\nI hope that you will like it.\n")

lst = ("Stone", "Paper", "Scissor")

var = random.choice(lst)


def starting():
    time.sleep(1)
    print ("[1]. Stone\n\n[2]. Paper\n\n[3]. Scissor")
    time.sleep(1)
    aa = int(input("\nEnter your choice\n"))
    time.sleep(2)
    if (aa == 1):

        print("\n\n\n\nYour choice is : Stone")

    elif (aa == 2):

        print("\n\n\n\nYour choice is : Paper")

    elif(aa == 3):

        print("\n\n\n\nYour choice is : Scissor")

    else:

        print("\n\n\n\nYou have entered a wrong number")

    time.sleep(3)

    print("The computer has choosed : ", var)

    time.sleep(2)

    print("\nPlease wait the match result is being caluclated")

    time.sleep(4)

    if(aa == 1 and var == "Paper"):

        print("Computer won the game\n")

    elif(aa == 1 and var == "Stone"):

        print("The game is draw\n")

    elif(aa == 2 and var == "Scissor"):

        print("Computer won the game\n")

    elif(aa == 2 and var == "Paper"):

        print("The game is draw\n")

    elif(aa == 3 and var == "Stone"):

        print("Computer won the game\n")

    elif(aa == 3 and var == "Scissor"):

        print("The game is draw\n")

    else:

        print("Congrats you win this game\n")

    return(var2())


# print("\nThe computer has choosed : ",var)my namw is shaikh rizwan ali jaa


def var2():

    time.sleep(2)

    print("I hope that you have enjoyed the game")

    time.sleep(3)

    print("\n\nWould You like to play again")

    time.sleep(1)

    bb = str(input("\nEnter Yes or No\n"))

    time.sleep(1)

    if(bb == "Yes" or bb == "YES" or bb == "yes"):

        print(starting())

    else:

        print("Thanks for using me ", exit())


'''def rizwan():

     

     if(aa==1 and var=="Paper"):

         print("Computer won the game\n")

     

     elif(aa==1 and var=="Stone"):

         print("The game is draw\n")

     

     elif(aa==2 and var=="Scissor"):

         print("Computer won the game\n")

 

     elif(aa==2 and var=="Paper"):

         print("The game is deaw\n")

    

     elif(aa==3 and var=="Stone"):

         print("Computer won the game\n")

    

     elif(aa==3 and var=="Scissor"):

         print("The game is draw\n")

 

     else:

         print("Congrats you win this game\n") 

 

     return(var2())'''


#print("You choosed",aa)

# print(rizwan())


# print(menu)

#aa = int(input("\nEnter your choice\n"))

print(starting())


#print("\nThe computer has choosed : ",var)

# print(rizwan())

# My name is Shaikh Rizwan ali. And I love to code. Currntly I am writing simple games and tools using Python. I have made one calculator that can Add, Subtract, Multiply the numbers. I have also masde one Stone Paper Scissor game.
