#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again.
import time

def quiz():
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "Which movie won the Oscar for Best Picture in 2020?",
            "options": ["A) Joker", "B) Parasite", "C) 1917", "D) Once Upon a Time in Hollywood"],
            "answer": "B"
        },
        {
            "question": "What does the 'print()' function do in Python?",
            "options": ["A) Takes user input", "B) Displays output", "C) Declares a variable", "D) Creates a loop"],
            "answer": "B"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A) James Cameron", "B) Christopher Nolan", "C) Steven Spielberg", "D) Quentin Tarantino"],
            "answer": "B"
        },
    ]

    score = 0

    print("\nWelcome to the Python & Movies Quiz! 🎬🐍")
    time.sleep(1)

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")
        time.sleep(1)

    print(f"\n🎉 Quiz Complete! Your final score: {score}/{len(questions)} 🎉")

while True:
    quiz()
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break
