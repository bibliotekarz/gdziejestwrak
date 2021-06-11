import yagmail
from os import getenv, path
from dotenv import load_dotenv
from datetime import datetime
import requests


load_dotenv()

receiver = 'as.po@interia.pl'
subject = 'tytuł ąęółńćźżśą'
contents = 'Nie ma Terrego'
url_api = 'http://api.sejm.gov.pl/sejm/term9/MP'


def send_mail(receiver, subject='hello', contents='...'):
    yag = yagmail.SMTP(getenv('PYPOCZTA_EMAIL'), getenv('PYPOCZTA_PASS'))
    yag.set_logging(yagmail.logging.DEBUG, 'somelocalfile.log')
    yag.send(
        to=receiver,
        subject=subject,
        contents=contents
    )
    return


# send_mail(receiver, subject, contents)


def update_data():
    now = datetime.now().weekday()
    current_date = datetime.now().date()
    modyfi_date = datetime.fromtimestamp(path.getmtime('data.json')).date()

    if now == (4 or 0) and current_date - modyfi_date == 0:
        data = requests.get(url_api)
        data.raise_for_status()
        with open("data.json", "w", encoding='utf-8') as f:
            f.write(data.text)
    return


# print(update_data())