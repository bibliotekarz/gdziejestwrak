from datetime import datetime
import requests
from os import path
from json import load
from declension import declension_vocative
from random import choice

chosen = []
club_name = "PiS"

def update_data():
    url_api = 'http://api.sejm.gov.pl/sejm/term9/MP'
    status = 'init'
    if path.exists('data.json'):
        now = datetime.now().weekday()
        current_date = datetime.now().date()
        modyfi_date = datetime.fromtimestamp(path.getmtime('data.json')).date()
        date_testing = str(current_date - modyfi_date)
        status = 'database of deputies has not been changed'
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

print((update_data()))
#
def work_json() -> list:
    i = 0
    meps_data = []
    with open('data.json', 'r', encoding='utf8') as json_file:
        data = load(json_file)
        while i < len(data):
            if data[i]['active'] == True:
                _ = [data[i]['email'], data[i]['firstName'], data[i]['firstLastName']]
                meps_data.append(_) if data[i]['club'] == club_name else ""
            i += 1
    return meps_data

meps_data = work_json()
# print(meps_data, ' mepsdata')

def random_email(meps: list) -> list:
    chosen = choice(meps)
    vocative = declension_vocative(chosen[2])
    chosen.append(vocative)
    return chosen

chosen = random_email(meps_data)
# print(chosen, ' chosen')


def get_name_for_body(chosen):
    name = chosen[-1]
    return name

name = get_name_for_body(chosen)
# print(name)