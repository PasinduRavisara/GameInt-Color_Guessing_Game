
#Creating and initializing variables

white = 1
blue = 2
red = 3
yellow = 4
green = 5
purple = 6
name = 0
x = 0
y = 0
random_number = 0
chances = 1
dig1 = 0
dig2 = 0
dig3 = 0
dig4 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
number_list = 0
ind = 0
end = "\n                         You have ended the game.\n                 Do you wish to play another game..Yes/No?"
z = end.center(70)
result = 0
score = 9

#Generate a random number
import random
random_number = random.sample(range(1,7),4)


#Input player's name
name=input("Please enter your name:")

#Creating manu
x="Hi " + name + " Welcome to GameInt"
y = x.center(77)
print("\n",y)
print(f"\n{'Number to Guess - X X X X'  :<30} {'Color Mapping:':>34}")
print("{0:>77}".format("1-White  2-Blue  3-Red"))
print("{0:>80}".format("4-Yellow 5-Green 6-Purple"))

#Give instructions to the player
print('''\nInstructions:-
    -There are 4 hidden pegs and you should guess their colours by entering the right number
    -The number you guess should have four digits
    -In the number you guess, each digit must be in the range of 1-6
    -Please remember to keep space between each digit when you enter the number you guess( Ex:-3 4 1 2 )
    -You have 8 attemps to guess the number
    -In the result, if it is correct number - correct position = 1, correct number - wrong position = 0 and wrong number - wrong position = '-'
    -If you want to end the game please enter - 0 0 0 0''')

# Add things to user interface
print(f"\n\n{'Attempt':>5} {'Guess':>36} {'Result':>29}")

#Input values
while(chances<=8):
    number_list=list(int(number_list)for number_list in input().strip().split())[:4]
    if number_list==[0, 0, 0, 0]:
        print("-"*78)
        print(z)
    else:
     if number_list[0]==random_number[0]:
        a1=1
     elif number_list[0]==random_number[1]:
        a1=0
     elif number_list[0]==random_number[2]:
        a1=0
     elif number_list[0]==random_number[3]:
        a1=0
     else:
        a1='-'
     if number_list[1]==random_number[0]:
        a2=0
     elif number_list[1]==random_number[1]:
        a2=1
     elif number_list[1]==random_number[2]:
        a2=0
     elif number_list[1]==random_number[3]:
        a2=0
     else:
        a2='-'
     if number_list[2]==random_number[0]:
        a3=0
     elif number_list[2]==random_number[1]:
        a3=0
     elif number_list[2]==random_number[2]:
        a3=1
     elif number_list[2]==random_number[3]:
        a3=0
     else:
        a3='-'
     if number_list[3]==random_number[0]:
        a4=0
     elif number_list[3]==random_number[1]:
        a4=0
     elif number_list[3]==random_number[2]:
        a4=0
     elif number_list[3]==random_number[3]:
        a4=1
     else:
        a4='-'
     result = [a1,a2,a3,a4]
     print(chances,("."*36),number_list,("."*14),result)
     chances=chances+1
     score = score-1
     print("-"*90)
     if result==[1,1,1,1]:
        print("\n             (: !!!!!!...Congratulations...!!!!!! :)\n                            You won... \n\n You have",score*12.5,"points.\n Do you want to play another round..Yes/No?")
print("\n                       You have run out of chances \n                 Do You want to play another game..Yes/No?")
    











    
