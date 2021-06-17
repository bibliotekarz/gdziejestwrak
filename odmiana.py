from lxml import html
import requests


url_api = 'http://nlp.actaforte.pl:8080/Nomina/ImionaNazwiska?ncase=voc&ndata=adrian+duda'

change_the_name  = requests.get(url_api).text
parse_xpath  = html.fromstring(change_the_name)
changed_name  = parse_xpath.xpath('//html/body/div/form/table/tr/td/table/tr/td')
for item in changed_name:
    roar = ' '.join(item.text_content().split())+" .."
    print(roar)