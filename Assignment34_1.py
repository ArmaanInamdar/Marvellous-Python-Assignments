import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousBreastCancer():
    Line = "*" * 100
    print(Line)

    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)

    print("Dataset loaded successfully")
    print(X.head())
    print("Target classes:", data.target_names)
    print(Line)

    print("Missing values:", X.isnull().sum().sum())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Summary statistics:")
    print(X.describe())

    plt.figure(figsize=(12, 10))
    sns.heatmap(pd.DataFrame(X_scaled, columns=data.feature_names).corr(), cmap='coolwarm')
    plt.title("Feature Correlation Heatmap")
    plt.show()

    sns.countplot(x=y)
    plt.title("Malignant vs Benign (0 = Malignant, 1 = Benign)")
    plt.xlabel("Cancer Type")
    plt.ylabel("Count")
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    importance = pd.Series(model.feature_importances_, index=data.feature_names)
    importance.nlargest(15).plot(kind='barh')
    plt.title("Top 15 Feature Importances")
    plt.xlabel("Importance")
    plt.show()

def main():
    MarvellousBreastCancer()

if __name__ == "__main__":
    main()