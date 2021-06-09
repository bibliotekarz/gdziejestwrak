import yagmail
from os import getenv
from dotenv import load_dotenv

load_dotenv()

receiver = "arek@bibliotekarz.com"
body = "ĄŻŹŚćńŁÓĘ \n Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP(getenv('PYPOCZTA_EMAIL'), getenv('PYPOCZTA_PASS'))
yag.send(
    to=receiver,
    subject="Yagmail tytuł ąęółńćźżśą",
    contents=body
# #    attachments=filename,
)
