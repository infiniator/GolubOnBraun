from random import randrange
from src.chromosome import Chromosome
from src.binary_search import binarySearch

population = []  # a list of chromosomes


def initialisation():
    # a temporary chromosome to be manipulated before adding to the population
    tempChromosome = Chromosome()
    for i in range(0, 100000):
        for j in range(0, tempChromosome.numTasks):
            k = randrange(0, tempChromosome.numProcs)
            tempChromosome.schedule[k].append(j)
        for j in range(0, tempChromosome.numProcs):
            tempChromosome.schedule[j].sort()
        # tempChromosome.schedule.sort(key=tempChromosome.schedule.itemgetter(0))
        tempChromosome.calculateFitness()
        population.append(tempChromosome)
        tempChromosome = Chromosome()


def selection():
    print("he")


def crossover(a, b):
    randProc = randrange(0, a.numProcs)
    randTask = randrange(0, a.numTasks)
    indexA = -1
    indexB = -1
    for i in range(0, b.numProcs):
        indexB = binarySearch(b[i], randTask)
        indexA = binarySearch(a[i], randTask)


def mutation(a):
    removeFrom = -1
    addTo = -1
    while removeFrom == addTo and len(a.schedule[removeFrom]) > 0:
        removeFrom = randrange(0, a.numProcs)
        addTo = randrange(0, a.numProcs)
    randTask = randrange(0, len(a.schedule[removeFrom]))
    a.schedule[addTo].insert(
        binarySearch(a.schedule[addTo], a.schedule[removeFrom][randTask]),
        a
    )
    del a.schedule[removeFrom][randTask]
    return a
