"""
Author: Robert Thomas Kohn
Date: November 2, 2026
Description: A simple quiz game that stores questions and answers in a dictionary,
evaluates player answers case-insensitively, tracks the score, and displays
win/game-over conditions and final results.
Code of honesty: I have not copied from any source without proper citation.
"""

# 1. Define quiz questions and answers in a dictionary
quiz = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare"
}

# Track score, total questions, and question counter
score = 0
total_questions = len(quiz)
question_number = 1

# 2. Iterate through each question, get player input, and check correctness
for question, correct_answer in quiz.items():
    print(f"Question {question_number}: {question}")
    user_answer = input("> ")

    # Compare answers ignoring case and surrounding whitespace
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

    question_number += 1

# 3. Check win condition and print appropriate message
if score == total_questions:
    print("Congratulations! You answered all the questions correctly!")
else:
    print("Game over. You didn't get all the questions right.")

# 4. Display final score
print(f"You got {score}/{total_questions} correct.")

# 5. Print concluding thank-you message
print("Thank you for playing the quiz game!")

