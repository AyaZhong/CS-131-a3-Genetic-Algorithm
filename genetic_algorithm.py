import  random



#initial population  with
def generate_population(populaion_size, gene):
    population = []
    for _ in range(populaion_size):
        #select gene without repeat
        no_duplicates = random.sample(gene,len(gene))
        # generate genotype with random number 0 or 1.
        genotype = [random.randint(0, 1) for _ in range(len(no_duplicates))]
        # generate initial population
        population.append(genotype)
    return population


#calculate fiteness of every genotype in the population
def calculate_fitness(genotype, gene, max_weight):
    # for each genotype in the population,we calculate its total weight and total value;
    # this fitness rule is if the total weight over 250, then the fitness total value = 0.
    total_weight = sum(gene[i][0] for i in range(len(gene)) if genotype[i] == 1)
    total_value = sum(gene[i][1] for i in range(len(gene)) if genotype[i] == 1)

    if total_weight > max_weight:
        total_value = 0

    # fitness=[]
    # fitness.append((total_value))
    return total_value







# use tournament selection, select parents from top 50%.

def tournament(population, gene, max_weight, tournament_size, population_size):
    parent_group = []
    sorted_population=sorted(population,key=lambda x:calculate_fitness(x,gene,max_weight),reverse=True)
    top_half=sorted_population[:int(population_size/2)]
    # print("Top 50%",top_half)
    #
    # for genotype in top_half:
    #     print(genotype)
    #     fitness50 = calculate_fitness(genotype, gene, max_weight)
    #     # fitness_values.append(fitness)
    #     print("Top 50% fitness value", fitness50)





    # generate winner as parents in Top 50%
    while len(parent_group) < population_size:
        max_fitness = float('-inf')
        winner = None
        competitors = random.sample(top_half, tournament_size)

        for genotype in competitors:
            fit = calculate_fitness(genotype, gene, max_weight)
            print("Two genotype are battling", genotype, "fitness value",fit)

            if fit > max_fitness:
                max_fitness = fit
                winner = genotype

        print("Winner:", winner)
        parent_group.append(winner)
    return parent_group



#crossover children in random position
def crossover(parent1,parent2,crossover_rate):
   if random.random() < crossover_rate:
    crossover_point =random.randint(1,len(parent1)-1 )
    child1=parent1[:crossover_point]+parent2[crossover_point:]
    child2=parent2[:crossover_point]+parent1[crossover_point:]
   else:
    child1=parent1
    child2=parent2


   return child1,child2



#mutate children in radom position, Perform single-point mutation
def mutation (child,mutation_rate):
    mutated_child=child.copy()
    # Select a random index for mutation
    index = random.randint(0, len(mutated_child) - 1)

    if random.random() < mutation_rate:
        if mutated_child[index] == 0:
            mutated_child[index] = 1
        elif mutated_child[index] == 1:
            mutated_child[index] = 0

    return mutated_child

