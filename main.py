from random import choice
import yagmail
from os import getenv
from dotenv import load_dotenv
from json import load
from declension import declension_vocative
from politicians import update_data
from bodytitle import random_subject


load_dotenv()

receiver = 'as.po@interia.pl'
subject = 'tytuł1 ąęółńćźżśą'
contents = 'Nie ma Terrego'

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