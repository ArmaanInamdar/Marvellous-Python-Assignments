import pandas as pd
import numpy as np

def main():
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
    df = pd.DataFrame(data)

    Q1 = np.percentile(df['Salary'], 25, interpolation = 'midpoint') 
    Q2 = np.percentile(df['Salary'], 50, interpolation = 'midpoint') 
    Q3 = np.percentile(df['Salary'], 75, interpolation = 'midpoint')
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outlier =[]
    for i in df['Salary']:
        if ((i > upper) or (i < lower)):
            outlier.append(i)
    print(' outlier in the dataset is', outlier)

if __name__ == "__main__":
    main()


