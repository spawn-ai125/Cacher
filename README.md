<div align="center">

# 🛡️ Cacher (Vulnerability Scanner v1.0.0)

<p align="center">
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="Security">
  <img src="https://shields.io" alt="Developer">
</p>

<h4>An automated lightweight security scanner built in Python to discover information disclosure and Stored XSS vulnerabilities.</h4>

---
</div>

### 📖 Description
**Cacher** is a dual-stage automated penetration testing tool designed for security researchers and ethical hackers. It helps identify critical misconfigurations and vulnerabilities on target servers with speed and precision.

---

### 🚀 Key Features

<table>
  <tr>
    <td>📂 <b>Stage 1: Information Disclosure</b></td>
    <td>Scans for sensitive, hidden, or forgotten backup files (`.env`, `.git`, logs) that could expose infrastructure secrets.</td>
  </tr>
  <tr>
    <td>💉 <b>Stage 2: Stored XSS Verification</b></td>
    <td>Injects custom HTML/JavaScript payloads into specified parameters and intelligently verifies vulnerability by checking if the payload reflects in the server response body.</td>
  </tr>
  <tr>
    <td>🛠️ <b>Smart URL Handling</b></td>
    <td>Automatically normalizes prefixes (`http://`, `https://`) and strips trailing slashes to prevent syntax errors.</td>
  </tr>
</table>

---

### 💻 Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com

# Navigate to the project directory
cd Cacher

# Install required library
pip install requests
```

---

### 🎯 Usage

Simply execute the script using Python 3 and follow the interactive prompt:

```bash
python cacher.py
```

1. **Target URL:** Enter the full web application address (e.g., `https://example.com`).
2. **Parameter:** Provide the input field name you wish to test for XSS (e.g., `comment`, `message`, `search`).

---

### ⚠️ Disclaimer
This tool is developed strictly for **educational and authorized security testing purposes**. Running this tool against targets without prior written consent is illegal. The developer (4B2A) assumes no liability and is not responsible for any misuse or damage caused by this program.

---

<div align="center">
  <sub>Coded with ❤️ by <b>4B2A</b> | Version 1.0.0 </sub>
</div>
