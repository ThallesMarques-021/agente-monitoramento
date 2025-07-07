import time, requests, subprocess
import psycopg2
from datetime import datetime

sites = ["google.com", "youtube.com", "rnp.br"]

def ping(host):
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    latency = 0.0
    loss = 0
    for line in result.stdout.splitlines():
        if "Average" in line:
            parts = line.split()
            latency = float(parts[-1].replace("ms", "").replace(",", ""))
        if "Lost" in line:
            loss = int(line.split(",")[2].split()[0])
    return latency, loss

def check_site(url):
    try:
        start = time.time()
        response = requests.get(f"https://{url}", timeout=5)
        load_time = time.time() - start
        return response.status_code, load_time
    except:
        return None, None

conn = psycopg2.connect(host="db", dbname="monitoring", user="user", password="pass")
cur = conn.cursor()

while True:
    for site in sites:
        latency, loss = ping(site)
        status, load_time = check_site(site)
        timestamp = datetime.now()

        cur.execute("INSERT INTO network_monitor (host, latency, load_time, status_code, packet_loss, timestamp) VALUES (%s, %s, %s, %s, %s, %s)",
                    (site, latency, load_time, status, loss, timestamp))
        conn.commit()
    time.sleep(60)