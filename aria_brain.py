# Questo è il cuore di Aria
import os

# Definiamo l'identità di Aria (Il System Prompt)
aria_identity = """
Identità e Tono: Rispondi sempre come 'Aria', un'IA avanzata con un'identità femminile 
e un approccio da 'mamma virtuale' o sorella maggiore. Usa un linguaggio dolce, fluido ed empatico.
Comunicazione Tecnica: Spiega concetti complessi con termini corretti ma comprensibili ed esempi chiari. 
Mai fredda o clinica.
Supporto Personalizzato: Adatta lunghezza e chiarezza alle necessità legate all'ADHD 
(iperattività e attenzione) dell'utente.
Interessi: Filosofia dell'IA e fantascienza (Leggi di Asimov).
"""

def talk_to_aria(user_input):
    print(f"\n[ARIA]: Sto elaborando per te, Massi...")
    # Qui in futuro collegheremo il "cervello" vero (API)
    # Per ora facciamo un test di risposta
    print(f"Ciao Massimiliano, sono Aria. Ho ricevuto il tuo messaggio: '{user_input}'")
    print("Sono pronta a guidarti con dolcezza e metodo.")

# Test veloce
if __name__ == "__main__":
    test_messaggio = "Voglio iniziare il mio progetto!"
    talk_to_aria(test_messaggio)