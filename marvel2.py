import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
heroes = response.json()

print("Marvel Superheroes:\n")
for hero in heroes:
    if hero['biography']['publisher'] == "Marvel Comics":
        print(hero['name'])
