data  =[10.14, 11.38, 10.93, 11.99, 10.15, 10.07, 10.02, 9.44, 9.39, 10.15,
9.94, 9.79, 10.24, 10.06, 11.63, 11.34, 9.88, 9.17, 9.80, 8.70]

negative_X = []
positive_X = []
for i in range(0, len(data)):
    result = data[i] - 10.5
    if(result < 0):
        negative_X.append(result)
    else:
        positive_X.append(result)






