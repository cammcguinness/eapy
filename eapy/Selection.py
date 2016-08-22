from abc import ABCMeta, abstractmethod

class Selection(metaclass=ABCMeta):
    'This is the base selection method for the evolutionary algorithm.'
    (MINIMUM, MAXIMUM) = (0, 1)
    
    def __init__(self):
        self.minmax=self.MAXIMUM
    
    @abstractmethod
    #This is the select method. 
    #It chooses which population members to perform variation operators on, perform them and then replace population members.
    def select(self, population):
        pass
        
    def setMinMax(self, minmax):
        self.minmax = minmax
        
    def sort(self, indexes, fitnesses):
        changed = True
        
        while changed:
            changed = False
            for i in range(0, len(indexes)-1):
                if(self.minmax==self.MAXIMUM):
                    if(fitnesses[i]<fitnesses[i+1]):
                        temp = fitnesses[i]
                        fitnesses[i] = fitnesses[i+1]
                        fitnesses[i+1] = temp
                        temp = indexes[i]
                        indexes[i] = indexes[i+1]
                        indexes[i+1] = temp
                        changed = True
                else:
                    if(fitnesses[i]>fitnesses[i+1]):
                        temp = fitnesses[i]
                        fitnesses[i] = fitnesses[i+1]
                        fitnesses[i+1] = temp
                        temp = indexes[i]
                        indexes[i] = indexes[i+1]
                        indexes[i+1] = temp
                        changed = True
        return indexes
