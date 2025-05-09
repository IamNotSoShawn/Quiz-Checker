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

def check_answers(user_file="answers.txt", correct_file="correct_answers.txt"):
    user_answers = load_answers(user_file)
    correct_answers = load_answers(correct_file)

    if user_answers is None or correct_answers is None:
        return

    print("\n--- Quiz Results ---")
    score = 0
    total = len(correct_answers)

    for q_num in sorted(correct_answers.keys()):
        user_ans = user_answers.get(q_num)
        correct_ans = correct_answers[q_num]
        result = "✅ Correct" if user_ans == correct_ans else f"❌ Wrong (Correct: {correct_ans})"
        print(f"Q{q_num}: You answered '{user_ans}' — {result}")
        if user_ans == correct_ans:
            score += 1

    print(f"\nFinal Score: {score} out of {total}")

if __name__ == "__main__":
    check_answers()