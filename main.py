questions = [
    {
        "question": "What is the correct extension for a Python file?",
        "options": ["A. .java", "B. .py", "C. .html", "D. .cpp"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. list", "D. bool"],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. display()", "C. print()", "D. output()"],
        "answer": "C"
    }
]


def run_quiz():
    score = 0

    print("=" * 40)
    print("       PYTHON QUIZ APPLICATION")
    print("=" * 40)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"])

    print("\n" + "=" * 40)
    print("             QUIZ RESULT")
    print("=" * 40)

    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent Performance!")
    elif percentage >= 60:
        print("Good Performance!")
    elif percentage >= 40:
        print("Needs Improvement!")
    else:
        print("Keep Practicing!")


run_quiz()