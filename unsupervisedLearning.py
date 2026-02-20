# unsupervisedLearning.py
import pandas as pd
from sklearn.cluster import KMeans
import warnings


warnings.filterwarnings("ignore")

def run_unsupervised_learning():
    print("--- Avvio Machine Learning Non Supervisionato (Clustering) ---")
    
    try:
        df = pd.read_csv("dataset_agri.csv")
    except FileNotFoundError:
        print("Errore: dataset_agri.csv non trovato.")
        return

    # Usiamo solo le features ambientali per trovare "Microclimi" simili
    X_cluster = df[['temperatura', 'umidita', 'pioggia_mm']]

    # Applichiamo K-Means per trovare 3 cluster (es. clima secco, temperato, umido)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Microclima_Cluster'] = kmeans.fit_predict(X_cluster)

    print("Campi raggruppati in Microclimi in base ai dati ambientali:")
    # Mostriamo solo le prime righe per dimostrare che il clustering è avvenuto
    print(df[['temperatura', 'umidita', 'Microclima_Cluster']].head(5))
    
    print("Centroidi dei cluster (Temp, Umidità, Pioggia):")
    for i, center in enumerate(kmeans.cluster_centers_):
        print(f"Cluster {i}: T={center[0]:.1f}°C, U={center[1]:.1f}%, P={center[2]:.1f}mm")
    
    print("-" * 50)

if __name__ == "__main__":
    run_unsupervised_learning()