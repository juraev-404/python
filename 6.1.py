import itertools
import numpy as np
from random import randint

# Возможные значения X

domain = [0,0,0,0,0,0,0,0,0,1,1,1]
prob = [0.2] * 12  # Равномерное распределение
li1 = []

all_combinations = list(itertools.product(domain, repeat=4))
for i in range(48):
    for i in range(len(domain)):
        li1.append(domain.pop(randint(0, len(domain))))
    
    domain = [0,0,0,0,0,0,0,0,0,1,1,1]

max_values = [sum(x) for x in all_combinations if sum(x)!=0 and sum(x)!=4]

# Вычисляем вероятности для каждого значения Y
y_values, counts = np.unique(max_values, return_counts=True)
y_probs = counts / len(all_combinations)

# Вывод распределения Y
for y, p in zip(y_values, y_probs):
    print(f"P(Y = {y}) = {p:.4f}")