import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {'Age': [18,22,25,30,35]}
    df = pd.DataFrame(data)

    scale = MinMaxScaler()
    Ndata = scale.fit_transform(df[['Age']])
    print("Normalized data : ",Ndata)


if __name__ == "__main__":
    main()