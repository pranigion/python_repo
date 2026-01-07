import requests
url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)
result = response.json()
print(result)