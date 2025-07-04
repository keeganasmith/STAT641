import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
def mad(data):
    data = np.asarray(data)
    c = np.median(data)
    deviations = np.abs(data - c)
    raw_mad = np.median(deviations)
    return raw_mad / 0.6745
    


def trimmed_mean(df, alpha, column):
    num = int(len(df) * alpha)
    df = df.sort_values(by=column).reset_index(drop=True)
    trimmed_df = df.iloc[num:len(df) - num]
    return trimmed_df[column].mean()

def cdf_estimate_for_x(df, column, value):
    cdf_x = (df[column] <= value).sum() / len(df)
    return cdf_x

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
    plt.savefig("./fig_1.png")

if __name__ == "__main__":
    df = pd.read_csv("../colon.csv")
    df = df.loc[df["sex"] == 0]
    observed_df = df.loc[df["status"] == 1]
    mean = trimmed_mean(observed_df, .10, "time")
    print(mean)
    mean = trimmed_mean(observed_df, 0, "time")
    print(mean)
    #p2_plot()
    est = cdf_estimate_for_x(observed_df, "time", 1200)
    print(est)
    print("median is: ", observed_df["time"].median())
    print(observed_df["time"].describe())
    mad_result = mad(observed_df["time"])
    print(mad_result)

