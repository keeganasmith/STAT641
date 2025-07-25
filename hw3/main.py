def iris_quantile(data, quantile):
    #formula: Y_((n−1)u+1)
    n = len(data)
    index = (n - 1) * quantile
    return data[int(index)]

if __name__ == "__main__":
    iris_setosa_data = [
        5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
        5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1,
        5.4, 5.1, 4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7,
        4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4, 5.1,
        5.0, 4.5, 4.4, 5.0, 5.1, 4.8, 5.1, 4.6, 5.3, 5.0
    ]
    iris_setosa_data = sorted(iris_setosa_data)
    setosa_quantile = iris_quantile(iris_setosa_data, .1)
    print(setosa_quantile)
    setosa_quantile = iris_quantile(iris_setosa_data, .4)
    print(setosa_quantile)
    setosa_quantile = iris_quantile(iris_setosa_data, .8)
    print(setosa_quantile)

    virginica_data = [
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
        6.5, 6.4, 6.8, 5.7, 5.8, 6.4, 6.5, 7.7, 7.7, 6.0,
        6.9, 5.6, 7.7, 6.3, 6.7, 7.2, 6.2, 6.1, 6.4, 7.2,
        7.4, 7.9, 6.4, 6.3, 6.1, 7.7, 6.3, 6.4, 6.0, 6.9,
        6.7, 6.9, 5.8, 6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9
    ]
    virginica_data = sorted(virginica_data)
    virginica_quantile = iris_quantile(virginica_data, .1)
    print(virginica_quantile)
    virginica_data = sorted(virginica_data)
    virginica_quantile = iris_quantile(virginica_data, .4)
    print(virginica_quantile)
    virginica_data = sorted(virginica_data)
    virginica_quantile = iris_quantile(virginica_data, .8)
    print(virginica_quantile)
