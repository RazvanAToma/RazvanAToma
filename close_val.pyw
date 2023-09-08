import psutil
import subprocess
import time

process_to_kill = "VALORANT-Win64-Shipping.exe"

while True:
    if "VALORANT-Win64-Shipping.exe" in (p.name() for p in psutil.process_iter()):
        print(f"{process_to_kill} is running")
        subprocess.call("TASKKILL /F /IM VALORANT-Win64-Shipping.exe", shell=True)
        print(f"{process_to_kill} killed")
        time.sleep(120)
    else:
        print(f"{process_to_kill} is not running")
        time.sleep(120)

