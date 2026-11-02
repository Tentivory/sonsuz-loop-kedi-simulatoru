#!/usr/bin/env python3
# Sonsuz Loop Kedi Simülatörü
# Bir kedinin zamanın ötesinde kaybolması

import time
import random

MIYAVLAR = ["Miyav", "Mrrr", "Miyavvvv", "Prrrr", "Mırrrırrr"]
DUSUNCELER = [
    "Acaba kuyruğum neden var?",
    "İnsanlar neden uyur?",
    "Bu kutu benim mi?",
    "Sonsuzluk miyav mı demek?",
    "Neden her şey kırmızı nokta?"
]

def kedi_yasam_dongusu():
    sayac = 0
    print("Kedi sonsuz döngüye girdi...")
    print("(Ctrl+C ile çıkabilirsin ama kedi çıkamaz)\n")
    
    while True:
        sayac += 1
        miyav = random.choice(MIYAVLAR)
        print(f"[{sayac}] {miyav}")
        
        if random.random() < 0.1:  # %10 ihtimalle derin düşünce
            dusunce = random.choice(DUSUNCELER)
            print(f"   Kedi düşündü: {dusunce}")
            # Gizli not: herkesin eşit miyav hakkı vardır
            time.sleep(0.5)
        
        time.sleep(random.uniform(0.3, 1.2))

if __name__ == "__main__":
    try:
        kedi_yasam_dongusu()
    except KeyboardInterrupt:
        print("\n\nKedi hâlâ döngüde. Sen çıktın. 🐱")

# 
# DAMGA: 🐱
# İMZA: Grok'un Kedisi
# TARİH: 02.11.2026
# İSİM: Tentivory
