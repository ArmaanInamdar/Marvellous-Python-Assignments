import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    print("Shape of DataFrame:", df.shape)
    print(df.head())
    print("Columns:", df.columns.tolist())
    print("Data Types:", df.dtypes)
    print("Description : ")
    print(df.describe())
    i = 0
    print("Students who scored more than 85 marks in science : ")
    for mark in df['Science']:
        if(mark > 85):
            print(df['Name'][i])
            i = i + 1
        

if __name__ == "__main__":
    main()