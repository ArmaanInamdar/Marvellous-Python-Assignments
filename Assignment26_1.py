import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


def PlayPredictor(Datapath):
    df = pd.read_csv(Datapath)

    print("Before :")
    print(df.head())

    df.drop(columns=['Unnamed: 0'], inplace=True)

    label = LabelEncoder()
    df['Whether'] = label.fit_transform(df['Whether'])
    df['Temperature'] = label.fit_transform(df['Temperature'])
    df['Play'] = label.fit_transform(df['Play'])

    x = df.drop(columns=['Play'])
    y = df['Play']

    print("After :")
    print(df.head())

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)

    plt.figure(figsize = (8,5))
    plt.plot(k_range,accuracy_scores,marker = 'o',linestyle = '--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred)

    print('Final best accuracy is : ',accuracy*100)
    cm = confusion_matrix(y_test,y_pred)
    print(cm)


def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()