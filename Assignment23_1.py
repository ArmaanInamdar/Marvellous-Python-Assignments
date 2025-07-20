import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    print("Shape of DataFrame:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data Types:", df.dtypes)

if __name__ == "__main__":
    main()