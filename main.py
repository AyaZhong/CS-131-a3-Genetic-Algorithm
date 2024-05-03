from  genetic_algorithm import  generate_population
from  genetic_algorithm import  calculate_fitness,crossover
from genetic_algorithm import tournament
from genetic_algorithm import mutation
import statistics
import matplotlib.pyplot as plt
import random




gene = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9), (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]
max_weight = 250
tournament_size= 2
mutation_rate=0.3
fitness_threshold=1
population_size = 100
crossover_rate=0.5
best_fitness_values = []
average_fitness_values = []
generations_for_graph=[]


def main():
    generation = 1
    population = generate_population(population_size, gene)
    next_generation = []
    fitness_values=[]
    count=0



#generate 100 generation,for example,if you would like to generate 50 generation you can modify to 50.
#If the evolution curve of the best solution generated in each iteration starts to flatten at some point,
# it can be considered that the algorithm is approaching the optimal solution.see the fitness graph.
    while count< 100:
        print("generation:", generation)
        print("Initial population:", population)
        print("=================================")

         # calculate initial population's fitness
        for genotype in population:
            print(genotype)
            fitness = calculate_fitness(genotype, gene, max_weight)
            fitness_values.append(fitness)
            print("Fitness value for population", fitness)

        # keep trak of best fitness and average fiteness
        best_fitness = max(fitness_values)
        average_fitness = sum(fitness_values) / len(fitness_values)

        # add best fitness and average fiteness to list
        print("=============================")
        best_fitness_values.append(best_fitness)
        average_fitness_values.append(average_fitness)


        print("best fitness",best_fitness)
        print("average fitness",average_fitness)
        print("best fitness list",best_fitness_values)
        print("average fitness list",average_fitness_values)
        print("=============================")
        print("Tournament selecting......")


        sorted_population = sorted(population, key=lambda x: calculate_fitness(x, gene, max_weight), reverse=True)
        top_half = sorted_population[:int(population_size / 2)]

        #generate parents
        parents = tournament(top_half, gene, max_weight, tournament_size, population_size)
        print("=============================")
        print("winner group as parents",parents)


        #generate next generation by using crossover and mutation to children
        n = 1
        while len(next_generation) < population_size:
            #each time geerate 2 child

            print("====Generate child in",n,"th time====")
            parent1, parent2 = random.sample(parents, 2)
            print("Random select two parents to crossover:",parent1,parent2)
            child1,child2=crossover(parent1,parent2,crossover_rate)
            print("crossovered children:", child1, child2)
            print("children ready to mutate:",child1,child2)
            mutated_child1= mutation(child1,mutation_rate)
            mutated_child2 = mutation(child2, mutation_rate)
            print("Random child get mutation on random position:",mutated_child1,mutated_child2)
            next_generation.append(mutated_child1)
            next_generation.append(mutated_child2)
            n +=1

        print("=============================")
        print("New generation", next_generation)
        children_fitness = [calculate_fitness(chromosome, gene, max_weight) for chromosome in next_generation]
        print("New generation value", children_fitness)


        population = next_generation
        generation += 1

        next_generation = []
        count +=1

    print("Final population:", population)



    # draw graph
    # generation numbers
    generations = range(1, len(best_fitness_values) + 1)

    plt.plot(generations, best_fitness_values, label='Best Fitness')
    plt.plot(generations, average_fitness_values, label='Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness Graph')
    plt.legend()
    plt.show()


    return population


if __name__ == "__main__":
    main()