from tkinter import *
from pygame import mixer
root = Tk()
root.geometry('1000x200')
root.title("Piano")

mixer.init()

def C():
    mixer.music.load("C.mp3")
    mixer.music.play()
def Db():
    mixer.music.load("C#.mp3")
    mixer.music.play()
def D():
    mixer.music.load("D.mp3")
    mixer.music.play()
def Eb():
    mixer.music.load("D#.mp3")
    mixer.music.play()
def E():
    mixer.music.load("E.mp3")
    mixer.music.play()
def F():
    mixer.music.load("F.mp3")
    mixer.music.play()
def Gb():
    mixer.music.load("F#.mp3")
    mixer.music.play()
def G():
    mixer.music.load("G.mp3")
    mixer.music.play()
def Ab():
    mixer.music.load("G#.mp3")
    mixer.music.play()
def A():
    mixer.music.load("A.mp3")
    mixer.music.play()
def Bb():
    mixer.music.load("A#.mp3")
    mixer.music.play()
def B():
    mixer.music.load("B.mp3")
    mixer.music.play()
def C2():
    mixer.music.load("C2.mp3")
    mixer.music.play()
def Db2():
    mixer.music.load("C#2.mp3")
    mixer.music.play()
def D2():
    mixer.music.load("D2.mp3")
    mixer.music.play()
def Eb2():
    mixer.music.load("D#2.mp3")
    mixer.music.play()
def E2():
    mixer.music.load("E2.mp3")
    mixer.music.play()
def F2():
    mixer.music.load("F2.mp3")
    mixer.music.play()
def Gb2():
    mixer.music.load("F#2.mp3")
    mixer.music.play()
def G2():
    mixer.music.load("G2.mp3")
    mixer.music.play()
def Ab2():
    mixer.music.load("G#2.mp3")
    mixer.music.play()
def A2():
    mixer.music.load("A2.mp3")
    mixer.music.play()
def Bb2():
    mixer.music.load("A#2.mp3")
    mixer.music.play()
def B2():
    mixer.music.load("B2.mp3")
    mixer.music.play()
def C3():
    mixer.music.load("C3.mp3")
    mixer.music.play()
def Db3():
    mixer.music.load("C#3.mp3")
    mixer.music.play()
def D3():
    mixer.music.load("D3.mp3")
    mixer.music.play()
def Eb3():
    mixer.music.load("D#3.mp3")
    mixer.music.play()
def E3():
    mixer.music.load("E3.mp3")
    mixer.music.play()
def F3():
    mixer.music.load("F3.mp3")
    mixer.music.play()
def Gb3():
    mixer.music.load("F#3.mp3")
    mixer.music.play()
def G3():
    mixer.music.load("G3.mp3")
    mixer.music.play()
def Ab3():
    mixer.music.load("G#3.mp3")
    mixer.music.play()
def A3():
    mixer.music.load("A3.mp3")
    mixer.music.play()
def Bb3():
    mixer.music.load("A#3.mp3")
    mixer.music.play()
def B3():
    mixer.music.load("B3.mp3")
    mixer.music.play()
def C4():
    mixer.music.load("C4.mp3")
    mixer.music.play()

b = Button(root, height=10, width=5, command=C, bg="white")
b.grid(row=0,column=1)

b2 = Button(root, height=10, width=5, command=D, bg="white")
b2.grid(row=0,column=2)

b3 = Button(root, height=10, width=5, command=E, bg="white")
b3.grid(row=0,column=3)

b4 = Button(root, height=10, width=5, command=F, bg="white")
b4.grid(row=0,column=4)

b5 = Button(root, height=10, width=5, command=G, bg="white")
b5.grid(row=0,column=5)

b6 = Button(root, height=10, width=5, command=A, bg="white")
b6.grid(row=0,column=6)

b7 = Button(root, height=10, width=5, command=B, bg="white")
b7.grid(row=0,column=7)

b8 = Button(root, height=10, width=5, command=C2, bg="white")
b8.grid(row=0,column=8)

b9 = Button(root, height=10, width=5, command=D2, bg="white")
b9.grid(row=0,column=9)

b10 = Button(root, height=10, width=5, command=E2, bg="white")
b10.grid(row=0,column=10)

b11 = Button(root, height=10, width=5, command=F2, bg="white")
b11.grid(row=0,column=11)

a1 = Button(root, command=Db, width=2, height=6, bg="black")
a1.place(x=32,y=0)

a2 = Button(root, command=Eb, width=2, height=6, bg="black")
a2.place(x=77,y=0)

a3 = Button(root, command=Gb, width=2, height=6, bg="black")
a3.place(x=167,y=0)

a4 = Button(root, command=Ab, width=2, height=6, bg="black")
a4.place(x=213,y=0)

a5 = Button(root, command=Bb, width=2, height=6, bg="black")
a5.place(x=257,y=0)

a6 = Button(root, command=Db2, width=2, height=6, bg="black")
a6.place(x=347,y=0)

a7 = Button(root, command=Eb2, width=2, height=6, bg="black")
a7.place(x=393,y=0)

b12 = Button(root, height=10, width=5, command=G2, bg="white")
b12.grid(row=0,column=12)

b13 = Button(root, height=10, width=5, command=A2, bg="white")
b13.grid(row=0,column=13)

b14 = Button(root, height=10, width=5, command=B2, bg="white")
b14.grid(row=0,column=14)

b15 = Button(root, height=10, width=5, command=C3, bg="white")
b15.grid(row=0,column=15)

b16 = Button(root, height=10, width=5, command=D3, bg="white")
b16.grid(row=0,column=16)

b17 = Button(root, height=10, width=5, command=E3, bg="white")
b17.grid(row=0,column=17)

b18 = Button(root, height=10, width=5, command=F3, bg="white")
b18.grid(row=0,column=18)

b19 = Button(root, height=10, width=5, command=G3, bg="white")
b19.grid(row=0,column=19)

b20 = Button(root, height=10, width=5, command=A3, bg="white")
b20.grid(row=0,column=20)

b21 = Button(root, height=10, width=5, command=B3, bg="white")
b21.grid(row=0,column=21)

b22 = Button(root, height=10, width=5, command=C4, bg="white")
b22.grid(row=0,column=22)

a8 = Button(root, command=Gb2, width=2, height=6, bg="black")
a8.place(x=482,y=0)

a9 = Button(root, command=Ab2, width=2, height=6, bg="black")
a9.place(x=528,y=0)

a10 = Button(root, command=Bb2, width=2, height=6, bg="black")
a10.place(x=572,y=0)

a11 = Button(root, command=Db3, width=2, height=6, bg="black")
a11.place(x=662,y=0)

a12 = Button(root, command=Eb3, width=2, height=6, bg="black")
a12.place(x=708,y=0)

a13 = Button(root, command=Gb3, width=2, height=6, bg="black")
a13.place(x=797,y=0)

a14 = Button(root, command=Ab3, width=2, height=6, bg="black")
a14.place(x=842,y=0)

a15 = Button(root, command=Bb3, width=2, height=6, bg="black")
a15.place(x=887,y=0)

root.mainloop()
