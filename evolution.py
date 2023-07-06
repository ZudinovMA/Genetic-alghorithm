import random

def random_population():
    population = []
    for i in range(0, 5):
        element = []
        for j in range(0, 8):
            element.append(random.randint(0, 1))
        population.append(element)
    return population

def sort_best_population(population):
    for i in range(0, len(population) - 1):
        for j in range(i + 1, len(population)):
            if sum(population[i]) < sum(population[j]):
                population[i], population[j] = population[j], population[i]
    return population[:5]

def mutation(population):
    lenn = len(population)
    for i in range(0, lenn):
        new_element = population[i]
        for j in range(0, len(new_element)):
            if random.randint(0, 100) <= 70:
                if new_element[j] == 0:
                    new_element[j] = 1
            else:
                if new_element[j] == 1:
                    new_element[j] = 0
        population.append(new_element)
    return population


if __name__ == '__main__':
    population = random_population()
    print(f'Начальные особи: {population}')
    population = sort_best_population(population)
    iteration = 50
    for i in range(iteration):
        population = mutation(population)
        population = sort_best_population(population)
        if (i + 1) % 10 == 0:
            print(f'Итерация {i + 1}: {population}')
