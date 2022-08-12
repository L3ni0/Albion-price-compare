import json
import requests
import json
import pandas as pd
import install_rq

def best_proportion(price_data,pl_name=''):
    """function compare items prices between cities

    Args:
    price_data : JSON file of data from www.albion-online-data.com <- if u want to use this func ale bee sure u set quality

    Return:
    dict with the best profit and cities between like:

    {"name":"item" ,"profit":1234, "from":"city 1", "to":"city 2"}
    """

    best = {"name":"item", "quality":2 ,"profit":0, "from": "city 1", "to":"city 2","pl_name":''}

    # compare each profit with another
    for from_city in price_data:
        for to_city in price_data:
            if ((profit := (to_city['sell_price_min']*0.97) - from_city['sell_price_min']) > best['profit']) and not (from_city['city'].isdecimal() or from_city['city'].isdecimal()):
                
                best = {"name": from_city['item_id'],
                        "quality": from_city['quality'],
                        "profit": round(profit), 
                        "from": from_city['city'], 
                        "to": to_city['city'],
                        "pl_name":pl_name}
    
    if best['name'] == 'item':
        return

    return best


def profits_of_item(price_data,pl_name=''):
    """function compare items profits between cities

    Args:
    price_data : JSON file of data from www.albion-online-data.com 

    Return:
    list of dict with the best profit and cities between like:

    [{"name":"item" ,"profit":1234, "from":"city 1", "to":"city 2"},
    {"name":"item2" ,"profit":334....
    """
    list_of_item = [[],[],[],[],[],[]] #index in list mean quality
    for item in price_data:
        list_of_item[item['quality']].append(item)

    profits = []
    for to_compare in list_of_item:
        if len(to_compare) > 1:
            if (resoult := best_proportion(to_compare,pl_name)) != None: profits.append(resoult) 

    filtered = [item for item in list_of_item if item is not None]

    return profits

if __name__ == '__main__':
    url = "https://www.albion-online-data.com/api/v2/stats/prices/T4_BAG"
    r = requests.get(url)
    f = json.loads(r.content)
    data = profits_of_item(f)


    df = pd.DataFrame(data)
    df.sort_values(by='profit',ascending=False, inplace=True)
    html = df.to_html()

    text_file = open("index.html", "w")
    text_file.write(html)
    text_file.close()