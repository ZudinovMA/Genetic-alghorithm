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
    return population

def mutation(element):
    if random.randint(0, 100) <= 10:
        mutation_gen = random.randint(0, len(element) - 1)
        if element[mutation_gen] == 1:
            element[mutation_gen] = 0
        else:
            element[mutation_gen] = 1
    return element
def cross(population):
    count_par = len(population) // 2
    par = []
    share = []
    for i in range(count_par):
        share.append(random.randint(1, len(population[0]) - 1))
    for i in range(0, count_par * 2):
        while len(par) != i + 1:
            x = random.randint(0, len(population) - 1)
            if x not in par:
                par.append(x)
    new_par = []
    mas = []
    for i, ii in enumerate(par):
        if i % 2 != 0 or i == 0:
            mas.append(ii)
        else:
            new_par.append(mas)
            mas = [ii]
    new_par.append(mas)

    for i in range(len(new_par)):
        new_element = []
        for j in range(0, share[i]):
            new_element.append(population[new_par[i][0]][j])
        for j in range(share[i], len(population[0])):
            new_element.append(population[new_par[i][1]][j])
        new_element = mutation(new_element)
        population.append(new_element)
    population = sort_best_population(population)
    return population


if __name__ == '__main__':
    population = random_population()
    print(f'Начальные особи: {population}')
    population = sort_best_population(population)
    iteration = 15
    for i in range(iteration):
        population = cross(population)
        print(f'Итерация {i+1}: {population}')


