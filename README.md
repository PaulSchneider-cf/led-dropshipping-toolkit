# LED Dropshipping Toolkit

**Automatisiertes Dropshipping-System fuer LED Beleuchtung auf dem deutschen Markt**

---

## Nische & Marktanalyse

**Warum LED Beleuchtung?**
- Google Trends DE: konstant 50-100 Punkte (letzten 90 Tage)
- Breite Zielgruppe: Gaming, Wohnen, Kueche, Outdoor, Auto
- Niedrige Einkaufspreise (2-10 EUR) - hohe Margen (60-70%)
- Einfacher Versand: leicht, klein, kein Zerbrechlichkeitsrisiko
- Wiederholkaeufe: Kunden kaufen mehrere Strips

**Zielgruppe:**
- Gamer (RGB Setup)
- Heimwerker & Interior-Fans
- TikTok / Instagram - Deko-Trend

---

## Produkte & Margen

| Produkt | Einkauf (AliExpress) | Verkauf | Gewinn |
|---------|---------------------|---------|--------|
| RGB LED Strip 5m | 4,50 EUR | 12,84 EUR | 8,34 EUR |
| Smart LED Strip WiFi 10m | 8,90 EUR | 25,42 EUR | 16,52 EUR |
| LED Streifen Fernbedienung 3m | 3,20 EUR | 9,13 EUR | 5,93 EUR |
| RGBIC LED Strip Neon 2m | 6,80 EUR | 19,42 EUR | 12,62 EUR |
| LED Unterbauleuchte Kueche 1m | 2,80 EUR | 7,99 EUR | 5,19 EUR |
| LED TV Hintergrund 55 Zoll | 3,90 EUR | 11,13 EUR | 7,23 EUR |
| LED Strip Wasserdicht Outdoor 5m | 5,60 EUR | 15,99 EUR | 10,39 EUR |
| LED Lichterkette USB 3m | 1,90 EUR | 5,42 EUR | 3,52 EUR |
| RGB Neon Flex Strip 5m | 9,50 EUR | 27,13 EUR | 17,63 EUR |
| COB LED Strip Ultra-Bright 5m | 7,20 EUR | 20,56 EUR | 13,36 EUR |

**Durchschnittliche Marge: ~65%**

---

## Setup - Schritt fuer Schritt

### Schritt 1: Shopify Store erstellen
1. shopify.com > "Kostenlos testen" (3 Tage gratis, dann ~30 EUR/Monat)
2. Store-Name: z.B. "LightCraft.de" oder "SmartLEDs.de"
3. Theme: Dawn (kostenlos) oder Sense (kostenlos)
4. Zahlungsmethoden aktivieren: PayPal + Shopify Payments

### Schritt 2: Domain registrieren
- Empfehlung: ionos.de oder namecheap.com
- Kosten: ~1-2 EUR/Jahr fuer .de Domain
- Vorschlaege: smartled-shop.de / ledwelt-shop.de / rgb-beleuchtung.de

### Schritt 3: Produkte importieren
```bash
# Python 3 installieren, dann:
python product_generator.py
# Erzeugt: shopify_import.csv
```
CSV in Shopify importieren: Admin > Produkte > Importieren

### Schritt 4: AliExpress Lieferanten
- CJ Dropshipping (cjdropshipping.com) - DE Lager verfuegbar!
- DSers (dsers.com) - direkter AliExpress Import in Shopify
- Versandzeit mit CJ aus DE: 3-7 Tage

### Schritt 5: Marketing (kostenlos starten)
1. **TikTok**: LED Raumbeleuchtung Videos -> viral potential
2. **Pinterest**: Zimmer-Deko Boards
3. **Instagram Reels**: Vorher/Nachher Videos
4. **Google Shopping**: Ab 50 EUR Budget

---

## Dateien in diesem Repo

| Datei | Beschreibung |
|-------|-------------|
| `product_generator.py` | Generiert Produktbeschreibungen + Shopify CSV |
| `shopify_import.csv` | (wird generiert) Shopify-Import Datei |

---

## Schnellstart

```bash
# 1. Repo klonen
git clone https://github.com/PaulSchneider-cf/led-dropshipping-toolkit.git
cd led-dropshipping-toolkit

# 2. Produkte generieren
python product_generator.py

# 3. CSV in Shopify importieren
# Admin > Produkte > Mehr Aktionen > Produkte importieren
```

---

## Ziele

- [ ] Shopify Store erstellen
- [ ] Domain registrieren
- [ ] Erste 10 Produkte live
- [ ] Erste TikTok Videos
- [ ] Erste Bestellung erhalten
- [ ] Break-even erreichen

---

*Erstellt am 22.04.2026 - LED Dropshipping Projekt DE*
