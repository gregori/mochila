import numpy as np
import ga

def main():
    # Variáveis de configuração e controle
    num_genes = 6
    num_solutions = 8
    pop_size = (num_solutions, num_genes)
    num_generations = 100
    num_parents_mating = 4
    weights = np.array([15, 3, 2, 5, 9, 20])
    points = np.array([15, 7, 10, 5, 8, 17])
    
    # Gerar população inicial
    population = gen_initial_population(pop_size)

    # Calcular o fitness
    fitness = ga.calc_pop_fitness(population, weights, points)


    # enquanto a cond. de parada não for atingida
    for generation in range(num_generations):
        print(f"Geração {generation}:")
        print(population)
        print(f"Fitness: {fitness}")
        print_best_solution(fitness, population)

        # Seleciona os indivíduos
        parents = ga.select_mating_pool(
            population, fitness, num_parents_mating
        )
    
        # Faz o crossover
        offspring_crossover = ga.crossover(
            parents, get_offspring_size(num_solutions, parents, num_genes)
        )
        print("Resultado do Crossover:")        
        print(offspring_crossover)
    
        # Faz a mutação
        offspring_mutation = ga.mutation(offspring_crossover)
        print("Resultado da Mutação:")
        print(offspring_mutation)

        # # Gerar nova população
        population = gen_new_population(pop_size, parents, offspring_mutation)
        
        # # Calcula o fitness
        fitness = ga.calc_pop_fitness(population, weights, points)

    # fim enquanto
    # imprime resultado
    print_best_solution(fitness, population)

def print_best_solution(fitness, population):
    best_match_idx = np.where(fitness == np.max(fitness))

    print(f"Melhor solução: {population[best_match_idx[0][0]]}")
    print(f"Fitness da melhor solução: {fitness[best_match_idx[0][0]]}")


def gen_initial_population(pop_size):
    population = np.random.randint(low=0, high=2, size=pop_size)

    return population


def get_offspring_size(num_solutions, parents, num_genes):
    return (num_solutions - parents.shape[0], num_genes)


def gen_new_population(pop_size, parents, offspring):
    new_population = np.empty(pop_size)
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring

    return new_population


if __name__ == "__main__":
    main()