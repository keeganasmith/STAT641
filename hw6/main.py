import math
def poisson(k, _lambda = 18.4):
    return _lambda**k * math.e**(-_lambda) / math.factorial(k) 
def q4():
    ranges = [
        [0, 10],
        [11, 15],
        [16, 20], 
        [21, 25],
        [26, 30],
        [31, 125]
    ]
    probabilities = [0] * len(ranges)
    index = 0
    for range in ranges:
        i = range[0]
        while(i <= range[1]):
            probabilities[index] += poisson(i)
            i+= 1
        index += 1
    print(probabilities)
    expected_values = [0] * len(ranges)
    index = 0
    for prob in probabilities:
        expected_values[index] = prob * 150
        index += 1
    print(expected_values)
    observed = [5, 34, 64, 40, 5, 2]
    q = 0
    i = 0
    while(i < len(observed)):
        q += (observed[i] - expected_values[i])**2 / expected_values[i]
        i += 1
    print(q)

def main():
    q4()

if __name__ == "__main__":
    main()