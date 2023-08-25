from tqdm import tqdm
import random
import math
from matplotlib import pyplot as plt

class Map:
    map_data = [('A', [76, 203]), ('B', [165, 75]), ('C', [366, 159]), ('D', [342, 307]),
            ('E', [201, 402]), ('F', [353, 97]), ('G', [489, 310]), ('H', [390, 380]),
            ('I', [501, 302]), ('J', [389, 510]), ('K', [509, 350]), ('L', [410, 160]), ('M', [380, 110])]
        
    map_dict = dict(map_data)
    travel_cities = dict(map_data[1:])
    dist_memory = {}
    
    def draw_map(individual):
        x, y = [], []
        for p in individual.adn:
            position = Map.map_dict[p]
            x.append(position[0])
            y.append(position[1])
            plt.text(position[0], position[1], s = p)
        plt.plot(x, y)
        plt.show()
class Individual:
    def __init__(self):
         self.adn = list(Map.travel_cities.keys()).copy()
         random.shuffle(self.adn)
         self.adn.insert(0, 'A')
         self.adn.append('A')
    def __len__(self):
        return len(self.adn)
    def __add__(self, mother):
        len_individual = len(self)
        c1 = random.randint(1, len_individual - 3)
        c2 = random.randint(c1 + 1, len_individual -2)
        child = Individual()
        child.adn[1:-1] = ['x'] * (len(child) - 2)
        child.adn[c1:c2] = self.adn[c1:c2]
        for idx in range(len(child)):
            if child.adn[idx] == 'x':
                for p2 in mother.adn[1:-1]:
                    if p2 not in child.adn:
                        child.adn[idx] = p2
                        break
        return child
    def mutation(self):
        position_one = random.randint(1, len(self) - 2)
        position_two = random.randint(1, len(self) - 2)
        mutant = self.adn.copy()
        mutant[position_one] = self.adn[position_two]
        mutant[position_two] = self.adn[position_one]
        self.adn = mutant
    def distance(a, b):
        return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1] ** 2))   
    def calc_cost(self):
        if tuple(self.adn) in Map.dist_memory:
         return Map.dist_memory[tuple(self.adn)]
        else:
         cost = 0
        for idx in range(len(self.adn) - 1):
            cost += self.distance(a = Map.map_dict[self.adn[idx]], b = Map.map_dict[self.adn[idx + 1]])
        Map.dist_memory[tuple(self.adn)] = cost
        return cost
class Population:
    def __init__(self, size):
        self.list_idv = []
        for _ in range(size):
            individual = Individual()
            self.list_idv.append(individual)
    def selection(self):
        costs = []
        for individual in self.list_idv:
            costs.append(individual.calc_cost())
        max_costs = max(costs)
        weights = [max_costs - x for x in costs]
        total_weights = sum(weights)
        weights = [w / total_weights for w in weights]
        selected = random.choices(self.list_idv, weights=weights)[0]
        return selected
class GA:
    def __init__(self, size, epochs, crossover_threshold, mutant_threshold):
        self.size = size
        self.epochs = epochs
        self.crossover_threshold = crossover_threshold
        self.mutant_threshold = mutant_threshold
        self.population = Population(size=size)
        self.global_best = {'individual':None, 'cost':10e9}
        self.dist_memory = {}
    def run(self):
        for e in tqdm(range(self.epochs)):
            individual_slected = self.population.selection()
            if individual_slected.calc_cost() <= self.global_best['cost']:
                self.global_best['individual'] = individual_slected
                self.global_best['cost'] = individual_slected.calc_cost()
            self.population = Population(size = self.size)
            for i in range(self.size):
                parent = self.population.selection()
                mother = self.population.selection()
                if random.random() < self.crossover_threshold:
                    child = parent + mother
                else:
                    child = random.choice([parent, mother])                
                if random.random() < self.mutant_threshold:
                    child.mutation()                
                self.population.list_idv.append(child)
    def get_global_best(self):
        return self.global_best
    def draw_best_line(self):
        Map.draw_map(individual=self.global_best['indiviudal'])
if __name__ == '__main__':
    ga = GA(size=100, epochs=500, crossover_threshold=0.5, mutant_threshold=0.5)
    ga.run()
    print(ga.get_global_best())
    ga.draw_best_line()
    plt.plot(ga)
    plt.show()




            

                    
                    

        



