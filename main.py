import random
import time

__author__ = 'Maxim'


# Generates vector with <length> random elements
def generate_vector(length):
    vector = []
    for i in range(0, length):
        vector.append(random.randint(0, 1000))
    return vector


# Bubble sort
def bubble_sort(vector):
    for i in range(0, len(vector)):
        for j in range(len(vector) - 1, i, -1):
            if vector[j - 1] > vector[j]:
                vector[j - 1], vector[j] = vector[j], vector[j - 1]


# Checks vector for being sorted
def is_sorted(vector):
    for i in range(1, len(vector)):
        if vector[i - 1] > vector[i]:
            return False
    return True


# Stupid sort
def stupid_sort(vector):
    while not is_sorted(vector):
        idx1 = random.randint(0, len(vector) - 1)
        idx2 = random.randint(0, len(vector) - 1)
        vector[idx1], vector[idx2] = vector[idx2], vector[idx1]


vector1 = generate_vector(100)
print('Generated vector for bubble sort:')
print(vector1)
start_time = time.time()
bubble_sort(vector1)
print('\nSorted vector:')
print(vector1)
print('Sorting time is %s seconds' % (time.time() - start_time))


print('\n-------------------------------------------------------------------------------\n')
vector2 = generate_vector(100)
print('Generated vector for stupid sort:')
print(vector2)
start_time = time.time()
stupid_sort(vector2)
print('\nSorted vector:')
print(vector2)
print('Sorting time is %s seconds' % (time.time() - start_time))


vector2 = generate_vector(100)

