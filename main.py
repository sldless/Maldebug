import requests

key_search = str(input('What Anime?: '))

json = requests.get(f'https://myanimelist.net/search/prefix.json?type=anime&keyword={key_search}&v=1').json()
output = [i for i in json['categories'][0]['items']]
for i in output: 
  print(f'\nName: {i["name"]}\nID: {i["id"]}\nType: {i["payload"]["media_type"]}\nURL: {i["url"]}\nStatus: {i["payload"]["status"]}\nScore: {i["payload"]["score"]}\nAired: {i["payload"]["aired"]}\n')