import os
import requests
import json

NOTION_KEY = "secret_fBxcXbsIZImtvlpKPSVptXvEkLla1F9LWbOKQkomGEL"
headers = {'Authorization': f"Bearer {NOTION_KEY}",
           'Content-Type': 'application/json',
           'Notion-Version': '2022-06-28'}

search_params = {"filter": {"value": "page", "property": "object"}}
search_response = requests.post(f'https://api.notion.com/v1/search',
                                json=search_params, headers=headers)

# This gets the page data and pretty prints it

obj = search_response.json()
pretty_json = json.dumps(obj, indent=2)
print(pretty_json)





print("Total Cards Found: " + str(len(search_response.json()['results'])) + "\n")

print("Card Name {0:10} Lowest Price - M {0:4} Lowest Price - S {0:4} Price Difference\n".format(""))
for page in search_response.json()['results']:
    if 'Name' in page['properties']:
        name = page['properties']['Name']['title'][0]['text']['content'].strip("")
        price_m = ("%0.2f" %page['properties']['Price - M']['number'])
        price_s = ("%0.2f" %page['properties']['Price - S']['number'])
        difference = ("+%0.2f" %(float(price_s) - float(price_m)))
        print("{0:<15} {1:>14} {2:>21} {3:>20}".format(name,price_m,price_s,difference))

print("")
EndMessage = input("End of Data")
