from random import choice
import yagmail
from os import getenv, path
from dotenv import load_dotenv
from datetime import datetime
import requests
from json import load

load_dotenv()

receiver = 'as.po@interia.pl'
subject = 'tytuł1 ąęółńćźżśą'
contents = 'Nie ma Terrego'
url_api = 'http://api.sejm.gov.pl/sejm/term9/MP'
club_name = "PiS"


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


def work_json():
    i = 0
    meps_emails = []
    with open('data.json', 'r', encoding='utf8') as json_file:
        data = load(json_file)
        while i < len(data):
            if data[i]['active'] == True:
                _ = [data[i]['email'], data[i]['firstName'], data[i]['firstLastName']]
                meps_emails.append(_) if data[i]['club'] == club_name else ""

            i += 1
    return meps_emails


def random_email(meps):
    return choice(meps)


print(random_email(work_json()))


def random_subject():
    subject_list = ['Kto odkąd PiS jest u władzy odpowiada za brak działań międzynarodowych aby odzyskać wrak?',
                    'Gdzie jest wrak?',
                    'Czy był zamach na Prezydenta i Rzeczpospolitą?',
                    'Gdzie jest raport Smoleński?',
                    'Czy Jarosław kazał lądować bratu?',
                    'Ile kosztuje Polskę indolencja Antoniego Maciarewicza?'
                    'Czy Jarosława gryzie sumienie za nakazanie bratu lądowania'
                    'Ile czasu potrzeba aby Rząd zadbał o sprawiedliwość #zamachsmoleński?']
    subject = choice(subject_list)
    return subject

# print(random_subject())

# {"active":true,
#  "club":"KO",
#  "discritNum":41,
#  "districtName":"Szczecin",
#  "email":"Artur.Lacki@sejm.pl",
#  "firstLastName":"Artur Łącki",
#  "firstName":"Artur",
#  "id":222,
#  "lastFirstName":"Łącki Artur",
#  "lastName":"Łącki",
#  "secondName":"Jarosław",
#  "voivodeship":"zachodniopomorskie"}