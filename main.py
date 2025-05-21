import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Rock, Paper, Scissors")

userInput = int(input("0 = Rock, 1 = Paper, 2 = Scissors\n"))
compInput = random.randint(0,2)
image = [rock, paper, scissors]

if userInput>3 or userInput<0:
    print("Invalid Input")
else:
    print(f"You Chose:\n{image[userInput]}")
    print(f"Computer Chose:\n{image[compInput]}")


    if userInput == compInput:
        print("Draw")
    elif userInput==0 and compInput==2:
        print("You Win")
    elif userInput==2 and compInput==0:
        print("You Lose")
    elif userInput>compInput:
        print("You Win")
    elif userInput<compInput:
        print("You Lose")

