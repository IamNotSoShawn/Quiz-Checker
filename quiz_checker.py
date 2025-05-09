# Pseudocode: Quiz Answer Checker

# 1. Create an empty dictionary to store answers.
# 2. Try to open the file with the given name.
# 3. For each line in the file:
#    - Remove extra spaces.
#    - Split the line into two parts using the dot ('.') as a separator.
#    - If there are exactly two parts:
#      - The first part is the question number.
#      - second part is the answer (convert it to lowercase).
#      - Store the answer in the dictionary using the question number as the key.
# 4. If the file can’t be found:
#    - Show a message saying the file is missing.
#    - Return nothing.
# 5. Return the dictionary of answers.
# answer key and user answer text file should be on the same folder 

# 1. Load the user’s answers from their file.
# 2. Load the correct answers from the correct answer file.
# 3. If either file couldn’t be loaded, stop here.
# 4. Show the heading “Quiz Results”.
# 5. Set the user’s score to 0.
# 6. Count how many questions are in the correct answers.
# 7. Go through each question number in order:
#    - Get the user’s answer for that question.
#    - Get the correct answer.
#    - If the user’s answer matches:
#      - Show it as correct answer
#      - Add 1 to the score.
#    - Otherwise:
#      - Show it as wrong answer and display the correct answer.
# 8. At the end, display the final score out of the total number of questions.


# Main Program
# - If this script is being run directly (not imported from somewhere else):
#   - Call the check_answers() function using default filenames.


def load_answers(filename):
    answers = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(".")
                if len(parts) == 2:
                    q_num, answer = parts
                    answers[int(q_num)] = answer.lower()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    return answers