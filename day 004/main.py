import random

stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
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

list_game = ["stone" , "paper" , "scissors"]
game_image = [stone , paper , scissors]

user_selection = int(input("plz make selection:0=stone , 1=paper , 2=scissors"))

if user_selection<0 or user_selection>=3:
    print("plz choose number again ")
else:
    print(f"user selection is:{game_image[user_selection]}")
    computer_selection = random.randint(0,2)
    print(f"computer selection is:{game_image[computer_selection]}")

    if user_selection == computer_selection:
        print("game is draw,play again")
    
    elif (user_selection==0 and computer_selection==2) or (user_selection==1 and computer_selection==0) or (user_selection==2 and computer_selection==1):
        print("user is winner")
    else:
        print("computer is winner")    