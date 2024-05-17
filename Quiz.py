class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List of questions and answers
questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("Who wrote 'Romeo and Juliet'? ", "Shakespeare"),
    Question("What is 2 + 2? ", "4"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print("You got", score, "out of", len(questions), "questions correct.")

if __name__ == "__main__":
    run_quiz(questions)
