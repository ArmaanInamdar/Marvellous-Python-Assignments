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
    print("Columns:", df.columns.tolist())
    print("Data Types:", df.dtypes)
    print("Description : ")
    print(df.describe())

if __name__ == "__main__":
    main()