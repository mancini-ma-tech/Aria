import time
import random
import csv
import os  # Necessario per gestire i file nel sistema operativo
from datetime import datetime

# --- CONFIGURAZIONE ---
SOGLIA_BPM_ALTO = 110
SOGLIA_HRV_BASSO = 20
SOGLIA_HRV_OTTIMO = 60
FILE_LOG = "aria_history.csv" # Nome del file dove salveremo i dati

class BiosensorSimulator:
    """Genera dati casuali per testare il sistema."""
    def get_readings(self):
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Formato completo data+ora
            "bpm": random.randint(55, 120),
            "hrv": random.randint(10, 100)
        }

class DataLogger:
    """
    MODULO NUOVO: Gestisce la persistenza dei dati.
    Salva le letture su un file CSV (compatibile con Excel).
    """
    def __init__(self, filename):
        self.filename = filename
        self.initialize_file()

    def initialize_file(self):
        # Se il file non esiste, lo creiamo e scriviamo l'intestazione (le colonne)
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "BPM", "HRV", "Stato Rilevato"]) # Intestazioni
            print(f"📁 Creato nuovo file di log: {self.filename}")

    def log_data(self, data, status):
        # Apre il file in modalità 'append' (a) per aggiungere righe senza cancellare le vecchie
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([data['timestamp'], data['bpm'], data['hrv'], status])

class AlertSystem:
    """Gestisce le notifiche a schermo."""
    def send_alert(self, level, message):
        icons = {"INFO": "ℹ️", "WARNING": "⚠️", "CRITICAL": "🚨"}
        print(f"\n{icons.get(level, '')} [{level}] {message}")

class AriaEngine:
    """Il cervello che analizza e coordina il salvataggio."""
    def __init__(self):
        self.alert_system = AlertSystem()
        self.logger = DataLogger(FILE_LOG) # Inizializza il logger

    def analyze(self, data):
        bpm = data['bpm']
        hrv = data['hrv']
        status = "Normale"
        
        # Logica di Analisi
        if bpm > SOGLIA_BPM_ALTO:
            self.alert_system.send_alert("CRITICAL", f"Battito elevato ({bpm} BPM).")
            status = "Agitazione"
        elif hrv < SOGLIA_HRV_BASSO:
            self.alert_system.send_alert("WARNING", f"Stress in aumento (HRV: {hrv}).")
            status = "Stress"
        elif hrv > SOGLIA_HRV_OTTIMO and bpm < 70:
            status = "Relax"

        # Output a schermo
        print(f"[{data['timestamp']}] ❤️ {bpm} | ⚡ {hrv} | Stato: {status}")
        
        # SALVATAGGIO: Scriviamo nel "diario" di Aria
        self.logger.log_data(data, status)

# --- MAIN ---
def main():
    print("🌌 ARIA System v1.1 - Logging Attivo")
    print(f"I dati verranno salvati in: {os.path.abspath(FILE_LOG)}\n")
    
    sensor = BiosensorSimulator()
    aria = AriaEngine()

    try:
        while True:
            data = sensor.get_readings()
            aria.analyze(data)
            time.