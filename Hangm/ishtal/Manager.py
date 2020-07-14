import tkinter as tk
from Hangm.ishtal.Hangman import *
from Hangm.ishtal.Main import *
man = tk.Tk()
greeting = tk.Label(text="Welcome to the game-Hangman,Type the subject and the word.",fg = "white",  bg = "blue",width=70,height=3)
greeting.pack()
subject = tk.Entry(text="Subject:",fg="black", bg="white", width=50)
subject.pack()
word = tk.Entry(text="Word:",fg="black", bg="white", width=50)
word.pack()
ent = tk.Button(text="Enter",width=4,height=2,bg="blue",fg="yellow",comand=Hangm.ishtal.Main)
ent.pack()
man.mainloop()
