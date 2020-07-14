class Hangm:
    def __init__(self, subject, word):
        self.subject = subject
        self.word = word
        self.let = len(word)
        self.count=0
        self.gu=[]
        for j in range (0,len(word)):
            self.gu.append("_")

    def Nihush (self,g):
        b=False
        if(len(g)==1):
            for i in range (0,self.let):
                if(self.word[i]==g):
                    self.gu[i]=g
                    b=True
            if(b==False):
                print("The letter:", g,"is not in the word.")
                self.count=self.count+1
            else:
                print("The letter:", g, "is  in the word.")
        elif(len(g)==self.let):
            if(self.word==g):
                print("You're Right,congratulations.")
                for i in range(0,self.let):
                    self.gu[i]=g[i]
            else:
                self.count=self.count+1
        else:
            print("You've typed an invalid guess, try again.")
    def Sim (self):
        count=0
        for i in range (0,self.let):
            if (self.gu[i]==self.word[i]):
                count=count+1
        if(count==self.let):
            print ("true")
            return True
        else:
            return False


