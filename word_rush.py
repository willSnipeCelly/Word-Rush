import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time
import os

def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return [word.strip().lower() for word in words if len(word.strip()) == 5]

def load_scores(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        scores = file.read().splitlines()
    score_dict = {}
    for score in scores:
        name, points = score.split(':')
        score_dict[name.strip()] = int(points.strip())
    return score_dict

def save_scores(filename, scores):
    with open(filename, 'w') as file:
        for name, points in scores.items():
            file.write(f"{name}: {points}\n")

# Load words and scores
ANSWER_WORDS = load_words('words.txt')
GUESSABLE_WORDS = load_words('guessable_words.txt')
SCORES_FILE = 'scores.txt'
scores = load_scores(SCORES_FILE)

class WordleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        self.master.geometry("600x800")
        self.rounds = 0
        self.total_time = 0
        self.times = []
        self.total_score = 0

        self.create_widgets()
        self.reset_game()
        self.update_timer()

    def reset_game(self):
        self.word_to_guess = random.choice(ANSWER_WORDS)
        print(self.word_to_guess)
        self.guesses = []
        self.current_guess = ""
        self.start_time = time.time()
        
        if hasattr(self, 'guess_text'):
            self.guess_text.config(state=tk.NORMAL)
            self.guess_text.delete('1.0', tk.END)
            self.guess_text.config(state=tk.DISABLED)

        self.reset_keyboard()

    def create_widgets(self):
        self.instructions = tk.Label(self.master, text="Guess the 5-letter word!")
        self.instructions.pack()

        self.timer_label = tk.Label(self.master, text="Time: 0")
        self.timer_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()
        self.guess_entry.bind("<Return>", self.check_guess)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.guess_frame = tk.Frame(self.master, height=1000, width=300)
        self.guess_frame.pack()
        self.guess_text = tk.Text(self.guess_frame, height=14, width=23, wrap=tk.WORD, state=tk.DISABLED)
        self.guess_text.config(fg="black")
        self.guess_text.pack(side=tk.LEFT)

        self.create_keyboard()

    def create_keyboard(self):
        self.keyboard_frame = tk.Frame(self.master)
        self.keyboard_frame.pack()

        self.buttons = {}
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        for row in rows:
            row_frame = tk.Frame(self.keyboard_frame)
            row_frame.pack(side=tk.TOP)
            for char in row:
                button = tk.Button(row_frame, text=char.upper(), command=lambda c=char: self.add_to_guess(c), width=1, height=2)
                button.pack(side=tk.LEFT)
                self.buttons[char] = button

    def reset_keyboard(self):
        for button in self.buttons.values():
            button.config(state="normal")

    def add_to_guess(self, char):
        if len(self.current_guess) < 5:
            self.guess_entry.insert(tk.END, char)
            self.current_guess += char

    def check_guess(self, event=None):
        self.current_guess = self.guess_entry.get().lower()
        if len(self.current_guess) != 5:
            messagebox.showerror("Error", "Please enter a 5-letter word.")
            return
        
        if self.current_guess not in GUESSABLE_WORDS:
            messagebox.showerror("Error", "Word not in the list.")
            return

        self.guesses.append(self.current_guess)
        self.display_guess(self.current_guess)
        self.update_keyboard(self.current_guess)
        self.guess_entry.delete(0, tk.END)

        if self.current_guess == self.word_to_guess:
            elapsed_time = int(time.time() - self.start_time)
            self.times.append(elapsed_time)
            self.total_time += elapsed_time
            self.calculate_score(elapsed_time, len(self.guesses))
            self.rounds += 1
            if self.rounds < 10:
                self.start_new_game()
            else:
                self.end_game(True)
        elif len(self.guesses) >= 6:
            self.end_game(False)
        else:
            self.current_guess = ""

    def start_new_game(self):
        self.reset_game()
        self.guess_entry.delete(0, tk.END)

    def display_guess(self, guess):
        self.guess_text.config(state=tk.NORMAL)
        guess_frame = tk.Frame(self.guess_text)
        word_to_guess_copy = list(self.word_to_guess)

        # First pass: mark correct letters (green)
        for i, char in enumerate(guess):
            label = tk.Label(guess_frame, text=char, width=2, height=1, font=("Helvetica", 18))
            if char == self.word_to_guess[i]:
                label.config(bg="green", fg="black")
                word_to_guess_copy[i] = None  # Mark this char as used
            label.pack(side="left", padx=2, pady=2)
        
        # Second pass: mark present letters (yellow)
        for i, char in enumerate(guess):
            if char != self.word_to_guess[i]:
                label = guess_frame.winfo_children()[i]
                if char in word_to_guess_copy:
                    label.config(bg="yellow", fg="black")
                    word_to_guess_copy[word_to_guess_copy.index(char)] = None  # Mark this char as used
                else:
                    label.config(bg="white", fg="black")

        self.guess_text.window_create(tk.END, window=guess_frame)
        self.guess_text.insert(tk.END, "\n")
        self.guess_text.config(state=tk.DISABLED)

    def update_keyboard(self, guess):
        for char in guess:
            if char not in self.word_to_guess:
                self.buttons[char].config(state="disabled")

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}")
        self.master.after(1000, self.update_timer)

    def calculate_score(self, time_taken, guesses):
        base_score = 100
        time_bonus = max(0, 120 - 2 * time_taken) if time_taken <= 60 else 0
        guess_penalty = [0, 0, 0, -25, -50, -100][guesses - 1]

        round_score = base_score + time_bonus + guess_penalty
        self.total_score += round_score

    def end_game(self, won):
        if won:
            messagebox.showinfo("Congratulations!", f"You completed 10 rounds!\nTotal Time: {self.total_time} seconds\nTimes per round: {self.times}\nTotal Score: {self.total_score}")
        else:
            messagebox.showinfo("Game Over", f"You've used all 6 guesses.\nRounds completed: {self.rounds}\nTotal Time: {self.total_time} seconds\nTotal Score: {self.total_score}")
        
        player_name = simpledialog.askstring("Name", "Enter your name:")
        if player_name:
            scores[player_name] = self.total_score
            save_scores(SCORES_FILE, scores)
        
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        score_board = "\n".join([f"{name}: {points}" for name, points in sorted_scores])
        messagebox.showinfo("Score Board", score_board)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleGame(root)
    root.mainloop()
