from random import choice
import yagmail
from os import getenv
from dotenv import load_dotenv
from json import load
from declension import declension_vocative
from politicians import update_data, get_deputies
from bodytitle import random_subject, random_body

load_dotenv()

receiver = 'as.po@interia.pl'
subject = random_subject()
contents = 'tere'  # random_body(name)
club_name = "PiS"
chosen = []
# TODO: resolve duplicate club_name

'''
from declension import declension_vocative
name = declension_vocative()
#TODO = where to embed name ?
'''


def send_mail(receiver: str, subject: str = 'hello', contents: str = '...'):
    yag = yagmail.SMTP(getenv('PYPOCZTA_EMAIL'), getenv('PYPOCZTA_PASS'))
    yag.set_logging(yagmail.logging.DEBUG, 'somelocalfile.log')
    yag.send(
        to=receiver,
        subject=subject,
        contents=contents
    )
    return


# send_mail(receiver, subject, contents)


def work_json()->list:
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


def random_email(meps:list)->list:
    chosen = choice(meps)
    vocative = declension_vocative(chosen[2])
    chosen.append(vocative)
    return chosen

def get_name_for_body():
    name = random_email(work_json())[-1]
    return name

print(random_body(get_name_for_body()))

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
