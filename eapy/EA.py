class EA:
    'This is the main class for the evolutionary algorithm.'
    def __init__(self, selection,  representation,  popSize):
        self.selection = selection
        self.popSize = popSize
        #create the starting population.
        self. population = [] 
        for i in range(0,  popSize):
            member=representation()
            member.randomize()
            self.population.append(member)
            
        
    def run(self, numIterations):
        for count in range(0,  numIterations):
            if count%10==0:
                print("Generation: "+str(count))
            self.selection.select(self.population)
        
    
    
