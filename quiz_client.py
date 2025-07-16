import tkinter as tk
from tkinter import messagebox, ttk
import socket
import json

class QuizClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x600")
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 20))
        self.style.configure("TButton", font=("Helvetica", 16))
        self.score = 0
        self.current_question = 0
        self.quiz_data = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("localhost", 8080))

        self.create_widgets()

    def create_widgets(self):
        self.qs_label = ttk.Label(self.root, anchor="center", wraplength=500, padding=10)
        self.qs_label.pack(pady=10)

        self.choice_btns = []
        for i in range(4):
            button = ttk.Button(self.root, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.choice_btns.append(button)

        self.feedback_label = ttk.Label(self.root, anchor="center", padding=10)
        self.feedback_label.pack(pady=10)

        self.correct_answer = ttk.Label(self.root, anchor="center", padding=10)

        self.score_label = ttk.Label(self.root, text="Score: 0/{}".format(len(self.quiz_data)), anchor="center", padding=10)
        self.score_label.pack(pady=10)

        self.next_btn = ttk.Button(self.root, text="Next", command=self.next_question, state="disabled")
        self.next_btn.pack(pady=10)

        self.socket.sendall("get_quiz_data".encode())
        response = self.socket.recv(1024).decode()
        self.quiz_data = json.loads(response)
        self.show_question()

    def show_question(self):
        question = self.quiz_data[self.current_question]
        self.qs_label.config(text=question["question"])
        for i in range(4):
            self.choice_btns[i].config(text=question["choices"][i], state="normal")
        self.feedback_label.config(text="")
        self.correct_answer.config(text="")
        self.next_btn.config(state="disabled")

    def check_answer(self, choice):
        question = self.quiz_data[self.current_question]
        selected_choice = question["choices"][choice]
        if selected_choice == question["answer"]:
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(self.quiz_data)), foreground="green")
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.correct_answer.pack(pady=10)
            self.feedback_label.config(text="Incorrect!", foreground="red")
            self.correct_answer.config(text="Correct Answer: {}".format(question["answer"]), foreground="green")
        for button in self.choice_btns:
            button.config(state="disabled")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.quiz_data):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(self.score, len(self.quiz_data)))
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    client = QuizClient(root)
    root.mainloop()