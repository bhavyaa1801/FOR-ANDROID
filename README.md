# FORANDROID

An AI-enhanced tool for investigating internal leaks from Android devices using OSINT & forensics.

## Overview

FORANDROID analyzes DNS logs and network activity extracted from Android devices to detect suspicious communication patterns and potential data leaks through comprehensive IP enrichment and machine learning-based anomaly detection.

---

## Key Features

- Parse DNS logs from Android devices via ADB
- Resolve domains to IPs with WHOIS & GeoIP enrichment
- ML-based suspicious activity detection (RandomForest)
- Geographic mapping and timeline generation
- Source IP to ASN and country mapping

---

## Installation

bash
git clone https://github.com/yourusername/FORANDROID.git
cd FORANDROID
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

## Usage

bash
streamlit run streamlit_ui/launch.py


Follow the UI workflow: Create case → Extract logs → Parse DNS → Resolve domains → Run ML analysis → View results

---

## Tech Stack

*Core:* Python, Streamlit, ADB  
*Analysis:* Pandas, RandomForest, Isolation Forest  
*Tools:* Nmap, WHOIS, GeoIP

## Project Structure

FORANDROID/
├── Home.py
├── app/
│   └── pages/
│       ├── extract_logs.py
│       ├── dns_parser.py
│       ├── model_ai.py
│       ├── enrich_ip.py
│       └── network_analysis.py
├── case_files/
│   └── CASE001/
│       ├── raw_logs/
│       └── processed/
├── requirements.txt



## Contributors

*Bhavya Rajput* – Lead Developer  
*IGDTUW* – Institutional Support
