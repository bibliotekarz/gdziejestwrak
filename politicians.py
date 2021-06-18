from datetime import datetime
import requests
from os import path


def update_data():
    url_api = 'http://api.sejm.gov.pl/sejm/term9/MP'
    status = 'database of deputies not downloaded'
    if path.exists('data.json'):
        now = datetime.now().weekday()
        current_date = datetime.now().date()
        modyfi_date = datetime.fromtimestamp(path.getmtime('data.json')).date()

        if now == (4 or 0) and current_date - modyfi_date == 0:
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


print(update_data())
