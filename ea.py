import random


# Define the Solution class
class Solution:
    def _init_(self, data,):
        self.data = data
        self.pop_size = 10
        self.routes = self.initialize_routes()
        self.fitness = None

    def initialize_routes(self):
        
        # Get routes
        routes =  list(
            zip(
                random.sample(sorted(self.data['Source']),len(self.data['Source'])),
                random.sample(sorted(self.data['Destination']),len(self.data['Destination']))
            )
        )
        return routes


# Fitness function
    def fitness(self,solution, distance_matrix):
        # Calculate fitness based on minimizing overall delivery cost

        total_cost = 0
        total_cost = 0
        for route in solution.routes:
            
                        
            # Calculate cost for each route considering fixed costs and delivery costs
            route_cost = distance_matrix[str(route[0])][str(route[1])]['cost']
                    
            # ... cost calculation logic ...
            total_cost += route_cost
        self.fitness = total_cost
        
        return -total_cost  # Negative because we want to minimize cost

# Selection function
    def selection(population):
        # Select solutions for reproduction using tournament selection
        selected_solutions = []
        tournament_size = 5  # Example value; adjust as needed
        for _ in range(len(population)):
            tournament = random.sample(population, tournament_size)
            winner = max(tournament, key=lambda sol: sol.fitness)
            selected_solutions.append(winner)
        return selected_solutions

# Crossover function
    def crossover(parent1, parent2):
        # Combine two solutions to create a new solution using one-point crossover
        crossover_point = random.randint(1, len(parent1.routes) - 1)
        child_routes = parent1.routes[:crossover_point] + parent2.routes[crossover_point:]
        return Solution(child_routes)

# Mutation function
    def mutation(solution, mutation_rate = 0.3):
        # Introduce random changes to a solution by swapping two routes or modifying a route
        if random.random() < mutation_rate:  # mutation_rate is a user-defined probability
            i, j = random.sample(range(len(solution.routes)), 2)
            solution.routes[i], solution.routes[j] = solution.routes[j], solution.routes[i]

# Function to print generation statistics
    def print_generation_stats(generation, population):
        best_fitness = max(sol.fitness for sol in population)
        average_fitness = sum(sol.fitness for sol in population) / len(population)
        print(f"Generation {generation}: Best Fitness = {best_fitness}, Average Fitness = {average_fitness}")

# Function to get the best solution from the population
    def get_best_solution(population):
        return max(population, key=lambda sol: sol.fitness)

# Evolutionary algorithm function
    def evolutionary_algorithm(self, data, max_generations):
        # Initialize population
        population = [self._init_(data) for _ in range(self.pop_size)]

        # Evaluate initial population
        for solution in population:
            solution.fitness = self.fitness(solution)

        # Evolutionary loop
        for generation in range(max_generations):
            # Selection
            selected_solutions = self.selection(population)

            # Crossover
            offspring = []
            for i in range(0, len(selected_solutions), 2):
                offspring.append(
                    self.crossover(selected_solutions[i], selected_solutions[i + 1])
                )

            # Mutation
            for solution in offspring:
                self.mutation(solution)

            # Evaluate offspring
            for solution in offspring:
                solution.fitness = self.fitness(solution)

            # Replace population with offspring
            population = offspring

            # Optionally, print out some statistics about the generation
            self.print_generation_stats(generation, population)

        # Return the best solution found
        return self.get_best_solution(population)

##########################################################################################


# Run the algorithm with your dataset headers and desired number of generations
