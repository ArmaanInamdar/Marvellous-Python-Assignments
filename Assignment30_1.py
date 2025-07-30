import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix , precision_score , f1_score , recall_score , classification_report, roc_auc_score , roc_curve, auc
from seaborn import countplot
from sklearn.preprocessing import StandardScaler


def MarvellousTitanicLogistic(Datapath):
    Line = '*'*100
    print(Line)
    df = pd.read_csv(Datapath,sep=';', quotechar='"')
    print("Dataset loaded successfully : ")
    print(df.head())
    print(Line)

    print("Dimensions of dataset is : ",df.shape)
    print(Line)

    print(df.describe())
    print(Line)

    df.replace('unknown', np.nan, inplace=True)
    print(df.isnull().sum())

    label_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

    le = LabelEncoder()
    for col in label_cols:
        df[col] = le.fit_transform(df[col])

    df.drop(columns = ['day', 'default', 'pdays', 'balance'], inplace = True)

    print("Dimensions of dataset is : ",df.shape)
    print(Line)

    x = df.drop(columns = ['y'])
    y = df['y'].map({'no': 0, 'yes': 1})    

    print(Line)
    print("Dimentions of Target : ",x.shape)
    print("Dimentions os Labels : ",y.shape)
    print(Line)

    numeric_cols = ['age', 'duration', 'campaign', 'previous']  
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print(df.head())

    x_train, x_test, y_train, y_test = train_test_split(x, y ,test_size = 0.2,random_state = 42)

    lr_model = LogisticRegression()
    lr_model.fit(x_train,y_train)

    y_pred = lr_model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print(Line)
    print("Logistic Regression : ")
    print('Accuracy is : ',accuracy*100)
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
    print(Line)
    print(" KNN : ")
    print('Final best accuracy is : ',accuracy*100)
    print(Line)

    rf_model = RandomForestClassifier(n_estimators=150,max_depth=8,random_state=42)

    rf_model.fit(x_train,y_train)
    y_pred = rf_model.predict(x_test)
    print(Line)
    print(" Random Forest : ")
    print("Accuracy is : ",accuracy_score(y_test,y_pred)*100)
    print(Line)

    print("Classification Report:\n", classification_report(y_test, y_pred))
    print(Line)
    print("ROC-AUC Score: ", roc_auc_score(y_test, y_pred))
    print(Line)

    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random Classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    MarvellousTitanicLogistic("bank-full.csv")

if __name__ == "__main__":
    main()