from matplotlib import pyplot as plt
import random
import math
from tqdm import tqdm

map_data = [('A', [76, 203]), ('B', [165, 75]), ('C', [366, 159]), ('D', [342, 307]),
            ('E', [201, 402]), ('F', [353, 97]), ('G', [489, 310]), ('H', [390, 380]),
            ('I', [501, 302]), ('J', [389, 510]), ('K', [509, 350]), ('L', [410, 160]), ('M', [380, 110])]

map_dict = dict(map_data)
travel_cities = dict(map_data[1:])
root_city = map_data[0]
dist_memory = {}


def draw_map(individual):
    x, y = [], []
    for p in individual:
        position = map_dict[p]
        x.append(position[0])
        y.append(position[1])
        plt.text(position[0], position[1], s=p)

    plt.plot(x, y)
    plt.show()


def initialize_pop(size=100):
    population = []
    for _ in range(size):
        individual = list(travel_cities.keys()).copy()
        random.shuffle(individual)
        individual.insert(0, 'A')
        individual.append('A')
        population.append(individual)
    return population


def distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def calc_cost(individual):
    individual_tuple = tuple(individual)
    if individual_tuple in dist_memory:
        return dist_memory[individual_tuple]
    else:
        cost = 0
        for idx in range(len(individual) - 1):
            cost += distance(a=map_dict[individual[idx]], b=map_dict[individual[idx + 1]])
        return cost


def selection(population):
    costs = []
    for individual in population:
        costs.append(calc_cost(individual))
    max_costs = max(costs)
    weights = [max_costs - x for x in costs]

    total_weights = sum(weights)
    weights = [w / total_weights for w in weights]
    selected = random.choices(population, weights=weights)[0]
    return selected


def crossover(parent1, parent2):
    len_individual = len(parent1)
    c1 = random.randint(1, len_individual - 3)
    c2 = random.randint(c1+1, len_individual - 2)

    child = ['x'] * (len(parent1) - 2)
    child.insert(0, root_city[0])
    child.append(root_city[0])
    child[c1:c2] = parent1[c1:c2]

    for idx in range(len(child)):
        if child[idx] == 'x':
            for p2 in parent2[1:-1]:
                if p2 not in child:
                    child[idx] = p2
                    break
    return child


def mutation(individual):
    position_one = random.randint(1, len(individual) - 2)
    position_two = random.randint(1, len(individual) - 2)

    mutant = individual.copy()
    mutant[position_one] = individual[position_two]
    mutant[position_two] = individual[position_one]

    return mutant


def ga(size=100, epochs=100, crossover_threshold=0.5, mutant_threshold=0.5):
    population = initialize_pop(size)
    global_best = {'individual': None, 'cost': 10e9}

    costs_log = []
    for e in tqdm(range(epochs)):
        individual_selected = selection(population=population)
        if calc_cost(individual_selected) <= global_best['cost']:
            global_best['individual'] = individual_selected
            global_best['cost'] = calc_cost(individual_selected)

        costs_log.append(global_best['cost'])

        new_population = []
        for i in range(size):
            parent1 = selection(population=population)
            parent2 = selection(population=population)

            if random.random() < crossover_threshold:
                child = crossover(parent1=parent1, parent2=parent2)
            else:
                child = random.choice([parent1, parent2])

            if random.random() < mutant_threshold:
                child = mutation(child)

            new_population.append(child)

        population = new_population
    return global_best, costs_log


# def test(size=100):
#     population = initialize_pop(size=100)
#     # selected_individual = selection(population=population)
#
#     child = crossover(parent1=population[0], parent2=population[1])
#     print(population[0])
#     # print(population[1])
#     # print(child)
#
#     print(mutation(individual=population[0]))


if __name__ == '__main__':
    draw_map(individual=[p[0] for p in map_data])
    best_road, costs_log = ga(size=100, epochs=500)
    print(best_road)

    draw_map(best_road['individual'])

    plt.plot(costs_log)
    plt.show()







