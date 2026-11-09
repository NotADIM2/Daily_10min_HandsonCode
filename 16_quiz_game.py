print("=====Python quiz Game=====")

questions={"Which language is used for python programming?":"Python",
           "what is 5+5?":"10",
           "Which keyword is used to define a function in Python?":"def",
           "Which function is used to get the length of a string in Python?":"len",
           "what symbol is used for comments in Python?":"#",
}
score=0
for question, answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer: ")
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print(f"\nYour final score is: {score}/{len(questions)}")
print("Thanks for playing the Python Quiz Game!")
print("Your score is:", score, "out of", len(questions))
if score == len(questions):
    print("Excellent! You got a perfect score!")
elif score >= len(questions) / 2:
    print("Good job! You scored above average.")
else:
    print("Better luck next time! Keep practicing.")