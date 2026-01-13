import time
import random
from datetime import datetime

# --- CONFIGURAZIONE ---
# Soglie di base (in un sistema reale, queste sarebbero adattive/apprese dall'AI)
SOGLIA_BPM_ALTO = 110       # Battiti per minuto
SOGLIA_HRV_BASSO = 20       # Heart Rate Variability (ms) - Basso = Stress
SOGLIA_HRV_OTTIMO = 60      # Alto = Relax/Recupero

class BiosensorSimulator:
    """
    Simula un dispositivo indossabile (es. Smartwatch).
    Genera dati casuali realistici per testare il sistema.
    """
    def get_readings(self):
        # Simuliamo: BPM (Battito) e HRV (Variabilità del battito)
        # Nota: In situazioni di stress, il BPM sale e l'HRV scende.
        return {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "bpm": random.randint(55, 120),    # Range realistico a riposo/attività leggera
            "hrv": random.randint(10, 100)     # Range in millisecondi
        }

class AlertSystem:
    """
    Gestisce le notifiche all'utente.
    """
    def send_alert(self, level, message):
        icons = {"INFO": "ℹ️", "WARNING": "⚠️", "CRITICAL": "🚨"}
        print(f"\n{icons.get(level, '')} [{level}] {message}")

class AriaEngine:
    """
    Il cuore dell'intelligenza artificiale.
    Analizza i dati grezzi e cerca pattern.
    """
    def __init__(self):
        self.alert_system = AlertSystem()
        self.history = [] # Memoria a breve termine

    def analyze(self, data):
        bpm = data['bpm']
        hrv = data['hrv']
        
        # Analisi Semplice (Rule-based)
        status = "Neutro"
        
        # 1. Controllo Battito Cardiaco (Anomalie immediate)
        if bpm > SOGLIA_BPM_ALTO:
            self.alert_system.send_alert("CRITICAL", f"Attenzione: Battito cardiaco elevato rilevato ({bpm} BPM).")
            status = "Agitazione Fisica"
        
        # 2. Controllo Stress basato su HRV (Motore Predittivo Semplificato)
        elif hrv < SOGLIA_HRV_BASSO:
            self.alert_system.send_alert("WARNING", f"Livello di Stress in aumento (HRV: {hrv}ms). Consigliata pausa respiratoria.")
            status = "Stress Mentale"
            
        # 3. Rilevamento Recupero
        elif hrv > SOGLIA_HRV_OTTIMO and bpm < 70:
            status = "Stato di Calma Profonda"
            print(f"✨ Aria: Ottimo recupero rilevato. I parametri sono ideali.")

        # Log per il debug
        print(f
