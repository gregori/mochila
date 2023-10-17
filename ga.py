import sys
import numpy as np

def calc_pop_fitness(population, weights, points):
    pop_weights = np.sum(population * weights, axis=1)
    pop_points = np.sum(population * points, axis=1)
    
    return pop_weights, pop_points


def select_mating_pool(population, fitness, pop_weights, num_parents_mating):
    # cria um vetor vazio com o tamanho da quantidade de genitores
    parents = np.empty((num_parents_mating, population.shape[1]))

    adjusted_fitness = fitness[pop_weights <= 30]

    for parent_idx in range(num_parents_mating):
        max_fitness_idx = np.where(fitness == np.max(adjusted_fitness))
        print(max_fitness_idx)
        max_fitness_idx = max_fitness_idx[0][0]

        parents[parent_idx, :] = population[max_fitness_idx, :]
        fitness[max_fitness_idx] = -9999

    return parents
