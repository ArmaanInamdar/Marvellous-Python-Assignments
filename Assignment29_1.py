import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix , precision_score , f1_score , recall_score
from seaborn import countplot
from sklearn.preprocessing import StandardScaler


def MarvellousTitanicLogistic(Datapath):
    Line = '*'*100
    print(Line)
    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully : ")
    print(df.head())
    print(Line)

    print("Dimensions of dataset is : ",df.shape)
    print(Line)

    print(df.describe())
    print(Line)

    df.drop(columns = ['Insulin','SkinThickness'], inplace = True)

    print("Dimensions of dataset is : ",df.shape)
    print(Line)

    columns = ['Glucose', 'BloodPressure','BMI']

    df[columns] = df[columns].replace(0, np.nan)

    df[columns] = df[columns].fillna(df[columns].median())

    x = df.drop(columns = ['Outcome'])
    y = df['Outcome']
    print(Line)
    print("Dimentions of Target : ",x.shape)
    print("Dimentions os Labels : ",y.shape)
    print(Line)

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y ,test_size = 0.2,random_state = 42)

    lr_model = LogisticRegression()
    lr_model.fit(x_train,y_train)

    y_pred = lr_model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    df.hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')
    plt.suptitle("Feature Distributions", fontsize=16)
    plt.show()

    print(Line)
    print('Accuracy is : ',accuracy)
    print(Line)
    print('Confusion matrix : ')
    print(Line)
    print(cm)
    print(Line)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    print("Using KNN : ")
    print(Line)
    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(x_train,y_train)
        y_pred = knn_model.predict(x_test)
        accuracy = accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)
    knn_model = KNeighborsClassifier(n_neighbors=best_k)
    knn_model.fit(x_train,y_train)
    y_pred = knn_model.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred)

    print('Final best accuracy is : ',accuracy*100)

    outcome_counts = df['Outcome'].value_counts()

    plt.figure(figsize=(6, 4))
    plt.bar(outcome_counts.index, outcome_counts.values, color=['skyblue', 'salmon'])
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.title("Distribution of Diabetes Outcome")
    plt.grid(True)
    plt.show()

    df.to_csv('final_diabetes.csv')

def main():
    MarvellousTitanicLogistic("diabetes.csv")

if __name__ == "__main__":
    main()