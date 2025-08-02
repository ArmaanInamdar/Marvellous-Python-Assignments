import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def MarvellousNewsClassifier(fake_path, true_path):
    Line = '*' * 100
    print(Line)

    df_fake = pd.read_csv(fake_path)
    df_true = pd.read_csv(true_path)
    
    print("Fake news sample:\n", df_fake.head())
    print("True news sample:\n", df_true.head())
    print(Line)

    df_fake['label'] = 0
    df_true['label'] = 1

    df = pd.concat([df_fake, df_true], axis=0).reset_index(drop=True)

    df = df[['text', 'label']]
    df.dropna(inplace=True)

    print("Dataset shape after merge:", df.shape)
    print(df['label'].value_counts())
    print(Line)

    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = tfidf.fit_transform(df['text'])
    y = df['label']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    log_model = LogisticRegression()
    dt_model = DecisionTreeClassifier()

    voting_hard = VotingClassifier(estimators=[
        ('lr', log_model), ('dt', dt_model)], voting='hard')
    voting_hard.fit(x_train, y_train)
    y_pred_hard = voting_hard.predict(x_test)

    acc_hard = accuracy_score(y_test, y_pred_hard)
    cm_hard = confusion_matrix(y_test, y_pred_hard)
    print("\nHard Voting Classifier:")
    print("Accuracy:", acc_hard * 100)
    print(classification_report(y_test, y_pred_hard))

    voting_soft = VotingClassifier(estimators=[
        ('lr', log_model), ('dt', dt_model)], voting='soft')
    voting_soft.fit(x_train, y_train)
    y_pred_soft = voting_soft.predict(x_test)

    acc_soft = accuracy_score(y_test, y_pred_soft)
    cm_soft = confusion_matrix(y_test, y_pred_soft)
    print("\nSoft Voting Classifier:")
    print("Accuracy:", acc_soft * 100)
    print(classification_report(y_test, y_pred_soft))

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm_soft, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title("Confusion Matrix - Soft Voting")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm_hard, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title("Confusion Matrix - Hard Voting")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

    plt.figure(figsize=(6, 4))
    models = ['Hard Voting', 'Soft Voting']
    scores = [acc_hard * 100, acc_soft * 100]
    sns.barplot(x=models, y=scores, palette='coolwarm')
    plt.ylabel('Accuracy (%)')
    plt.title('Voting Classifier Accuracy Comparison')
    plt.ylim(80, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    MarvellousNewsClassifier("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()
