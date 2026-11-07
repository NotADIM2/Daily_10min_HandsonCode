import random
print("========= Rock Paper Scissor ============")
print("-------Play The Game <--------->")
choices=["rock","paper","scissors"]
computer=random.choice(choices)
user=input("Enter your choices Rock,Paper or Scissors : -->").lower()
print("Your Choice:",user)
print("Computer choice:",computer)
if user not in choices:print("You have entered an invalid choice")
elif user ==computer:
    print("It is a tie")
elif user=="rock" and computer=="scissor" :print("You win!")
elif user=="paper" and computer=="rock"   :print("You win !")
elif user=="scissor" and computer=="paper" :print("You win")

else:
     print("You lose !!")