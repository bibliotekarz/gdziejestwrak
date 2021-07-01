import yagmail
from os import getenv
from dotenv import load_dotenv
from bodytitle import random_subject, random_body
from politicians import random_email, parse_json, get_name_for_body

load_dotenv()

receiver = random_email(parse_json())[0]
subject = random_subject()
contents = '' #random_body(get_name_for_body(chosen))
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
print(receiver)
print(subject)
print(contents)



print("---")

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
