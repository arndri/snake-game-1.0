from turtle import Turtle

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.cetak()
        self.hideturtle()
        self.high_score = 0
        

    def cetak(self):
        self.clear()
        self.write(f"Score Anda : {self.score}",align="center",font=("Arial",15,"normal"))

    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
        self.cetak()

    def tambah(self):
        self.clear()
        self.score += 1
        self.cetak()

    def akhir(self):
        self.goto(0,0)
        self.color("black")
        self.write(f" GAME OVER \n Score Anda : {self.score}",align="center",font=("Arial",15,"normal"))
        