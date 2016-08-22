from abc import ABCMeta, abstractmethod

class Representation(metaclass=ABCMeta):
    'This is the base class for representations to be used in the evolutionary algorithm.'
    @abstractmethod
    def randomize(self):
        pass
        
    @abstractmethod
    def fitness(self):
        pass
        
    @abstractmethod
    def mutate(self):
        pass
        
    @abstractmethod
    def crossover(self, other):
        pass
        
    @abstractmethod
    def copy(self):
        pass
        
    @abstractmethod
    def toString(self):
        pass
