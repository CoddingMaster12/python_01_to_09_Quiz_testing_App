import streamlit as st

# Full quiz data
quiz_data = {
    "Google Colab": [
        ("What is Google Colab primarily used for?", ["Web development", "Mobile app testing", "Cloud-based Python coding and notebooks", "Game development"], "Cloud-based Python coding and notebooks"),
        ("Which file format is commonly used in Google Colab for notebooks?", [".txt", ".docx", ".ipynb", ".html"], ".ipynb"),
        ("Which command installs external libraries in Colab?", ["run install", "install.package", "!pip install", "import install"], "!pip install"),
        ("What is the default programming language supported by Colab?", ["Java", "C++", "Python", "JavaScript"], "Python"),
        ("Can Google Colab use GPU for computation?", ["No", "Only with paid version", "Yes, but only for 30 minutes", "Yes"], "Yes")
    ],
    "Introduction to Python": [
        ("Who developed Python?", ["Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup"], "Guido van Rossum"),
        ("Which symbol is used for comments in Python?", ["//", "--", "#", "<!--"], "#"),
        ("Which of the following is correct to print \"Hello, World\" in Python?", ["print(\"Hello, World\")", "echo \"Hello, World\"", "printf(\"Hello, World\");", "Console.WriteLine(\"Hello, World\");"], "print(\"Hello, World\")"),
        ("Which version introduced f-strings in Python?", ["2.7", "3.5", "3.6", "3.8"], "3.6"),
        ("Python is an example of what type of language?", ["Compiled", "Assembly", "Low-level", "Interpreted"], "Interpreted")
    ],
    "Data Types": [
        ("What data type is the result of: type(3.14)?", ["int", "float", "complex", "str"], "float"),
        ("Which of these is an immutable data type?", ["list", "set", "dict", "tuple"], "tuple"),
        ("What is the data type of True in Python?", ["str", "int", "bool", "binary"], "bool"),
        ("Which function converts a string to an integer?", ["str()", "int()", "float()", "bool()"], "int()"),
        ("Which of the following is used to define a complex number in Python?", ["4j", "j4", "4i", "4#"], "4j")
    ],
    "Operators, Keywords, Variables": [
        ("What will 5 % 2 return?", ["0", "1", "2", "2.5"], "1"),
        ("Which operator is used for exponentiation?", ["^", "**", "//", "%"], "**"),
        ("Which of the following is a valid Python variable name?", ["2data", "data-2", "_data", "class"], "_data"),
        ("Which of the following is a Python keyword?", ["for", "loop", "iterate", "define"], "for"),
        ("What will x = 5; x += 3 result in?", ["5", "8", "3", "15"], "8")
    ],
    "Strings and Casting": [
        ("What does len(\"Hello\") return?", ["4", "5", "6", "Error"], "5"),
        ("Which of these creates a string from an integer x = 10?", ["str(x)", "int(x)", "float(x)", "cast(x)"], "str(x)"),
        ("What will 'Python'[0] return?", ["P", "y", "n", "o"], "P"),
        ("What does 'Python'.lower() return?", ["PYTHON", "python", "Python", "error"], "python"),
        ("Which method can check if a string is numeric?", ["isnum()", "checknum()", "isnumeric()", "isdigit()"], "isnumeric()")
    ],
    "Control Flow": [
        ("What does the if statement do?", ["Loops a block", "Defines a function", "Makes decisions", "Declares variables"], "Makes decisions"),
        ("What is the output of: if 0: print(\"Yes\") else: print(\"No\")?", ["Yes", "No", "0", "Error"], "No"),
        ("Which keyword is used for looping?", ["repeat", "for", "each", "iterate"], "for"),
        ("Which of the following is not a valid control structure?", ["if", "for", "then", "while"], "then"),
        ("What does break do in a loop?", ["Skips to next iteration", "Ends the program", "Exits the loop", "Restarts loop"], "Exits the loop")
    ],
    "Lists, Tuples, and Dictionaries": [
        ("What is the output of [1, 2, 3][1]?", ["1", "2", "3", "Error"], "2"),
        ("Which of these is a mutable type?", ["tuple", "list", "str", "int"], "list"),
        ("How do you define a dictionary in Python?", ["[]", "()", "{}", "<>"] , "{}"),
        ("What will len((1, 2, 3)) return?", ["2", "3", "1", "Error"], "3"),
        ("Which method adds an item to the end of a list?", ["insert()", "push()", "append()", "add()"], "append()")
    ],
    "Sets": [
        ("What is a property of sets in Python?", ["Ordered", "Allow duplicates", "Unordered", "Indexed"], "Unordered"),
        ("Which method adds an element to a set?", ["append()", "insert()", "add()", "update()"], "add()"),
        ("What is the result of {1, 2} | {2, 3}?", ["{2}", "{1, 2, 3}", "{1, 3}", "Error"], "{1, 2, 3}"),
        ("How do you remove all items from a set?", ["delete()", "clear()", "remove()", "discard()"], "clear()"),
        ("What does set([1,2,2,3]) return?", ["{1, 2, 2, 3}", "{1, 2, 3}", "[1, 2, 3]", "Error"], "{1, 2, 3}")
    ],
    "Modules and Functions": [
        ("How do you import a module named math?", ["use math", "include math", "import math", "require math"], "import math"),
        ("What is the output of math.sqrt(16)?", ["4", "8", "2", "16"], "4"),
        ("Which keyword defines a function?", ["def", "func", "define", "function"], "def"),
        ("What will return do in a function?", ["Print the result", "End loop", "Return a value", "Stop the program"], "Return a value"),
        ("Which of these is a built-in function?", ["echo()", "print()", "write()", "send()"], "print()")
    ],
    "Exception Handling": [
        ("Which keyword is used to handle exceptions?", ["check", "error", "except", "fail"], "except"),
        ("What is the output of try: 1/0 except: print(\"Error\")?", ["0", "Error", "ZeroDivisionError", "None"], "Error"),
        ("What is the purpose of finally?", ["Executes if no error", "Executes only on error", "Executes always", "Skips execution"], "Executes always"),
        ("Which of these is a built-in exception?", ["DivideError", "ZeroDivisionError", "MathError", "LogicError"], "ZeroDivisionError"),
        ("How do you manually raise an exception?", ["error()", "raise", "throw", "catch"], "raise")
    ]
}

def run_quiz():
    st.title("Python Quiz")
    st.subheader("Test your Python knowledge!")
    st.subheader("Created by Mohammad Zeeshan Ali")
    st.write("Select a topic to begin the quiz.")
    st.write("Each quiz consists of multiple-choice questions. Choose the correct answer for each question.")
    topic = st.selectbox("Select a topic:", list(quiz_data.keys()))

    if topic:
        score = 0
        total = len(quiz_data[topic])

        for idx, (question, options, correct_answer) in enumerate(quiz_data[topic]):
            st.markdown(f"**Q{idx+1}. {question}**")
            user_answer = st.radio("Select an answer:", options, key=f"q{idx}")
            if user_answer == correct_answer:
                score += 1

        if st.button("Submit Quiz"):
            st.success(f"Your Score: {score}/{total}")
            if score >= total * 0.6:
                st.markdown("### 🎉 Congratulations! You passed the quiz.")
            else:
                st.markdown("### ❌ Sorry, you did not pass. Try again!")

if __name__ == "__main__":
    run_quiz()
