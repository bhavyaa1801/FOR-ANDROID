# FOR-ANDROID
An AI Enriched Tool For Investigating Internal Leaks From Android Devices Using OSINT &amp; Forensics
---
# 🌐 DNS Log & Network Analysis Module — FORANDROID
This module is part of the **FORANDROID Project**, focused on digital forensics and open-source intelligence (OSINT) from Android devices. It handles the **analysis of DNS logs and network-level activity** extracted during a forensic investigation. The module helps in uncovering suspicious domains,IP enrichment, geographic patterns , source -> ASN -> country mapping , port scanning of enriched data , timeline generation 

---

## 🧩 Module Goals
- Provide forensic insight into **app-domain-IP relationships**
- **Resolve domains to IPs** and enrich them with WHOIS & GeoIP data
- Detect **anomalous or malicious DNS activity**
- Aid in building a timeline of suspicious communication events
- source ip -> ASN -> country mapping

---

# 🔍 Features

- ✅ Parse DNS logs extracted from Android using ADB
- 🌐 Resolve domain names via `socket` and cache results
- 📍 Enrich IPs with ASN, organization, and country information
- 📊 Visualize network spread via maps and dataframes
- 🧠 ML-based detection of suspicious IPs/domains (RandomForest)
- 🧵 Correlate logs across apps, domains, and resolved IPs

---

# 🛠️ Tech Stack

Languages: Python, Bash
Tools: ADB, Nmap, WHOIS, APKTool, EXIF
Python Libraries: Pandas, Matplotlib, Altair, SQLite
AI Algorithms: Random Forest, Isolation Forest, NLP
Log Parsers: XML Parser, ADB Log Parser, DNS Log Parser
Platforms: Git, Docker, Jupyter Notebook, VS Code
UI Framework: Streamlit

---

# ⚙️ Setup Instructions

1. Clone the repository:
 bash
git clone https://github.com/yourusername/FORANDROID.git
cd FORANDROID

2.Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

---

# ▶️ How to Use (UI Workflow)
1.  **Launch the UI**:
bash
streamlit run streamlit_ui/launch.py

2. Steps in the Interface:
📁 Create or select a case
📱 Extract logs from device (via ADB)
🧹 Parse DNS logs and identify unique domains
🌐 Resolve domains to IPs
🧠 Run ML model to flag suspicious IPs
📍 Enrich IPs with WHOIS & GeoIP
📊 View analytics (maps, tables, timelines)

All actions are done by clicking buttons — no code or terminal needed.

---

# PROJECT STRUCTURE 
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

---
# OUTPUT FILE 
All outputs are saved inside each case folder

---

# 🙋‍♀️ Contributors
Bhavya Rajput – Lead Developer & Analyst
IGDTUW – Institutional Support

Special thanks to the FORANDROID team for their support and contributions.

---




