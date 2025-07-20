import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler , OneHotEncoder

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

    df['Gender'] = ['Male','Male','Female']
    
    
    encoder = OneHotEncoder(handle_unknown='ignore')
    encode = encoder.fit_transform(df[['Gender']]).toarray()
    encoded = pd.DataFrame(encode, columns=encoder.get_feature_names_out(['Gender']))
    df = pd.concat([df, encoded], axis=1)
    print(df)

    grouped = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print("Average : ")
    print(grouped)
    
        

if __name__ == "__main__":
    main()









