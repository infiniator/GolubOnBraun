from random import randrange
from src.chromosome import Chromosome

population = []  # a list of chromosomes


def initialisation():
    # a temporary chromosome to be manipulated before adding to the population
    tempChromosome = Chromosome()
    for i in range(0, 100000):
        for j in range(0, 512):
            k = randrange(0, 16)
            tempChromosome.schedule[k].append(j)
        tempChromosome.calculateFitness()
        population.append(tempChromosome)
        tempChromosome = Chromosome()


def selection():
    print("he")
