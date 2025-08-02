import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def MarvellousStudent(Datapath):

    df = pd.read_csv(Datapath, sep=';')

    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    cluster_centers = pd.DataFrame(
        scaler.inverse_transform(kmeans.cluster_centers_), 
        columns=features
    )

    def assign_cluster_label(row):
        if row['Cluster'] == 2:
            return 'Top Performers'
        elif row['Cluster'] == 1:
            return 'Average Students'
        else:
            return 'Struggling Students'

    df['PerformanceGroup'] = df.apply(assign_cluster_label, axis=1)

    print("Cluster Centers :")
    print(cluster_centers)

    print("Number of students in each group:")
    print(df['PerformanceGroup'].value_counts())

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='G3', y='studytime', hue='PerformanceGroup', palette='Set1')
    plt.title('Clustering of Students by Final Grade vs Study Time')
    plt.xlabel('Final Grade (G3)')
    plt.ylabel('Study Time')
    plt.grid(True)
    plt.show()

    df.to_csv("student_performance_clustered.csv", index=False)

def main():
    MarvellousStudent("student-mat.csv")

if __name__ == "__main__":
    main()
