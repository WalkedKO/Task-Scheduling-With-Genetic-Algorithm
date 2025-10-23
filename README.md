TASK SCHEDULING WITH GENETIC ALGORITHMS
Kacper Osmola, 23.10.2025.

The problem:
Let's show the problem on an example. 
We are a company and we hire a two workers: A and B. We want to schedule their working hours in the way it is the most profitable for us.
We can produce those products:
- X, has no value, it's just a component, takes 1 hour to produce.
- Y , also has no value, only a component.
- Z, needs X and Y to be created, we can sell it for 1$.
But there's a problem:
- worker A can only produce X
- where worker B can only produce Y and Z.

The genetic algorithms:
It is classic implementation of genetic algorithm which can be summarized in this way:
- We have a problem, so we create P amount of random solutions (called individuals). We call it population.
- For each solution we calculate the fitness score, it tells us how good is this solution
- We randomly choose X individuals, those with higher fitness score are more probable to be chosen.
- Then from that X individuals, we create new P individuals which will replace current population. We call it next generation. We create them by applying crossover function over the X individuals.
- We repeat the process for the fixed amount of generations.

My implementation:
Class Specie is responsible for all the process. Each individual is represented as an object of class Schedule, which stores 2D list. First index represents a worker, and the second the worker's job schedule. 
Each element represents a product being produced at the time. For choosing the individuals for reproduction I used Fitness proportionate selection algorithm. For crossover, the algorithm chooses half of parent's
workers schedules to copy, and the other half to mix with the second parent schedules. The mixing of schedules is just taking a random part of one parent schedule and injecting it into the other parent's schedule of the 
same worker.

Files:
specie.py - contains the Specie class
schedule.py - contains the Schedule class
worker.py - worker's data class
product.py - product's data class
productTag.py - enum for product tags
main.py - testing, example of implementation
