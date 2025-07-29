from scipy import stats
import numpy as np
def get_rank(combined, value):
    first_occurence = combined.index(value)
    index = first_occurence + 1
    final_index = first_occurence
    while(index < len(combined) and combined[index] == value):
        final_index = index
        index += 1
    average_rank = index + final_index / 2 + 1
    return average_rank

def wilcox_ranks(x, y):
    combined = x + y
    combined = sorted(combined)
    x_sum = 0
    y_sum = 0
    for val in x:
        x_sum += get_rank(combined, val)
    for val in y:    
        y_sum += get_rank(combined, val)
    return x_sum, y_sum


def main():
    x = [117, 119, 128, 120, 121, 129, 122, 114, 117, 118, 126, 122, 122, 121, 117]
    y = [121, 114, 102, 116, 110, 107, 111, 107, 108, 109, 104, 116, 113, 106, 118]
    d = np.asarray(x) - np.asarray(y)
    w_1, w_2 = wilcox_ranks(x, y)
    print(w_1, w_2)
    statistic, p_value = stats.shapiro(x)
    print(p_value)
    statistic, p_value = stats.shapiro(y)
    print(p_value)
    stat, p_value = stats.shapiro(d)
    print(p_value)


if __name__ == "__main__":
    main()