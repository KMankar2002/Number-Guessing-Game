#Number Guessing Game

import random

a = int(input("Lower limit of the list is :\n"))
b = int(input("Upper limit of the list is :\n"))
no_of_chances = int(input("Enter no. of chances :\n"))
i = 0
count1 = 0
count2 = 0

while(i < 2):
    n = int(input("Enter 1 for player1 or 2 for player2 :\n"))

    if n == 1:
        random_num = random.randint(a, b)
        #print(random_num)
        while(count1 < no_of_chances):
            num = int(input("Enter a number you want to guess :\n"))
            if num > random_num:
                print("The number is greater")
            elif num < random_num:
                print("The number is smaller")
            else:
                print("The number is correctly guess")
                break
            count1 = count1 + 1
        print("No. of guesses taken by player1 is :", count1 + 1)

    else:
        random_num = random.randint(a, b)
        #print(random_num)
        while(count2 < no_of_chances):
            num = int(input("Enter a number you want to guess :\n"))
            if num > random_num:
                print("The number is greater")
            elif num < random_num:
                print("The number is smaller")
            else:
                print("The number is correctly guess")
                break
            count2 = count2+ 1
        print("No. of guesses taken by player2 is :", count2 + 1)
    i = i + 1

if count1 < count2:
    print("Player 1 is winner!")
elif count1 > count2:
    print("Player 2 is winner!")
else:
    print("Game is draw!")
