% kb.pl - Knowledge Base per AgriKBS

% --- 1. TASSONOMIA E FATTI BASE (Questi verranno poi iniettati dinamicamente da Python) ---
% coltura(ID, Tipo).
coltura(c1, vite).
coltura(c2, pomodoro).

% meteo(ID_Coltura, Condizione).
meteo(c1, alta_umidita).
meteo(c1, pioggia_frequente).
meteo(c2, temp_elevata).
meteo(c2, siccita).

% sintomo(ID_Coltura, Sintomo).
sintomo(c1, macchie_gialle_foglie).
sintomo(c1, muffa_bianca).
sintomo(c2, foglie_arricciate).

% --- 2. REGOLE DI INFERENZA (Background Knowledge) ---
% Regola per la Peronospora: colpisce la vite se c'è alta umidità, pioggia e macchie gialle.
rischio_patologia(Coltura, peronospora) :-
    coltura(Coltura, vite),
    meteo(Coltura, alta_umidita),
    meteo(Coltura, pioggia_frequente),
    sintomo(Coltura, macchie_gialle_foglie).

% Regola per l'Oidio: colpisce vite o pomodoro con temperature elevate e muffa bianca.
rischio_patologia(Coltura, oidio) :-
    (coltura(Coltura, vite) ; coltura(Coltura, pomodoro)),
    meteo(Coltura, temp_elevata),
    sintomo(Coltura, muffa_bianca).

% Regola per lo Stress Idrico: non è una malattia patogena, ma una condizione ambientale.
rischio_patologia(Coltura, stress_idrico) :-
    meteo(Coltura, siccita),
    sintomo(Coltura, foglie_arricciate).

% --- 3. REGOLE DI AZIONE / INTERVENTO ---
% Suggerisce un trattamento basato sulla patologia dedotta.
suggerimento_trattamento(Coltura, fungicida_rameico) :-
    rischio_patologia(Coltura, peronospora).

suggerimento_trattamento(Coltura, zolfo) :-
    rischio_patologia(Coltura, oidio).

suggerimento_trattamento(Coltura, irrigazione_emergenza) :-
    rischio_patologia(Coltura, stress_idrico).