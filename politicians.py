from datetime import datetime
import requests
from os import path
from json import load


club_name = "PiS"

def update_data():
    url_api = 'http://api.sejm.gov.pl/sejm/term9/MP'
    status = 'database of deputies not downloaded'
    if path.exists('data.json'):
        now = datetime.now().weekday()
        current_date = datetime.now().date()
        modyfi_date = datetime.fromtimestamp(path.getmtime('data.json')).date()
        date_testing = str(current_date - modyfi_date)
        if now == (4 or 0) and date_testing != '0:00:00':
            data = requests.get(url_api)
            data.raise_for_status()
            with open("data.json", "w", encoding='utf-8') as f:
                f.write(data.text)
            status = 'database of deputies has been updated'
    else:
        data = requests.get(url_api)
        data.raise_for_status()
        with open("data.json", "w", encoding='utf-8') as f:
            f.write(data.text)
        status = 'database of deputies downloaded'
    return status



def get_deputies()->list:
#TODO: duplicated functionality ?
    i = 0
    deputies = []
    with open('data.json', 'r', encoding='utf8') as json_file:
        data = load(json_file)
        while i < len(data):
            if data[i]['active'] == True:
                _ = [data[i]['email'], data[i]['firstName'], data[i]['firstLastName']]
                deputies.append(_) if data[i]['club'] == club_name else ""
            i += 1

    return deputies


# print('-----\n\n', get_deputies(), ' ', type(get_deputies()), '-----\n\n')
# print(update_data())