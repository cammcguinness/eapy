from eapy.Selection import Selection
import random
class Tournament(Selection):
 
    def setSize(self, size):
        self.size = size
    
    def select(self, population):
        indexes = []
        fitnesses = []
        count = 0
        for member in population:
            indexes.append(count)
            fitnesses.append(member.fitness())
            count+=1
            
        random.shuffle(indexes)
        for i in range(0, len(indexes), self.size):
            fits = []
            indices = []
            
            for j in range(0, self.size):
                indices.append(indexes[i+j])
                fits.append(fitnesses[indexes[i+j]])
                
            
            indices = self.sort(indices, fits)
            mother = population[indices[0]]
            father = population[indices[1]]
           
            child1 = mother.copy()
            child2 = father.copy()
            child1.crossover(child2)
            child1.mutate()
            child2.mutate()
            
            population[indices[self.size-2]] = child1
            population[indices[self.size-1]] = child2
                
            
