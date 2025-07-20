import pandas as pd
import numpy as np

def main():
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

    df = pd.DataFrame(data)
    print(df)
    print(df.dtypes)

    for column in df.columns:
        print(f"{column}: {df[column].dtype}")

    df['Age'] = df['Age'].astype(int)

    print(df)

    print(df.dtypes)

if __name__ == "__main__":
    main()