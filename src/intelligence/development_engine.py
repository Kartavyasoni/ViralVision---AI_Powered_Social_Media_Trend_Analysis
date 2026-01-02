# Development Intelligence Engine
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def perform_pca(df, n_components):
    """Perform PCA on the dataset."""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(df)