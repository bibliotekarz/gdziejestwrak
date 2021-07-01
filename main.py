import yagmail
from os import getenv
from dotenv import load_dotenv
from bodytitle import random_subject, random_body
from politicians import is_data_exist, do_you_update_data, parse_json, random_email, get_name_for_body, get_email_adress

load_dotenv()

'''
from declension import declension_vocative
name = declension_vocative()
#TODO = where to embed name ?
'''


def send_mail(receiver: str, subject: str = 'hello', contents: str = '...'):
    yag = yagmail.SMTP(getenv('PYPOCZTA_EMAIL'), getenv('PYPOCZTA_PASS'))
    yag.set_logging(yagmail.logging.DEBUG, 'somelocalfile.log')
    receiver = 'arek@bibliotekarz.com'
    yag.send(
        to=receiver,
        subject=subject,
        contents=contents
    )
    return

is_data_exist()
do_you_update_data()
meps_data = parse_json()
chosen = random_email(meps_data)
name = get_name_for_body(chosen)
receiver = get_email_adress(chosen)
subject = random_subject()
contents = random_body(name)

send_mail(receiver, subject, contents)