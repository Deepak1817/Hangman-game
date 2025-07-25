import tkinter as tk
import random

# List of predefined words
word_list = ["apple", "train", "house", "plant", "table"]

# GUI class
class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.word = random.choice(word_list)
        self.guessed_letters = []
        self.attempts_left = 6

        self.create_widgets()
        self.update_word_display()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="🎮 Hangman Game", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.word_display = tk.Label(self.root, text="", font=("Consolas", 24), bg="#f0f0f0")
        self.word_display.pack(pady=20)

        self.status_label = tk.Label(self.root, text="Attempts left: 6", font=("Arial", 14), bg="#f0f0f0")
        self.status_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack(pady=10)

        self.letter_buttons = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(
                self.buttons_frame,
                text=letter.upper(),
                width=4,
                height=2,
                font=("Arial", 10),
                command=lambda l=letter: self.guess_letter(l),
                bg="#ffffff"
            )
            btn.grid(row=i // 9, column=i % 9, padx=4, pady=4)
            self.letter_buttons[letter] = btn

        self.restart_btn = tk.Button(self.root, text="🔄 Restart Game", command=self.restart_game,
                                     bg="#c1e1c1", font=("Arial", 12, "bold"))
        self.restart_btn.pack(pady=15)

    def update_word_display(self):
        display = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_display.config(text=display)

    def guess_letter(self, letter):
        if letter in self.guessed_letters or self.attempts_left == 0:
            return

        self.guessed_letters.append(letter)
        self.letter_buttons[letter]['state'] = 'disabled'

        if letter not in self.word:
            self.attempts_left -= 1

        self.status_label.config(text=f"Attempts left: {self.attempts_left}")
        self.update_word_display()

        if all(l in self.guessed_letters for l in self.word):
            self.status_label.config(text="🎉 You Won!")
            self.disable_all_buttons()
        elif self.attempts_left == 0:
            self.status_label.config(text=f"💀 Game Over! Word was '{self.word}'")
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn.config(state='disabled')

    def restart_game(self):
        self.word = random.choice(word_list)
        self.guessed_letters = []
        self.attempts_left = 6
        self.status_label.config(text="Attempts left: 6")
        self.update_word_display()

        for btn in self.letter_buttons.values():
            btn.config(state='normal')


# Main Program Entry
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()
