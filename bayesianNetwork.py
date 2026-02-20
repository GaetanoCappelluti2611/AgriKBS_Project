# bayesianNetwork.py
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def run_probabilistic_reasoning():
    print("--- Avvio Ragionamento Probabilistico (Rete Bayesiana) ---")
    
    # Definisco la struttura della rete usando la nuova classe aggiornata
    model = DiscreteBayesianNetwork([('Meteo', 'Umidita'), ('Umidita', 'RischioFungo')])

    # Probabilità a priori del Meteo (0: Sereno, 1: Piovoso)
    cpd_meteo = TabularCPD(variable='Meteo', variable_card=2, values=[[0.7], [0.3]])

    # Probabilità Condizionata: Umidità data il Meteo (0: Bassa, 1: Alta)
    cpd_umidita = TabularCPD(variable='Umidita', variable_card=2, 
                             values=[[0.8, 0.2],  # P(Umidità Bassa | Meteo Sereno/Piovoso)
                                     [0.2, 0.8]], # P(Umidità Alta | Meteo Sereno/Piovoso)
                             evidence=['Meteo'], evidence_card=[2])

    # Probabilità Condizionata: RischioFungo data l'Umidità (0: Basso, 1: Alto)
    cpd_rischio = TabularCPD(variable='RischioFungo', variable_card=2,
                             values=[[0.9, 0.3],  # P(Rischio Basso | Umidità Bassa/Alta)
                                     [0.1, 0.7]], # P(Rischio Alto | Umidità Bassa/Alta)
                             evidence=['Umidita'], evidence_card=[2])

    model.add_cpds(cpd_meteo, cpd_umidita, cpd_rischio)
    model.check_model()

    # Inferenza
    infer = VariableElimination(model)
    
    # Calcoliamo la probabilità di rischio fungo sapendo che piove (Meteo=1)
    q = infer.query(variables=['RischioFungo'], evidence={'Meteo': 1})
    print("Probabilità di Rischio Malattia Fungina sapendo che è Piovoso:")
    print(q)
    print("-" * 50)

if __name__ == "__main__":
    run_probabilistic_reasoning()