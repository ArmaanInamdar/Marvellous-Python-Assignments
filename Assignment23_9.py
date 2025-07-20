import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    Line = '*'*50
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, np.nan, 82]
    }

    df = pd.DataFrame(data)

    print("Missing values in each column",df.isnull().sum())
    df.fillna(df.mean(numeric_only=True), inplace=True)

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print(Line)
    print("Shape of DataFrame:", df.shape)
    print(Line)
    print(df.head())
    print(Line)
    print("Columns:", df.columns.tolist())
    print(Line)
    print("Data Types:", df.dtypes)
    print(Line)
    print("Description : ")
    print(Line)
    print(df.describe())
    print(Line)
    i = 0
    print("Students who scored more than 85 marks in science : ")
    for mark in df['Science']:
        if(mark > 85):
            print(df['Name'][i])
            i = i + 1
    print(Line)
    df['Name'].replace('Pooja','Puja',inplace=True)
    print("Updated dataset")
    print(df.head())
    print(Line)
    sdata = df.sort_values(by = 'Total',ascending=False)
    print(sdata)
    print(Line)
    Names = df['Name']
    Marks = df['Total']
    plt.bar(Names,Marks , color='skyblue') 

    plt.xlabel('Student Name')
    plt.ylabel('Marks')
    plt.title('Exam Marks')

    plt.show()

    Name = df[df['Name'] == 'Amit'].iloc[0]
    subjects = ['Math','Science','English']
    marks = Name[subjects]

    plt.plot(subjects,marks,color='skyblue') 

    plt.xlabel('Subjects Name')
    plt.ylabel('Amit Marks')
    plt.title('Exam Marks')

    plt.show()


        

if __name__ == "__main__":
    main()