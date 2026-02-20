# supervisedLearning.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

def run_supervised_learning():
    print("--- Avvio Machine Learning Supervisionato ---")
    
    # Caricamento del dataset
    try:
        df = pd.read_csv("dataset_agri.csv")
    except FileNotFoundError:
        print("Errore: dataset_agri.csv non trovato.")
        return

    # Features (X) e Target (y)
    X = df.drop('resa_raccolto_kg', axis=1)
    y = df['resa_raccolto_kg']

    # Modello: Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Valutazione rigorosa tramite K-Fold (come da linee guida: tabelle mediate su più run, dev. standard)
    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    
    # Usiamo il Mean Absolute Error (MAE) come metrica (in negativo per convenzione sklearn)
    scores = cross_val_score(model, X, y, cv=kf, scoring='neg_mean_absolute_error')
    mae_scores = -scores

    print(f"Modello addestrato: {model.__class__.__name__}")
    print(f"Risultati MAE sui vari fold: {np.round(mae_scores, 2)}")
    print(f"MAE Medio: {np.mean(mae_scores):.2f} Kg")
    print(f"Deviazione Standard MAE: {np.std(mae_scores):.2f} Kg")
    print("-" * 50)

if __name__ == "__main__":
    run_supervised_learning()