# Medical IoT (mIoT) Security Risk Analyzer 🩺🛡️

An interactive prototype built during a hackathon at HIT to simulate and visualize cybersecurity vulnerability assessments for critical Medical IoT devices (such as pacemakers, insulin pumps, and patient monitors).

## 🚀 The Mission
Security in connected medical devices is a matter of life and death. This tool simulates an automated system where a technician or healthcare provider inputs a device's unique **User/Device ID** to pull real-time security configurations, calculating an interactive risk/vulnerability percentage profile.

## 🛠️ Tech Stack
- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** HTML5, CSS3 (Custom SVG animations), JavaScript (Fetch API)
- **Database:** Flat-file Mock DB (`db.txt`)

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/The3rdNinja/HIThackathon-medical-IOT-security
   cd medical-iot-security-analyzer
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
```
3. Run the Flask server:
  ```bash
  python server.py
