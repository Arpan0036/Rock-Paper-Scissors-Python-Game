import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,paper,scissors]
user_choice=int(input("User Choose the number!--- 0 for 'ROCK' 1 for 'PAPER' 2 for 'SCISSORS' :  "))

if user_choice >= 3 or user_choice < 0:
    print("You Choose invalid number!🤡 You lose!💔")
else:
    print("User Chose game Image: ⬇️⬇️⬇️⬇️")
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer Chose {computer_choice}")
    print("Computer chose game Image: ⬇️⬇️⬇️⬇️")
    print(game_images[computer_choice])
    if user_choice == computer_choice:
        print("It's a Draw! 🫱🏻‍🫲🏼 🙊")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! Rock crushes Scissors.💝🎆")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer win!💝🎆 You Lose!🤡 Rock crushes Scissors.")
    elif user_choice > computer_choice:
        print("You Win!💝🎆")
    elif computer_choice > user_choice:
        print("Computer Win!💝🎆 You Lose!🤡")
