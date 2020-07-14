#main
from Hangm.ishtal.Hangman import *
class H:
    sub=input ("Type the subject and the word")
    wo= input()
    H=Hangm(sub,wo)
    f=False
    while((H.count<7)and(f==False)):
        g=input ("Type your guess.")
        H.Nihush(g)
        f=H.Sim()
        print(H.subject)
        print (H.gu)
        print
    if(f==False):
        print("You've lost the game,He's dead")