import requests
url = "https://pokeapi.co/api/v2/pokemon"
total_count = requests.get(url).json().get("count")
# print(total_count)
full_response =[]

for i in range(0,total_count,20):
    paginated_url = f"{url}?offset={i}&limit=20"
    result = requests.get(paginated_url)
    data = result.json()
    full_response.append(data)

print(len(full_response))
