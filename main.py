import datetime

import yagmail
from os import getenv, path
from dotenv import load_dotenv
import time
from datetime import datetime, date
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
    now = datetime.utcnow().weekday()
    current_date = datetime.now()
    modyfi_date = datetime.fromtimestamp(path.getmtime('data.json'))
    print("\n\n",type(modyfi_date), modyfi_date, " modyfi_date")
    print(type(current_date), current_date, " current_date")
    return current_date - modyfi_date
    # if now == 3 or 6:
    #     data = requests.get(url_api)
    #     data.raise_for_status()
    #     with open("data.json", "w", encoding='utf-8') as f:
    #         f.write(data.text)
    # return


print(update_data())
#
# print(time.ctime(path.getctime('data.json')), ' ctime')
# print(time.ctime(path.getatime('data.json')), ' atime')
# print(time.ctime(path.getmtime('data.json')), ' mtime')