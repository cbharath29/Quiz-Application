import random
import os
import time
import msvcrt
from datetime import datetime


# ==========================================================
# COLORS
# ==========================================================

RESET = "\033[0m"
BOLD = "\033[1m"

BLACK = "\033[30m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

BG_BLUE = "\033[44m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_CYAN = "\033[46m"


# ==========================================================
# SETTINGS
# ==========================================================

# Change this to 8 if you want exactly 8 seconds.
TIMER_SECONDS = 10

HIGH_SCORE_FILE = "highscore.txt"
HISTORY_FILE = "history.txt"


# ==========================================================
# QUESTIONS
# ==========================================================

questions = [

    {
        "question": "What is the correct extension for a Python file?",
        "options": [".java", ".py", ".html", ".cpp"],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    },

    {
        "question": "Which data type is used to store True or False?",
        "options": ["int", "str", "list", "bool"],
        "answer": "D"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "B"
    },

    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "print()", "output()"],
        "answer": "C"
    },

    {
        "question": "Which function is used to take input from the user?",
        "options": ["scan()", "input()", "get()", "read()"],
        "answer": "B"
    },

    {
        "question": "Which data type is used to store a sequence of characters?",
        "options": ["int", "float", "str", "bool"],
        "answer": "C"
    },

    {
        "question": "Which collection is ordered and changeable in Python?",
        "options": ["Tuple", "List", "Set", "FrozenSet"],
        "answer": "B"
    },

    {
        "question": "Which brackets are used to create a list?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": "C"
    },

    {
        "question": "Which brackets are used to create a tuple?",
        "options": ["[]", "{}", "()", "<>"],
        "answer": "C"
    },

    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "//", "%%"],
        "answer": "B"
    },

    {
        "question": "What is the output of 10 // 3 in Python?",
        "options": ["3", "3.33", "1", "4"],
        "answer": "A"
    },

    {
        "question": "Which keyword is used to create a loop over a sequence?",
        "options": ["repeat", "loop", "for", "iterate"],
        "answer": "C"
    },

    {
        "question": "Which keyword is used to check a condition?",
        "options": ["if", "check", "when", "condition"],
        "answer": "A"
    },

    {
        "question": "Which keyword is used when the condition is false?",
        "options": ["otherwise", "else", "false", "default"],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to exit a loop?",
        "options": ["stop", "exit", "break", "close"],
        "answer": "C"
    },

    {
        "question": "Which keyword skips the current iteration of a loop?",
        "options": ["skip", "continue", "pass", "next"],
        "answer": "B"
    },

    {
        "question": "Which method adds an element to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "C"
    },

    {
        "question": "Which function returns the length of a list?",
        "options": ["size()", "length()", "count()", "len()"],
        "answer": "D"
    },

    {
        "question": "Which keyword is used to import a module in Python?",
        "options": ["include", "import", "require", "using"],
        "answer": "B"
    }
]


# ==========================================================
# CLEAR SCREEN
# ==========================================================

def clear_screen():
    os.system("cls")


# ==========================================================
# DESIGN FUNCTIONS
# ==========================================================

def line():
    print(f"{CYAN}{'━' * 68}{RESET}")


def small_line():
    print(f"{BLUE}{'─' * 68}{RESET}")


def title(text):

    print()

    print(
        f"{BG_BLUE}{WHITE}{BOLD}"
        f"{' ' * 68}"
        f"{RESET}"
    )

    print(
        f"{BG_BLUE}{WHITE}{BOLD}"
        f"{text:^68}"
        f"{RESET}"
    )

    print(
        f"{BG_BLUE}{WHITE}{BOLD}"
        f"{' ' * 68}"
        f"{RESET}"
    )

    print()


# ==========================================================
# PROGRESS BAR
# ==========================================================

def progress_bar(current, total):

    percentage = int((current / total) * 100)

    length = 32

    filled = int((percentage / 100) * length)

    empty = length - filled

    bar = (
        f"{GREEN}{'█' * filled}"
        f"{BLUE}{'░' * empty}"
        f"{RESET}"
    )

    print(
        f"Progress  {bar} "
        f"{WHITE}{percentage}%{RESET}"
    )


# ==========================================================
# TIMER BAR
# ==========================================================

def timer_bar(seconds_left):

    total = TIMER_SECONDS
    length = 20

    filled = int(
        (seconds_left / total) * length
    )

    empty = length - filled

    if seconds_left <= 3:
        color = RED

    elif seconds_left <= 5:
        color = YELLOW

    else:
        color = GREEN

    bar = (
        f"{color}{'█' * filled}"
        f"{BLUE}{'░' * empty}"
        f"{RESET}"
    )

    return (
        f"  TIME  {bar} "
        f"{color}{seconds_left:02d}s{RESET}"
    )


# ==========================================================
# GET ANSWER WITH TIMER
# ==========================================================

def get_answer():

    start_time = time.time()

    # Display timer for the first time
    print(
        timer_bar(TIMER_SECONDS),
        end="",
        flush=True
    )

    while True:

        elapsed = time.time() - start_time

        remaining = (
            TIMER_SECONDS - int(elapsed)
        )

        if remaining < 0:
            remaining = 0

        # Update the same timer line
        print(
            f"\r\033[K"
            f"{timer_bar(remaining)}",
            end="",
            flush=True
        )

        # Check keyboard input
        if msvcrt.kbhit():

            key = msvcrt.getch().decode(
                errors="ignore"
            ).upper()

            if key in ["A", "B", "C", "D"]:

                print()

                return key

        # Time expired
        if remaining == 0:

            print()

            return None

        time.sleep(0.1)


# ==========================================================
# HIGH SCORE
# ==========================================================

def get_high_score():

    if not os.path.exists(HIGH_SCORE_FILE):
        return 0

    try:

        with open(
            HIGH_SCORE_FILE,
            "r"
        ) as file:

            return int(file.read())

    except:

        return 0


def save_high_score(score):

    old_score = get_high_score()

    if score > old_score:

        with open(
            HIGH_SCORE_FILE,
            "w"
        ) as file:

            file.write(str(score))

        return True

    return False


# ==========================================================
# QUIZ HISTORY
# ==========================================================

def save_history(
    score,
    total,
    percentage,
    grade
):

    date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        HISTORY_FILE,
        "a"
    ) as file:

        file.write(
            f"{date} | "
            f"Score: {score}/{total} | "
            f"Percentage: {percentage:.1f}% | "
            f"Grade: {grade}\n"
        )


def show_history():

    clear_screen()

    title("📜  QUIZ HISTORY")

    if not os.path.exists(HISTORY_FILE):

        print(
            f"{YELLOW}"
            f"No quiz history available."
            f"{RESET}"
        )

    else:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            records = file.readlines()

        if not records:

            print(
                f"{YELLOW}"
                f"No quiz history available."
                f"{RESET}"
            )

        else:

            for record in records:

                print(
                    f"{WHITE}"
                    f"• {record.strip()}"
                    f"{RESET}"
                )

    print()

    input(
        f"{YELLOW}"
        f"Press Enter to return..."
        f"{RESET}"
    )


# ==========================================================
# INSTRUCTIONS
# ==========================================================

def instructions():

    clear_screen()

    title("📖  HOW TO PLAY")

    print(
        f"{WHITE}"
        f"  • The quiz contains 20 Python questions.\n"
        f"  • Each question has four options.\n"
        f"  • You have {TIMER_SECONDS} seconds per question.\n"
        f"  • Press A, B, C or D directly.\n"
        f"  • You do NOT need to press Enter.\n"
        f"  • Your score is hidden during the quiz.\n"
        f"  • Your final score is displayed at the end.\n"
        f"  • Questions are presented randomly.\n"
        f"  • Your highest score is automatically saved.\n"
        f"  • Your quiz history is stored automatically.\n"
        f"{RESET}"
    )

    print()

    input(
        f"{YELLOW}"
        f"Press Enter to return..."
        f"{RESET}"
    )


# ==========================================================
# GRADE
# ==========================================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# ==========================================================
# PERFORMANCE
# ==========================================================

def performance_message(percentage):

    if percentage >= 90:

        return "Outstanding Performance!"

    elif percentage >= 80:

        return "Excellent Performance!"

    elif percentage >= 70:

        return "Great Job!"

    elif percentage >= 60:

        return "Good Effort!"

    else:

        return "Keep Practicing!"


# ==========================================================
# START QUIZ
# ==========================================================

def start_quiz():

    clear_screen()

    title("🧠  PYTHON QUIZ")

    print(
        f"{WHITE}"
        f"  Welcome to the Python Challenge!"
        f"{RESET}"
    )

    print()

    print(
        f"{CYAN}"
        f"  Select your answer using A / B / C / D."
        f"{RESET}"
    )

    print(
        f"{YELLOW}"
        f"  You have {TIMER_SECONDS} seconds per question."
        f"{RESET}"
    )

    print()

    input(
        f"{GREEN}"
        f"  Press Enter to begin..."
        f"{RESET}"
    )

    # Copy questions
    quiz_questions = questions.copy()

    # Randomize
    random.shuffle(
        quiz_questions
    )

    score = 0

    total = len(
        quiz_questions
    )

    # ======================================================
    # QUESTIONS LOOP
    # ======================================================

    for number, question in enumerate(
        quiz_questions,
        start=1
    ):

        clear_screen()

        title(
            f"QUESTION  {number:02d}  /  {total:02d}"
        )

        progress_bar(
            number,
            total
        )

        print()

        # Question heading
        print(
            f"{BG_CYAN}{BLACK}{BOLD}"
            f"  QUESTION"
            f"{RESET}"
        )

        print()

        # Question text
        print(
            f"{WHITE}{BOLD}"
            f"  {question['question']}"
            f"{RESET}"
        )

        print()

        small_line()

        print()

        # Options
        letters = [
            "A",
            "B",
            "C",
            "D"
        ]

        for letter, option in zip(
            letters,
            question["options"]
        ):

            print(
                f"  {CYAN}{BOLD}"
                f"[ {letter} ]"
                f"{RESET}"
                f"  {WHITE}{option}{RESET}"
            )

            print()

        small_line()

        print()

        # Instruction
        print(
            f"{YELLOW}"
            f"  Select your answer: "
            f"{WHITE}[ A / B / C / D ]"
            f"{RESET}"
        )

        print()

        # Timer
        user_answer = get_answer()

        print()

        # ==================================================
        # ANSWER RESULT
        # ==================================================

        if user_answer is None:

            print(
                f"{BG_RED}{WHITE}{BOLD}"
                f"  ⏰  TIME'S UP!  "
                f"{RESET}"
            )

            correct = question["answer"]

            correct_index = (
                ord(correct) - ord("A")
            )

            correct_option = (
                question["options"][
                    correct_index
                ]
            )

            print()

            print(
                f"{YELLOW}"
                f"  Correct Answer: "
                f"{correct} - {correct_option}"
                f"{RESET}"
            )

        elif user_answer == question["answer"]:

            score += 1

            print(
                f"{BG_GREEN}{BLACK}{BOLD}"
                f"  ✓  CORRECT  "
                f"{RESET}"
            )

        else:

            correct = question["answer"]

            correct_index = (
                ord(correct) - ord("A")
            )

            correct_option = (
                question["options"][
                    correct_index
                ]
            )

            print(
                f"{BG_RED}{WHITE}{BOLD}"
                f"  ✗  INCORRECT  "
                f"{RESET}"
            )

            print()

            print(
                f"{YELLOW}"
                f"  Correct Answer: "
                f"{correct} - {correct_option}"
                f"{RESET}"
            )

        # Small delay before next question
        time.sleep(1.5)

    # ======================================================
    # FINAL RESULT
    # ======================================================

    clear_screen()

    percentage = (
        score / total
    ) * 100

    grade = calculate_grade(
        percentage
    )

    new_high_score = save_high_score(
        score
    )

    save_history(
        score,
        total,
        percentage,
        grade
    )

    title("🏆  QUIZ COMPLETED")

    print()

    print(
        f"{CYAN}"
        f"{'─' * 50}"
        f"{RESET}"
    )

    print(
        f"  Total Questions     : "
        f"{WHITE}{total}{RESET}"
    )

    print(
        f"  Correct Answers     : "
        f"{GREEN}{score}{RESET}"
    )

    print(
        f"  Wrong Answers       : "
        f"{RED}{total - score}{RESET}"
    )

    print(
        f"  Final Score         : "
        f"{CYAN}{score} / {total}{RESET}"
    )

    print(
        f"  Percentage          : "
        f"{CYAN}{percentage:.1f}%{RESET}"
    )

    print(
        f"  Grade               : "
        f"{GREEN}{grade}{RESET}"
    )

    print(
        f"{CYAN}"
        f"{'─' * 50}"
        f"{RESET}"
    )

    print()

    # Performance
    if percentage >= 90:

        print(
            f"{BG_GREEN}{BLACK}{BOLD}"
            f"  ⭐ {performance_message(percentage)}  "
            f"{RESET}"
        )

    elif percentage >= 70:

        print(
            f"{BG_CYAN}{BLACK}{BOLD}"
            f"  ⭐ {performance_message(percentage)}  "
            f"{RESET}"
        )

    else:

        print(
            f"{BG_BLUE}{WHITE}{BOLD}"
            f"  📚 {performance_message(percentage)}  "
            f"{RESET}"
        )

    # High score
    if new_high_score:

        print()

        print(
            f"{YELLOW}{BOLD}"
            f"  🎉 NEW HIGH SCORE!"
            f"{RESET}"
        )

    else:

        print()

        print(
            f"  🏆 High Score: "
            f"{YELLOW}"
            f"{get_high_score()}"
            f"{RESET}"
        )

    print()

    line()

    print()

    # Next action
    choice = input(
        f"{CYAN}"
        f"  [R] Play Again     "
        f"[M] Main Menu     "
        f"[E] Exit\n\n"
        f"  Choose an option: "
        f"{RESET}"
    ).strip().upper()

    if choice == "R":

        start_quiz()

    elif choice == "M":

        main_menu()

    else:

        exit_program()


# ==========================================================
# EXIT
# ==========================================================

def exit_program():

    clear_screen()

    title("👋  THANK YOU")

    print(
        f"{CYAN}"
        f"  Thanks for playing the Python Quiz!"
        f"{RESET}"
    )

    print()

    print(
        f"{GREEN}"
        f"  Keep learning. Keep coding. 🚀"
        f"{RESET}"
    )

    print()


# ==========================================================
# MAIN MENU
# ==========================================================

def main_menu():

    while True:

        clear_screen()

        title(
            "🧠  PYTHON QUIZ APPLICATION"
        )

        print(
            f"{WHITE}"
            f"  Test your Python knowledge."
            f"{RESET}"
        )

        print()

        line()

        print()

        print(
            f"  {GREEN}{BOLD}[1]{RESET}  "
            f"Start Quiz"
        )

        print()

        print(
            f"  {BLUE}{BOLD}[2]{RESET}  "
            f"Instructions"
        )

        print()

        print(
            f"  {YELLOW}{BOLD}[3]{RESET}  "
            f"View High Score"
        )

        print()

        print(
            f"  {MAGENTA}{BOLD}[4]{RESET}  "
            f"Quiz History"
        )

        print()

        print(
            f"  {RED}{BOLD}[5]{RESET}  "
            f"Exit"
        )

        print()

        line()

        print()

        choice = input(
            f"{CYAN}"
            f"  Select an option [1-5]: "
            f"{RESET}"
        ).strip()

        if choice == "1":

            start_quiz()

        elif choice == "2":

            instructions()

        elif choice == "3":

            clear_screen()

            title("🏆  HIGH SCORE")

            print()

            print(
                f"  Highest Score: "
                f"{YELLOW}"
                f"{get_high_score()}"
                f"{RESET} / {len(questions)}"
            )

            print()

            input(
                f"{YELLOW}"
                f"  Press Enter to return..."
                f"{RESET}"
            )

        elif choice == "4":

            show_history()

        elif choice == "5":

            exit_program()

            break

        else:

            print()

            print(
                f"{RED}"
                f"  Invalid option. Please choose 1-5."
                f"{RESET}"
            )

            time.sleep(1.5)


# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":

    main_menu()