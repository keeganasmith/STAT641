import numpy as np
from scipy.stats import binom, poisson
value = .48
n = 15
p = .6
i = 0
total_prob = 0
while(True):
    total_prob += binom.pmf(i, n, p)
    if total_prob >= value:
        print("result: ", i)
        break;
    i += 1


total_prob = 0
i = 0
while(True):
    total_prob += poisson.pmf(i, 4)
    if(total_prob >= value):
        print("result: ", i)
        break;
    i += 1
