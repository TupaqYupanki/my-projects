import requests
import json
# resp = requests.get("https://api.originsro.org/api/v1/ping")
# print(resp.status_code)
# print(resp.json())
# test = requests.get("https://api.originsro.org/api/v1/whoami?api_key=utexehpdlrachyfbbsqgslgeemy7q2zm")
# print(test.status_code)
# print(test.json())

# items = requests.get("https://api.originsro.org/api/v1/items/list?api_key=utexehpdlrachyfbbsqgslgeemy7q2zm")
market = requests.get("https://api.originsro.org/api/v1/market/list?api_key=utexehpdlrachyfbbsqgslgeemy7q2zm")

# items_json = items.json()
# items_json_str = json.dumps(items_json)

market_json = market.json()
market_json_str = json.dumps(market_json)

# with open('items.json', 'w') as outfile:
#     outfile.write(items_json_str)

with open('market.json', 'w') as outfile:
    outfile.write(market_json_str)
