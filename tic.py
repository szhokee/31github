import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        self.create_board()
        self.initialize_game()

    def create_board(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5, background="#3498db", foreground="#ecf0f1")
        style.map("TButton", background=[("active", "#2980b9")])

        for i in range(3):
            for j in range(3):
                button = ttk.Button(
                    self.window, text="", style="TButton",
                    width=10, command=lambda row=i, col=j: self.handle_click(row, col)
                )
                button.grid(row=i, column=j, sticky="nsew")

        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def initialize_game(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1
        self.game_over = False

    def handle_click(self, row, col):
        if not self.game_over and self.board[row][col] == 0:
            self.board[row][col] = "X" if self.current_player == 1 else "O"
            button = self.window.grid_slaves(row=row, column=col)[0]
            button.configure(text=self.board[row][col], state="disabled")
            self.check_for_winner()
            self.current_player = 3 - self.current_player  # Switch player

    def check_for_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0 or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.declare_winner(self.board[i][0])

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0 or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.declare_winner(self.board[1][1])

        if all(all(cell != 0 for cell in row) for row in self.board) and not self.game_over:
            self.declare_winner("tie")

    def declare_winner(self, winner):
        self.game_over = True
        message = "It's a tie!" if winner == "tie" else f"Player {winner} wins!"
        answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")
        if answer:
            self.reset_game()
        else:
            self.window.destroy()

    def reset_game(self):
        self.initialize_game()
        for i in range(3):
            for j in range(3):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.configure(text="", state="normal")

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
