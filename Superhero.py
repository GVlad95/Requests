import requests

heroes_data = requests.get('https://akabab.github.io/superhero-api/api//all.json').json()
heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes_data))
hero_int = {hero['name']: hero['powerstats']['intelligence'] for hero in heroes}
max_int = max(hero_int, key=hero_int.get)
most_int_hero = f'Наибольшим интеллектом среди всех супергероев обладает {max_int}'
print(most_int_hero)
