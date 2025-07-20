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
    print(Line)
    df = pd.DataFrame(data)

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    scale = MinMaxScaler()
    Ndata = scale.fit_transform(df[['Math']])
    print("Normalized data : ",Ndata)
    print(Line)
    df['Gender'] = ['Male','Male','Female']
    
    print(Line)
    encoder = OneHotEncoder(handle_unknown='ignore')
    encode = encoder.fit_transform(df[['Gender']]).toarray()
    encoded = pd.DataFrame(encode, columns=encoder.get_feature_names_out(['Gender']))
    df = pd.concat([df, encoded], axis=1)
    print(df)
    print(Line)
    grouped = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print("Average : ")
    print(grouped)
    print(Line)
    sagarmarks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(6,6))
    plt.pie(sagarmarks, labels=sagarmarks, autopct='%1.1f%%', startangle=90)
    plt.title("Marks for Sagar")
    plt.show()

    df['Status'] = df['Total'].apply(lambda A: 'Pass' if A >= 250 else 'Fail')
    count = 0

    print(df)
    print(Line)
    for i in df['Status']:
        if(i == 'Pass'):
            count = count + 1
        
    print("Total students passed : ",count)
    print(Line)

    df.to_csv('Marks.csv',index=False)
    print("Dataset exported")
    print(Line)

    plt.hist(df['Math'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)

    plt.xlabel("Marks")
    plt.ylabel("Students")
    plt.title("Math Histogram")

    plt.show()
    
if __name__ == "__main__":
    main()









