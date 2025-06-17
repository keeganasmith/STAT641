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


if __name__ == "__main__":
    virginica_data = [
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
        6.5, 6.4, 6.8, 5.7, 5.8, 6.4, 6.5, 7.7, 7.7, 6.0,
        6.9, 5.6, 7.7, 6.3, 6.7, 7.2, 6.2, 6.1, 6.4, 7.2,
        7.4, 7.9, 6.4, 6.3, 6.1, 7.7, 6.3, 6.4, 6.0, 6.9,
        6.7, 6.9, 5.8, 6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9
    ]
    f_5 = kernel_estimator(len(virginica_data), .5, K, virginica_data, 5)
    print("f_5: ", f_5)

    f_7 = kernel_estimator(len(virginica_data), .5, K, virginica_data, 7)
    print("f_7: ", f_7)
    data = sorted(virginica_data)
    n = len(data)
    h = 0.5

    y_values = np.linspace(min(data) - 1, max(data) + 1, 200)
    estimates = [kernel_estimator(n, h, K, data, y) for y in y_values]

    plt.figure(figsize=(8, 5))
    plt.plot(y_values, estimates, label='Kernel Density Estimate', color='blue')
    plt.title('Kernel Density Estimator')
    plt.xlabel('y')
    plt.ylabel('Density estimate')
    plt.legend()
    plt.show()

    edf_values = [np.sum(data <= y) / n for y in y_values]

    plt.figure(figsize=(8, 5))
    plt.step(y_values, edf_values, where='post', label='Empirical Distribution Function', color='green')
    plt.title('Empirical Distribution Function')
    plt.xlabel('y')
    plt.ylabel('EDF')
    plt.legend()
    plt.show()

    n = len(data)

    probs = np.linspace(0, 1, n, endpoint=False) + 1/(2*n)

    plt.figure(figsize=(8, 5))
    plt.step(probs, data, where='post', color='purple', label='Quantile function (inverse EDF)')
    plt.title('Quantile Function')
    plt.xlabel('Probability')
    plt.ylabel('Quantile')
    plt.legend()
    plt.show()