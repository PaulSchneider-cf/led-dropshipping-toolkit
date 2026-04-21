#!/usr/bin/env python3
"""
LED Dropshipping - Produktbeschreibungs-Generator
Generiert SEO-optimierte Produktbeschreibungen fuer deutsche Shopify-Shops
"""

import csv
import random
from datetime import datetime

PRODUCTS = [
    {"name": "RGB LED Strip 5m", "keywords": ["LED Strip", "RGB Beleuchtung", "Smart LED"], "einkauf_preis": 4.50, "kategorie": "LED Strips"},
    {"name": "Smart LED Strip WiFi 10m", "keywords": ["WiFi LED", "Smart Home", "Alexa LED"], "einkauf_preis": 8.90, "kategorie": "Smart LED"},
    {"name": "LED Streifen Fernbedienung 3m", "keywords": ["LED Streifen", "Fernbedienung", "Deko Licht"], "einkauf_preis": 3.20, "kategorie": "LED Strips"},
    {"name": "RGBIC LED Strip Neon 2m", "keywords": ["RGBIC LED", "Neon Beleuchtung", "Gaming Zimmer"], "einkauf_preis": 6.80, "kategorie": "Gaming LED"},
    {"name": "LED Unterbauleuchte Kueche 1m", "keywords": ["Unterbauleuchte", "Kuechen LED", "Schrankbeleuchtung"], "einkauf_preis": 2.80, "kategorie": "Kuechen LED"},
    {"name": "LED TV Hintergrundbeleuchtung 55 Zoll", "keywords": ["TV LED", "Bias Lighting", "Ambilight"], "einkauf_preis": 3.90, "kategorie": "TV LED"},
    {"name": "LED Strip Wasserdicht Outdoor 5m", "keywords": ["Outdoor LED", "Garten Beleuchtung", "IP65 LED"], "einkauf_preis": 5.60, "kategorie": "Outdoor LED"},
    {"name": "LED Lichterkette USB 3m", "keywords": ["Lichterkette USB", "Fairy Lights", "Stimmungslicht"], "einkauf_preis": 1.90, "kategorie": "Lichterketten"},
    {"name": "RGB Neon Flex Strip 5m", "keywords": ["Neon Flex", "Neon LED", "Neon Sign"], "einkauf_preis": 9.50, "kategorie": "Neon LED"},
    {"name": "COB LED Strip Ultra-Bright 5m", "keywords": ["COB LED", "High Density LED", "Linear Beleuchtung"], "einkauf_preis": 7.20, "kategorie": "COB LED"},
]

TEMPLATES = [
    "Verwandle dein Zuhause mit unserem {name}! Hochwertige LED-Loesung mit lebendigen Farben. Perfekt fuer Schlafzimmer, Wohnzimmer oder Gaming-Setup. Einfache Installation in wenigen Minuten - einfach aufkleben und geniessen! Energiesparend mit 50.000+ Betriebsstunden.",
    "Erlebe brillante Beleuchtung mit dem {name}. Modernste LED-Technologie mit praectigen Farben. Ideal als Ambient-Beleuchtung hinter TV, Bett oder Schreibtisch. Integrierter Klebestreifen fuer sicheren Halt auf allen glatten Oberflaechen.",
    "Der {name} ist das perfekte Upgrade! Millionen Farbkombinationen fuer jeden Anlass. Ruhiges Weisslicht zum Arbeiten oder dynamische Farbwechsel fuer die Party. Per App oder Fernbedienung gesteuert.",
]

FEATURES = [
    "Selbstklebend - keine Werkzeuge noetig",
    "16 Millionen Farboptionen",
    "Energiesparend - 80% weniger Strom",
    "50.000+ Betriebsstunden Lebensdauer",
    "Zuschneidbar alle 3 LEDs",
    "Alexa & Google Assistant kompatibel",
    "App-Steuerung per Smartphone",
    "Inkl. Netzteil und Fernbedienung",
    "CE und RoHS zertifiziert",
    "12 Monate Garantie",
]

def berechne_vk(ek, marge=0.65):
    return round(ek / (1 - marge) - 0.01, 2)

def generiere_beschreibung(produkt):
    text = random.choice(TEMPLATES).format(name=produkt["name"])
    features = random.sample(FEATURES, 4)
    return text + "\n\nHighlights:\n" + "\n".join(f"- {f}" for f in features)

def export_shopify_csv(produkte, datei="shopify_import.csv"):
    felder = ["Handle","Title","Body (HTML)","Vendor","Type","Tags","Published",
              "Variant Price","Variant Compare At Price","Variant Requires Shipping",
              "Variant Taxable","Status"]
    with open(datei, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=felder)
        w.writeheader()
        for p in produkte:
            handle = p["name"].lower().replace(" ", "-")
            vk = berechne_vk(p["einkauf_preis"])
            w.writerow({
                "Handle": handle,
                "Title": p["name"],
                "Body (HTML)": f"<p>{generiere_beschreibung(p)}</p>",
                "Vendor": "LightCraft DE",
                "Type": p["kategorie"],
                "Tags": ", ".join(p["keywords"]),
                "Published": "true",
                "Variant Price": vk,
                "Variant Compare At Price": round(vk * 1.3, 2),
                "Variant Requires Shipping": "true",
                "Variant Taxable": "true",
                "Status": "active"
            })
    return datei

def preisanalyse():
    print("=" * 55)
    print("PREISANALYSE - LED Dropshipping")
    print("=" * 55)
    print(f"{'Produkt':<30} {'EK':>5} {'VK':>7} {'Gewinn':>7}")
    print("-" * 55)
    for p in PRODUCTS:
        ek = p["einkauf_preis"]
        vk = berechne_vk(ek)
        gewinn = vk - ek
        print(f"{p['name'][:28]:<30} {ek:>4.2f}E {vk:>6.2f}E {gewinn:>6.2f}E")
    print("=" * 55)

if __name__ == "__main__":
    print(f"LED Dropshipping Generator - {datetime.now():%d.%m.%Y}")
    preisanalyse()
    csv_datei = export_shopify_csv(PRODUCTS)
    print(f"\nShopify CSV erstellt: {csv_datei}")
    print(f"{len(PRODUCTS)} Produkte exportiert!")
    print("\nNaechste Schritte:")
    print("1. shopify_import.csv in Shopify hochladen")
    print("2. Bilder von AliExpress hinzufuegen")
    print("3. Produktpreise nach Markt anpassen")
