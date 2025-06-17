import math
import numpy as np
import matplotlib.pyplot as plt
def K(u):
    return 1 / math.sqrt(2 * math.pi) * math.e**(-u**2 / 2) 

def kernel_estimator(n, h, kernel_function, data, y):
    result = 0
    coefficient = 1 / (n * h)
    smallest_weight = 10000000
    smallest_weight_y = 0
    largest_weight = 0
    largest_weight_y = 0
    for i in range(0, len(data)):
        input = (y - data[i]) / h
        weight = kernel_function(input)
        if(weight < smallest_weight):
            smallest_weight = weight
            smallest_weight_y = data[i]
        if(weight > largest_weight):
            largest_weight = weight
            largest_weight_y = data[i]
        result += kernel_function(input)
    print("smallest weight: ", smallest_weight, " y: ", smallest_weight_y)
    print("largest weight: ", largest_weight, " y: ", largest_weight_y)
    return coefficient * result

def generate_graphs(data, prefix):
    data = sorted(data)
    n = len(data)
    h = 0.5

    y_values = np.linspace(min(data) - 1, max(data) + 1, 200)
    estimates = [kernel_estimator(n, h, K, data, y) for y in y_values]

    plt.figure(figsize=(8, 5))
    plt.plot(y_values, estimates, label=prefix + ' PDF', color='blue')
    plt.title(prefix + ' PDF')
    plt.xlabel('y')
    plt.ylabel('Density estimate')
    plt.legend()
    plt.show()

    edf_values = [np.sum(data <= y) / n for y in y_values]

    plt.figure(figsize=(8, 5))
    plt.step(y_values, edf_values, where='post', label=prefix + ' EDF', color='blue')
    plt.title(prefix + ' EDF')
    plt.xlabel('y')
    plt.ylabel('EDF')
    plt.legend()
    plt.show()

    n = len(data)

    probs = np.linspace(0, 1, n, endpoint=False) + 1/(2*n)

    plt.figure(figsize=(8, 5))
    plt.step(probs, data, where='post', color='blue', label=prefix + ' Quantile Function')
    plt.title(prefix + ' Quantile Function')
    plt.xlabel('Probability')
    plt.ylabel('Quantile')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    virginica_data = [
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
        6.5, 6.4, 6.8, 5.7, 5.8, 6.4, 6.5, 7.7, 7.7, 6.0,
        6.9, 5.6, 7.7, 6.3, 6.7, 7.2, 6.2, 6.1, 6.4, 7.2,
        7.4, 7.9, 6.4, 6.3, 6.1, 7.7, 6.3, 6.4, 6.0, 6.9,
        6.7, 6.9, 5.8, 6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9
    ]
    iris_setosa_data = [
        5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
        5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1,
        5.4, 5.1, 4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7,
        4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4, 5.1,
        5.0, 4.5, 4.4, 5.0, 5.1, 4.8, 5.1, 4.6, 5.3, 5.0
    ]
    f_5 = kernel_estimator(len(virginica_data), .5, K, virginica_data, 5)
    print("f_5: ", f_5)

    f_7 = kernel_estimator(len(virginica_data), .5, K, virginica_data, 7)
    print("f_7: ", f_7)
    generate_graphs(virginica_data, prefix="Virginica")
    generate_graphs(iris_setosa_data, "Setosa")
    