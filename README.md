# AgriKBS - Sistema Ibrido per l'Agricoltura di Precisione 

**Insegnamento:** Ingegneria della Conoscenza  
**Anno Accademico:** [2025/2026]  
**Gruppo di Progetto:** [Cappelluti Gaetano] [Gadaleta Roberto]

---

##  Descrizione del Progetto

**AgriKBS** è un prototipo di Knowledge-Based System (KBS) sviluppato per il dominio dell'agricoltura di precisione. Il sistema supporta il processo decisionale per la diagnosi di fitopatologie e la stima della resa agricola. 

Per garantire una copertura completa delle tecniche di Ingegneria della Conoscenza, il progetto adotta un **approccio ibrido** che integra tre paradigmi fondamentali:

1. **Rappresentazione e Ragionamento Logico (Prolog):** Una Knowledge Base che modella le relazioni tra colture, condizioni ambientali e patologie, permettendo al sistema di dedurre i rischi e suggerire trattamenti tramite ragionamento simbolico.
2. **Ragionamento Probabilistico (Reti Bayesiane):** Un modulo per la gestione dell'incertezza climatica che calcola la probabilità di proliferazione fungina in base a evidenze parziali sul meteo.
3. **Apprendimento Automatico (Machine Learning):** L'utilizzo di dati ambientali simulati (IoT) per esplorare microclimi tramite clustering (*Unsupervised Learning*) e predire la resa del raccolto tramite Random Forest (*Supervised Learning*), valutato rigorosamente tramite K-Fold Cross Validation.

---

## Struttura della Repository

Il progetto è suddiviso in moduli specializzati orchestrati da un controller principale:

* `main.py` : Controller principale che orchestra i tre moduli del KBS.
* `kb.pl` : Base di Conoscenza scritta in Prolog (Background Knowledge e regole di inferenza).
* `bayesianNetwork.py` : Modulo per il ragionamento in condizioni di incertezza (pgmpy).
* `unsupervisedLearning.py` : Modulo di clustering (K-Means) per l'individuazione di microclimi.
* `supervisedLearning.py` : Modulo predittivo (Random Forest) valutato con K-Fold CV.
* `dataset_agri.csv` : Dataset simulato contenente i dati dei sensori ambientali.
* `requirements.txt` : Lista delle librerie Python necessarie.
* `Documentazione.pdf` : Relazione completa con le decisioni di progetto e l'analisi dei risultati.

---

##  Requisiti e Installazione

Per eseguire il progetto è necessario avere installato **Python 3.8+** e **SWI-Prolog** (necessario per il funzionamento della libreria `pyswip`).

### 1. Installazione di SWI-Prolog
Assicurati di aver installato SWI-Prolog sul tuo sistema operativo e che sia stato aggiunto al PATH di sistema:
* **Windows/Mac:** Scarica l'installer da [swi-prolog.org](https://www.swi-prolog.org/download/stable)
* **Linux (Ubuntu):** `sudo apt-get install swi-prolog`

### 2. Installazione delle dipendenze Python
Clona la repository e installa i pacchetti richiesti:

```bash
git clone https://github.com/GaetanoCappelluti2611/AgriKBS_Project.git
cd AgriKBS_Project
pip install -r requirements.txt
