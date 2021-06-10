import yagmail
from os import getenv
from dotenv import load_dotenv

load_dotenv()

receiver = 'as.po@interia.pl'
subject = "tytuł ąęółńćźżśą"
contents = "Nie ma Terrego"


def send_mail(receiver, subject='hello', contents='...'):
    yag = yagmail.SMTP(getenv('PYPOCZTA_EMAIL'), getenv('PYPOCZTA_PASS'))
    yag.set_logging(yagmail.logging.DEBUG, 'somelocalfile.log')
    yag.send(
        to=receiver,
        subject=subject,
        contents=contents
    )
    return


send_mail(receiver, subject, contents)
