import random
print("========= Dice Roller ============")
while True:
    input("Press Enter to roll the dice")
    number=random.randint(1,6)
    print("You Rolled:",number)
    choice =input("Do you want to roll again? (y/n): ").lower()
    if choice == 'n':
        break
    elif choice != 'y':
        print("Invalid input. Please enter 'y' or 'n'.")
        break
print("Thanks for playing Dice Roller!")

