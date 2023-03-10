from turtle import Turtle
POSISI_AWAL = [(0,0),(-20,0),(-40,0)]
JARAK = 20
ATAS = 90
BAWAH = 270
KANAN = 0
KIRI = 180

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for posisi_segment in POSISI_AWAL:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(posisi_segment)
            self.segment.append(new_segment)
    
    def move(self):
        for segment_num in range(len(self.segment)-1,0,-1):
            new_x = self.segment[segment_num - 1].xcor()
            new_y = self.segment[segment_num - 1].ycor()
            self.segment[segment_num].goto(new_x,new_y)
        self.head.forward(JARAK)

    def tambah_segment(self, posisi_segment):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(posisi_segment)
        self.segment.append(new_segment)

    def extend(self):
        self.tambah_segment(self.segment[-1].position())

    def up(self):
        if self.head.heading() != BAWAH:
            self.head.setheading(ATAS)

    def down(self):
        if self.head.heading() != ATAS:
            self.head.setheading(BAWAH)

    def left(self):
        if self.head.heading() != KANAN:
            self.head.setheading(KIRI)

    def right(self):
        if self.head.heading() != KIRI:
            self.head.setheading(KANAN)