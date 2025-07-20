import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    Line = '*'*50
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    scale = MinMaxScaler()
    Ndata = scale.fit_transform(df[['Math']])
    print("Normalized data : ",Ndata)
    



        

if __name__ == "__main__":
    main()