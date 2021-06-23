from random import choice
import yagmail
from os import getenv
from dotenv import load_dotenv
from json import load
from declension import declension_vocative
from politicians import update_data
from bodytitle import random_subject, random_body


load_dotenv()

receiver = 'as.po@interia.pl'
subject = random_subject()
contents = random_body(name)
club_name = "PiS"
#TODO: resolve duplicate club_name

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


send_mail(receiver, subject, contents)





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

print(update_data(), ' update data')
print(random_email(work_json()))
print(random_body(random_email(work_json())[2]), " tekst którego szukam")

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