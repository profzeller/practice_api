import requests
import pprint

url = "https://sandbox.zestfuldata.com/parseIngredients"

payload = {}
headers = {
	"Content-Type": "application/json"
}
data = {
    "ingredients": ["ham"]
}

response = requests.post(url, json=data, headers=headers)

data = response.json()

pprint.pprint(data)

confidence = data['results'][0]['confidence']

usdaInfo = data['results'][0]['ingredientParsed']['usdaInfo']


for k,v in usdaInfo.items():
    print(f'{k}: {v}')
