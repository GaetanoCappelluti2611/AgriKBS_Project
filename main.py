# main.py
from pyswip import Prolog
import bayesianNetwork
import unsupervisedLearning
import supervisedLearning

def query_knowledge_base():
    print("--- Avvio Ragionamento Logico (Prolog KB) ---")
    prolog = Prolog()
    
    # Carica il file Prolog creato in precedenza
    try:
        prolog.consult("kb.pl")
    except Exception as e:
        print("Impossibile caricare kb.pl. Assicurati che il file sia nella directory.")
        return

    # Eseguiamo un'inferenza: Quali colture sono a rischio peronospora?
    print("Ricerca delle colture a rischio 'peronospora' tramite inferenza logica:")
    rischi = list(prolog.query("rischio_patologia(Coltura, peronospora)"))
    
    if rischi:
        for r in rischi:
            print(f"- La coltura {r['Coltura']} è a rischio peronospora in base alle regole meteo/sintomi.")
            # Chiediamo al sistema un trattamento suggerito
            trattamenti = list(prolog.query(f"suggerimento_trattamento({r['Coltura']}, Trattamento)"))
            for t in trattamenti:
                print(f"  -> Trattamento suggerito dalla KB: {t['Trattamento']}")
    else:
        print("Nessun rischio rilevato al momento.")
    print("-" * 50)

def main():
    print("=" * 60)
    print(" INIZIALIZZAZIONE AGRIKBS - KNOWLEDGE BASED SYSTEM")
    print("=" * 60)
    
    # 1. Modulo Logico-Simbolico (Rappresentazione e Ragionamento)
    query_knowledge_base()
    
    # 2. Modulo Probabilistico (Gestione dell'incertezza)
    bayesianNetwork.run_probabilistic_reasoning()
    
    # 3. Modulo di Apprendimento Non Supervisionato (Clustering / Esplorazione)
    unsupervisedLearning.run_unsupervised_learning()
    
    # 4. Modulo di Apprendimento Supervisionato (Predizione)
    supervisedLearning.run_supervised_learning()

    print("=" * 60)
    print(" ESECUZIONE COMPLETATA CON SUCCESSO")
    print("=" * 60)

if __name__ == "__main__":
    main()