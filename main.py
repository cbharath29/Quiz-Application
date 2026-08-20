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
    },
    {
        "question": "Which function is used to take input from the user?",
        "options": ["A. scan()", "B. input()", "C. get()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which collection is ordered and changeable in Python?",
        "options": ["A. Tuple", "B. List", "C. Set", "D. FrozenSet"],
        "answer": "B"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C"
    },
    {
        "question": "Which brackets are used to create a tuple?",
        "options": ["A. []", "B. {}", "C. ()", "D. <>"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. **", "C. //", "D. %%"],
        "answer": "B"
    },
    {
        "question": "What is the output of 10 // 3 in Python?",
        "options": ["A. 3", "B. 3.33", "C. 1", "D. 4"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a loop over a sequence?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to check a condition?",
        "options": ["A. if", "B. check", "C. when", "D. condition"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used when the condition is false?",
        "options": ["A. otherwise", "B. else", "C. false", "D. default"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to exit a loop?",
        "options": ["A. stop", "B. exit", "C. break", "D. close"],
        "answer": "C"
    },
    {
        "question": "Which keyword skips the current iteration of a loop?",
        "options": ["A. skip", "B. continue", "C. pass", "D. next"],
        "answer": "B"
    },
    {
        "question": "Which method adds an element to the end of a list?",
        "options": ["A. add()", "B. insert()", "C. append()", "D. push()"],
        "answer": "C"
    },
    {
        "question": "Which function returns the length of a list?",
        "options": ["A. size()", "B. length()", "C. count()", "D. len()"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to import a module in Python?",
        "options": ["A. include", "B. import", "C. require", "D. using"],
        "answer": "B"
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