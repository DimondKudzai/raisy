from sklearn.cluster import KMeans


def run_clustering(data, k=3):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(data)
    return labels