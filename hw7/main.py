import pandas as pd
def p1():
    data = [9.6, 9.7, 9.8, 9.9, 9.95, 10, 10.05, 10.1, 10.2, 10.3, 10.4]
    df = pd.DataFrame()
    df["data"] = data
    mean = df["data"].mean()
    std = df["data"].std()
    print(mean)
    print(std)
def main():
    p1()

if __name__ == "__main__":
    main()