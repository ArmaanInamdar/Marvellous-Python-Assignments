import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    df = pd.DataFrame(data)

    encoder = OneHotEncoder(handle_unknown='ignore')
    encode = encoder.fit_transform(df[['Department']]).toarray()
    encoded = pd.DataFrame(encode, columns=encoder.get_feature_names_out(['Department']))
    df = pd.concat([df, encoded], axis=1)
    print(df)


if __name__ == "__main__":
    main()