
import random as rn

class SakClass:    
    ''' SakClass docstring'''
    def __init__(self):
        self.lets = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]}

        self.letlist = []
        self.randomize_sak()

        d = {}
        with open("greek7.txt" , "r" , encoding = "utf8") as greek7File:
            for line in greek7File:
                d[line]=0

    def showSack(self):
        suma = 0
        for letters in self.lets:
            suma += self.lets[letters][0]
        print('Στο σακουλάκι έχει ', suma, 'γράμματα - Παίζεις....')

    def randomize_sak(self):
        for i in self.lets: 
            for k in range(self.lets[i][0]):
                self.letlist.append(i)
        rn.shuffle(self.letlist)
     
     
    def getletters(self,N):
        getlets=[]
        for i in range (N-1):
            let = rn.sample(self.letlist,1)
            if self.lets[let][0]>0:
                self.lets[i][0] -= 1
                getlets.append(let)
            else:
                del self.lets[let]
            print(getlets)
        # subtracting in self.lex!
        for i in getlets:
            if self.lets[i][0]>0:
                self.lets[i][0] -=1
        self.randomize_sak()
        return getlets

    def putbackletters(self,L):
        #adding in self.lex!
        for i in L:
            self.lets[i][0] +=1
        self.randomize_sak()

    #calculate the points of the word
    def calculatePoints(self,word):
        suma=0
        for letter in word:
            for letters in self.lets:
                suma+= self.lets['letter'][1]
        #return suma


class Player:
    def __init__(self,name):
        sk = SakClass()
        self.name = name
        self.score = 0
        letterslist = []
        letterslist = sk.getletters(7)
        print(letterslist)

    def  addPoints (self,points):
        self.score +=points
        
    def printScore (self):
        print('Ο παίχτης ',self.name,'έχει ', self.score, 'πόντους')


class GamePlay:
    def __init__(self):
        sk = SakClass()

        print('Ο υπολογιστής έχει τα εξής γράμματα: ')
        pc = Player('PC')
        name = input('Δώσε το όνομα σου.\n')
        sk.showSack()
        print( name, ' έχεις τα εξής γράμματα: ')
        person = Player(name)


    #Checks if the word is valid, is concluded in the greek7.txt file
    def validWord(self,word):
        with open('greek7.txt', encoding = "utf8" ) as file:
            for line in file:
                if word in line:
                    #calculatePoint(word)
                    print('Η λέξη είναι έγκυρη')
                else:
                    print('Η λέξη δεν είναι έγκυρη! Προσπάθησε ξανά')
        

    def changeLetters(self):
        pass

    def endGame(self):
        pass




    

#--------------------------main -----------------------------


def menu():
    print('1. ΣΚΟΡ')
    print('2. ΡΥΜΘΙΣΕΙΣ')
    print('3. ΠΑΙΧΝΙΔΙ')
    print('q. ΕΞΟΔΟΣ')



print('******* SCRABLE *******')
print('-----------------------')
while True:
    menu()
    answer=input('Επέλεξε μια ενέργεια... \n')
    if answer in (['q','1','2','3']):
        break
    else:
        print('Λάθος είσοδο! Παρακαλώ εισάγετε νέα.')


        
if answer == '1':
    with open('history.txt', 'r', encoding = "utf8") as his:
        for c,names in enumerate(his,1):
            print (c,names)
elif answer == '2':
    pass
elif answer == '3':
    newgame = GamePlay()
    
else:
    print('ΑΝΤΕ ΓΕΙΑ!')
    
   
    

            
             
         
      
         

