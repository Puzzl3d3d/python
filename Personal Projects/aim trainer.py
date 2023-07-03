import tkinter as tk
import random
import time

game_length = 30

class AimTrainer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aim Trainer")
        self.window.geometry("500x580")
        self.canvas = tk.Canvas(self.window, width=500, height=500, bg="black")
        self.canvas.pack()
        self.score = 0
        self.score_label = tk.Label(self.window, text="Score: {}".format(self.score), font=("Arial", 16))
        self.score_label.pack(side="top")
        self.timer_label = tk.Label(self.window, text="Time remaining: 60", font=("Arial", 16))
        self.timer_label.pack(side="top")

        self.target = self.canvas.create_oval(0, 0, 50, 50, fill="red")

        self.canvas.tag_bind(self.target, "<Button-1>", self.hit_target)
        self.move_target()

        self.start_time = time.time()
        self.remaining_time = game_length
        self.update_timer()

        self.window.mainloop()
        
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.remaining_time = game_length - elapsed_time
        if self.remaining_time <= 0:
            self.timer_label.config(text="Time's up!")
            self.canvas.pack_forget()
            self.window.after(5000, self.restart_game)
            return
        self.timer_label.config(text="Time remaining: {}".format(self.remaining_time))
        self.window.after(100, self.update_timer)

    def move_target(self):
        x = random.randint(50, 450)
        y = random.randint(50, 450)
        self.canvas.coords(self.target, x, y, x+50, y+50)
        #self.window.after(1000, self.move_target)

    def hit_target(self, event):
        self.score += 1
        self.score_label.config(text="Score: {}".format(self.score))

        self.move_target()

    def restart_game(self):
        self.score = 0
        self.start_time = time.time()
        self.remaining_time = 60
        self.score_label.config(text="Score: {}".format(self.score))
        self.timer_label.config(text="Time remaining: {}".format(self.remaining_time))
        self.canvas.pack()
        self.move_target()
        self.update_timer()


if __name__ == "__main__":
    game = AimTrainer()
