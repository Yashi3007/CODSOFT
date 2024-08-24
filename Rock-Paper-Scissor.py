from tkinter import *
from PIL import ImageTk, Image
import random

window = Tk()
window.title("Rock-Paper-Scissors")
window.geometry("800x700")
window.attributes("-alpha",1)

canvas = Canvas(window,width=700, height=800)
canvas.grid(row=0, column=0)

l1=Label(window, text="Player", font=("Times New Roman",25))
l2=Label(window, text="Computer", font=("Times New Roman",25))
l3=Label(window, text="Vs", font=("Times New Roman",40))

l1.place(x=80,y=20)
l2.place(x=560,y=20)
l3.place(x=370,y=230)

img_p = Image.open("default.jpeg")
img_p = img_p.resize((300, 300))
img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

rock_p = Image.open("rock.png")
rock_p = rock_p.resize((300, 300))
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

paper_p = Image.open("paper.jpeg")
paper_p = paper_p.resize((300, 300))
paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

scissor_p = Image.open("scissor.jpeg")
scissor_p = scissor_p.resize((300, 300))
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

img_s = Image.open("selection.jpeg")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)

def game(player):
    select=[1,2,3]
    computer = random.choice(select)
    
    if player == 1:
        canvas.create_image(0, 100, anchor=NW, image=rock_p)
    elif player == 2:
        canvas.create_image(0, 100, anchor=NW, image=paper_p)
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_p)
        

    if computer == 1:
        canvas.create_image(0, 100, anchor=NW, image=rock_p)
    elif computer == 2:
        canvas.create_image(0, 100, anchor=NW, image=paper_p)
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_p)


    if player == computer:
        res = "Draw"
    elif(player == 1 and computer == 3)or(player == 2 and computer == 1)or(player == 3 and computer == 2):
        res = "You Won"
    else:
        res = "Computer Won"

    canvas.create_text(390, 600, text="Result"+res, fill="black", font=("Tmes New Roman",25),tag="result")

def clear():
    canvas.delete("result")
    canvas.create_image(0,100, anchor=NW, image=img_p)
    canvas.create_image(500,100, anchor=NW, image=img_c)

rock_b = Button(window, text="Rock", command=lambda: game(1))
rock_b.place(x=35, y=487)

paper_b = Button(window, text="paper", command=lambda: game(2))
paper_b.place(x=128, y=487)

scissor_b = Button(window, text="Scissor", command=lambda: game(3))
scissor_b.place(x=220, y=487)

clear_b = Button(window, text="Clear", font=("Times New Roman",10,"bold"),width=10, command=clear)
clear_b.place(x=370, y=28)

window.mainloop()