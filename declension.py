from lxml import html
import requests


def declension_vocative(envoy: str = 'adrian+duda') -> str:
    print(envoy, " env")
    url_api = f'http://nlp.actaforte.pl:8080/Nomina/ImionaNazwiska?ncase=voc&ndata={envoy}'
    change_the_name = requests.get(url_api).text
    parse_xpath = html.fromstring(change_the_name)
    changed_name = parse_xpath.xpath('//html/body/div/form/table/tr/td/table/tr/td')
    for item in changed_name:
        vocative = ' '.join(item.text_content().split()) + " .."
    return vocative
