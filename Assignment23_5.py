import pandas as pd

def main():
    Line = '*'*50
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

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
    


        

if __name__ == "__main__":
    main()