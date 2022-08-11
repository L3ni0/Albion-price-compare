import requests
import json

r = requests.get("https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.json")

f = json.loads(r.content)

with open('names.txt', 'w', encoding='utf-8') as to_save:
    for name in f:
        if name['LocalizedNames'] and name['UniqueName'][0] == 'T' and not 'CONTRACT' in name['UniqueName']:
            to_save.write(f"{name['UniqueName']},{name['LocalizedNames']['PL-PL']}\n")

end = input('done, press any key to end')