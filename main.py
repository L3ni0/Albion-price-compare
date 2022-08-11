from compare_func import *
import pandas as pd
import requests
import json
url = r'https://www.albion-online-data.com/api/v2/stats/prices/'

with open('names.txt', 'r',encoding='utf-8') as names: #open files with all items indexes and names
    data = []
    while name:=names.readline():
        item_index, pl_name = name.strip().split(',')
        r = requests.get(url+item_index)

        try:
            price_data = json.loads(r.content)
        except:
            continue

        best = profits_of_item(price_data,pl_name)
        #if we haven't much information return = None
        if best != [None]:
            data.extend(best)
            print(best)



    df = pd.DataFrame(data)
    df.sort_values(by='profit',ascending=False, inplace=True)
    html = df.to_html()

    text_file = open("index.html", "w")
    text_file.write(html)
    text_file.close()

    message = input('process finished! :D')
        