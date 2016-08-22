from eapy.Representation import Representation
import random
import sys
class StringMember(Representation):
    size = 11
    LETTERS = ['a','b', 'c','d', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    goal = "hello world"
    maxFitness = -1
    def __init__(self):
        self.letters = []
        
    def randomize(self):
        #print("Length: "+str(len(self.LETTERS)))
        for i in range(0, self.size):
            index = random.randint(0, len(self.LETTERS)-1)
            #print("Index: "+str(index))
            self.letters.append(self.LETTERS[index])
            
    
    def fitness(self):
        fit = 0
        #print(self.size)
        #print(len(self.letters))
        for i in range(0, self.size):
            #print("i: "+str(i))
            #print(self.letters[i]+"="+self.goal[i]+"?")
            if(self.letters[i]==self.goal[i]):
                fit+=1
        if fit>StringMember.maxFitness:
            StringMember.maxFitness = fit
            print("New best fitness found ("+str(fit)+") with "+self.toString())
        return fit
        
    def mutate(self):
        #going to do uniform mutation with a mutation rate of 0.1
        for i in range(0, self.size-1):
            if random.random()<0.1:
                self.letters[i] = self.LETTERS[random.randint(0, len(self.LETTERS)-1)]
                
    def crossover(self, other):
        #going to do uniform crossover with rate of 0.1
        for i in range(0, self.size-1):
            if random.random()<0.1:
                temp = self.letters[i]
                self.letters[i] = other.getValueAt(i)
                other.setValueAt(i, temp)
        
        
    def getValueAt(self, index):
        #just return the value at the given position
        return self.letters[index]
        
    def setValueAt(self, index, value):
        try:
            self.letters[index] = value
        except IndexError:
            print("IndexError at "+str(index)+" letters length("+self.toString()+") = "+str(len(self.letters)))
            sys.exit()
            
        
        
    def copy(self):
        newMember = StringMember()
        newMember.randomize()
        for i in range(0, self.size):
            newMember.setValueAt(i, self.letters[i])
        return newMember
        
    def toString(self):
        s = '';
        for l in self.letters:
            s+=l
        return s
