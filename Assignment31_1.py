import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix , classification_report
from seaborn import countplot
from sklearn.preprocessing import StandardScaler


def MarvellousBrestCanser(Datapath):
    Line = '*' * 100
    print(Line)

    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully : ")
    print(df.head())
    print(df.info())
    print(Line)

    df.replace('unknown', np.nan, inplace=True)
    df['BareNuclei'] = pd.to_numeric(df['BareNuclei'], errors='coerce')
    df.dropna(inplace=True)

    df.drop(columns=['CodeNumber'], inplace=True, errors='ignore')

    print("Dimensions of dataset is : ", df.shape)
    print(Line)

    x = df.drop(columns=['CancerType'])
    y = df['CancerType']

    print("Dimensions of Features : ", x.shape)
    print("Dimensions of Target : ", y.shape)
    print(Line)

    numeric_cols = x.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    x[numeric_cols] = scaler.fit_transform(x[numeric_cols])
    print(x.head())

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    print("Accuracy:", accuracy_score(y_test, y_pred)*100)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    importance = pd.Series(model.feature_importances_, index=x.columns)
    importance.sort_values(ascending=False).plot(kind='bar', figsize=(10, 6), title='Feature Importance')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    df['CancerType'].value_counts().plot(kind='bar', color=['tomato', 'skyblue'])
    plt.title("Distribution of Cancer Types")
    plt.xlabel("Cancer Type")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()


def main():
    MarvellousBrestCanser("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()