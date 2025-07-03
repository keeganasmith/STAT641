import pandas as pd
import matplotlib.pyplot as plt
import math


def trimmed_mean(df, alpha, column):
    num = int(len(df) * alpha)
    df = df.sort_values(by=column).reset_index(drop=True)
    trimmed_df = df.iloc[num:len(df) - num]
    return trimmed_df[column].mean()

def cdf_estimate(df, column):
    values = df[column]
    cdf = values.rank(method='max', pct=True)
    return cdf

def p2_plot():
    df = pd.read_csv("../colon.csv")
    t = df["time"]
    cdf = cdf_estimate(df, "time")
    survival = -cdf + 1
    plt.xlabel("")
    plt.ylabel("t")
    plt.scatter(survival, t)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../colon.csv")
    df = df.loc[df["sex"] == 1]
    mean = trimmed_mean(df, .10, "time")
    print(mean)
    mean = trimmed_mean(df, 0, "time")
    print(mean)
    p2_plot()
