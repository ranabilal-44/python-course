import requests
url = "https://www.superheroapi.com/api.php/b4ff3437ee65c6ae14a966f8f9aa83/search/a"
response = requests.get(url)
data = response.json()
print("data",data)