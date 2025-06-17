def frequency_histogram(data, width, y):
    num_bins = int(data[-1] / width) + 1
    bin_freqs = [0] * num_bins
    for i in range(0, len(data)):
        bin_index = int(data[i] / width)
        bin_freqs[bin_index] += 1
    relative_freqs = [0] * num_bins
    for i in range(0, len(relative_freqs)):
        relative_freqs[i] = bin_freqs[i] / len(data)
    concentrations = [0] * num_bins
    for i in range(0, len(concentrations)):
        concentrations[i] = relative_freqs[i] / width
    bin_index = int(y / width)
    return concentrations[bin_index]

if __name__ == "__main__":
    virginica_data = [
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
        6.5, 6.4, 6.8, 5.7, 5.8, 6.4, 6.5, 7.7, 7.7, 6.0,
        6.9, 5.6, 7.7, 6.3, 6.7, 7.2, 6.2, 6.1, 6.4, 7.2,
        7.4, 7.9, 6.4, 6.3, 6.1, 7.7, 6.3, 6.4, 6.0, 6.9,
        6.7, 6.9, 5.8, 6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9
    ]
    virginica_data = sorted(virginica_data)
    f_5 = frequency_histogram(virginica_data, .48, 5)
    print("f5: ", f_5)
    f_7 = frequency_histogram(virginica_data, .48, 7)
    print("f7: ", f_7)