import sys
import numpy as np

def calc_pop_fitness(population, weights, points):
    pop_weights = np.sum(population * weights, axis=1)
    pop_points = np.sum(population * points, axis=1)

    invalid = pop_weights > 30
    pop_points[invalid] = -9999
    
    return pop_points


def select_mating_pool(population, fitness, num_parents_mating):
    # cria um vetor vazio com o tamanho da quantidade de genitores
    parents = np.empty((num_parents_mating, population.shape[1]))

    for parent_idx in range(num_parents_mating):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]

        parents[parent_idx, :] = population[max_fitness_idx, :]
        fitness[max_fitness_idx] = -9999

    return parents


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)

    # o ponto onde o cruzamento acontece entre os genitores
    # geramos um número aleatório entre 1 e o tamanho do cromossomo
    crossover_point = np.random.randint(1, offspring_size[1])

    for chromossome in range(offspring_size[0]):
        # indice do primeiro genitor
        parent1_idx = chromossome % parents.shape[0]
        # indice do segundo genitor
        parent2_idx = (chromossome + 1) % parents.shape[0]
        # O novo filho tera a 1a parte de seus genes
        # oriunda do primeiro genitor
        offspring[chromossome, 0:crossover_point] = parents[
            parent1_idx, 0:crossover_point
        ]
        # o novo filho tera a 2a parte de seus genes
        # oriunda do segundo genitor
        offspring[chromossome, crossover_point:] = parents[
            parent2_idx, crossover_point:
        ]

    return offspring


def mutation(offspring, mutation_rate=0.3):
    # a mutação transforma um gene único em cada filho, aleatoreamente
    # para cada índice entre os cromossomos dos filhos
    for idx in range(offspring.shape[0]):
        # a mutação so ocorrerá se dentro da mutation rate (por padrao 30%)
        if np.random.random() < mutation_rate:
            # escolhe o gene que sofrerá mutação (aleatóreamente)
            random_idx = np.random.randint(0, offspring.shape[1])
            # se o gene tinha 1, recebe 0, se tinha 0, recebe 1
            offspring[idx, random_idx] = (offspring[idx, random_idx] + 1) % 2

    return offspring
