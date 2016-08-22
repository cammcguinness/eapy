# eapy
## Evolutionary Algorithm Framework in Python


This project is a minimal framework for evolutionary algorithms. It is meant as a starting project to get you started with evolutionary algorithms. The user will need to create their own selection methods and representation (or use ones found in the examples). 

### Getting started

1. The first step is to create a representation (population member). For this, you need to extend the abstract class Representation. There are 6 methods that you need to write.
	1. `copy()` -- This method creates a copy of the representation based on the current one.
    2. `crossover(other)` -- This method performs crossover and is given another Representation object
    3. `fitness()` -- This method calculates the current fitness of the Population Member
    4. `mutate()` -- This method mutates the current population member
    5. `randomize()` -- This method is called when the population is initialized and creates a random member
    6. `toString()` -- This is for logging purposes to print out which member has the highest fitness

2. The next step is to create the selection method. For this, you need to extend the abstract class Selection. There is only one method that you need to write, `select()`. This method needs to perform whatever actions are needed to choose which members to breed and perform the breeding and replacing of poor members.

3. Once you have these two classes created you simply create an EA object by calling 
`EA(selection,Representation,popSize)`. The selection method needs to be instantialized while you only need to send in the Object name for the representation. Once the EA object is created, call EA.run(generations).

###Examples
For an example see \_\_main\_\_.py and the examples directory. The example directory would also be a good place to find implemented Selection methods (they are typically problem independent).
