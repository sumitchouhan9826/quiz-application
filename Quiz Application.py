users = {}
user_scores = {}

quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
        {"question": "Which data structure uses LIFO?", "options": ["Stack", "Queue", "Array", "Linked List"], "answer": "Stack"},
    ],
    "DBMS": [
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Strong Query Language", "Structured Question Language", "Simple Query Language"], "answer": "Structured Query Language"},
        {"question": "Which of these is a NoSQL database?", "options": ["MySQL", "Oracle", "MongoDB", "SQL Server"], "answer": "MongoDB"},
    ],
    "Python": [
        {"question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "fun", "define"], "answer": "def"},
        {"question": "What data type is the output of: type(5)?", "options": ["int", "float", "str", "None"], "answer": "int"},
    ]
}

# register new user
def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different one.")
    else:
        password = input("Enter a password: ")
        enrollment_number = input("Enter your enrollment number: ")
        contact_number = input("Enter your contact number: ")
        email = input("Enter your email address: ")

        users[username] = {
            "password": password,
            "enrollment_number": enrollment_number,
            "contact_number": contact_number,
            "email": email
        }
        print("Registration successful!")

# login user
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

# attempt quiz
def attempt_quiz():
    print("\n--- Attempt Quiz ---")
    print("Choose a topic: 1. DSA 2. DBMS 3. Python")
    choice = input("Enter the number of your choice: ")
    topic = None
    if choice == "1":
        topic = "DSA"
    elif choice == "2":
        topic = "DBMS"
    elif choice == "3":
        topic = "Python"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Start quiz
    print(f"\nStarting quiz on {topic}")
    questions = quizzes[topic]
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        answer = input("Enter the number of your answer: ")
        if q["options"][int(answer) - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nQuiz completed! Your score: {score}/{len(questions)}")
    return score

#show result
def show_result(username):
    if username in user_scores:
        print(f"\n{username}'s Score: {user_scores[username]}")
    else:
        print("No results found. Attempt a quiz first.")

# Main function
def main():
    username = None

    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Show Result")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
        elif choice == "3":
            if username:
                score = attempt_quiz()
                if score is not None:
                    user_scores[username] = score
            else:
                print("Please login first to attempt a quiz.")
        elif choice == "4":
            if username:
                show_result(username)
            else:
                print("Please login first to view results.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
