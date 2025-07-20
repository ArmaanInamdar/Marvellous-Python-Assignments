import pandas as pd


def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    df = pd.DataFrame(data)

    gradedict = {'A+': 'Excellent','A': 'Very Good', 'B+': 'Good','B': 'Average','C': 'Poor'}

    # Replace values using the mapping
    df['Grade'] = [gradedict.get(grade, grade) for grade in data['Grade']]

    print(df)


if __name__ == "__main__":
    main()