import numpy as np
import ga

def main():
    # Gerar população inicial
    num_genes = 6
    num_solutions = 8
    num_generations = 1
    num_parents_mating = 4
    weights = np.array([15, 3, 2, 5, 9, 20])
    points = np.array([15, 7, 10, 5, 8, 17])
    population = gen_initial_population(num_genes, num_solutions)
    print(population)

    # Calcular o fitness
    pop_weights, fitness = ga.calc_pop_fitness(population, weights, points)
    print(pop_weights)
    print(fitness)

    # enquanto a cond. de parada não for atingida
    for generation in range(num_generations):
        # Seleciona os indivíduos
        parents = ga.select_mating_pool(
            population, fitness, pop_weights, num_parents_mating
        )
    
        print(parents)

        # # Faz o crossover
        # offspring_crossover = ga.crossover(parents, get_offspring_size())
    
        # # Faz a mutação
        # offspring_mutation = ga.mutation(offspring_crossover)

        # # Gerar nova população
        # population = gen_new_population(parents, offspring_mutation)
        
        # # Calcula o fitness
        # pop_weights, fitness = ga.calc_pop_fitness(population, weights, points)

    # fim enquanto
    # imprime resultado
    

def gen_initial_population(num_genes, num_solutions):
    pop_size = (num_solutions, num_genes)

    population = np.random.randint(low=0, high=2, size=pop_size)

    return population


def get_offspring_size():
    pass


def gen_new_population(parents, offspring):
    pass


if __name__ == "__main__":
    main()