import tkinter as tk
from tkinter import ttk

class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "Who served as the charioteer for Arjuna during the Kurukshetra War?",
                "answer": "krishna"
            },
            {
                "question": "What is the name of the sacred text within the Mahabharata that contains the teachings of Lord Krishna to Arjuna?",
                "answer": "bhagavad gita"
            },
            {
                "question": "Which character in the Mahabharata is known for his unbreakable vow of celibacy?",
                "answer": "bhishma"
            }
        ]

        self.question_label = ttk.Label(root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.answer_entry = ttk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = ttk.Button(root, text="Submit", command=self.check_answer, command=self.clear)
        self.submit_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=20)

        self.play_again_button = ttk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()  # Hide the button initially

        self.score = 0
        self.question_index = 0
        self.play_again()

    def load_question(self):
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index]["question"])
        else:
            self.question_label.config(text="Quiz completed! Your score: {}".format(self.score))
            self.submit_button.pack_forget()
            self.play_again_button.pack()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.questions[self.question_index]["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = "Incorrect. The correct answer is '{}'.".format(correct_answer)

        self.result_label.config(text=feedback)
        self.question_index += 1
        self.load_question()

    def play_again(self):
        self.score = 0
        self.question_index = 0
        self.result_label.config(text="")
        self.play_again_button.pack_forget()
        self.submit_button.pack()
        self.load_question()

def main():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
