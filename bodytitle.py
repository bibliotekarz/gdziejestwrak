from random import choice
from declension import declension_vocative

def random_subject():
    email_title = ['Kto odkąd PiS jest u władzy odpowiada za brak działań międzynarodowych aby odzyskać wrak?',
                   'Gdzie jest wrak?',
                   'Czy był zamach na Prezydenta i Rzeczpospolitą?',
                   'Gdzie jest raport Smoleński?',
                   'Czy Jarosław kazał lądować bratu?',
                   'Ile kosztuje Polskę indolencja Antoniego Maciarewicza?',
                   'Czy Jarosława gryzie sumienie za nakazanie bratu lądowania',
                   'Ile jeszcze czasu potrzeba aby Rząd zadbał o sprawiedliwość #zamachsmoleński?']
    subject = choice(email_title)
    return subject


print(random_subject())

def random_body(name:str ="adrian duda")->str:
    email_body = [['http:\\wrak.jpg','szczątki tupolewa'],
    ['http:\\wrak2.jpg','szczątki tupolewa2'],
    ['http:\\wrak1.jpg','szczątki tupolewa1']]

    drawn = choice(email_body)
    link_photo, link_alt = drawn
    name = declension_vocative()
    body = f'<h1>{name} dzień dobry</h1> \n\n<p>Czy wiesz że noty dyplomatyczne nic nie dają a wrak polskiego Tu-154M rozbitego pod Smoleńskiem nadal jest przetrzymywany przez ruskich?\nApelacje Premira sprzed 2 lat nic nie dały i nadal nie możemy godnie rozliczyć tego zamachu.'\
           f' Antoni Maciarewicz jest blokowany z publikacją raportu o prawdziwych wydarzeniach jakie miały miejsce 11 lat temu.</p>\n\n <p>Od 11 lat Polki i Polacy nie odzyskali tego symbolu narodowej tragedii wyrażonej śmiercią Prezydentów. '\
           f'Nadszedł czas aby podjąć bardziej zdecydowane działania i wycignąć rękę po to co nasze bez oglądania się na Unię Europejską</p>\n\n<img="{link_photo}" alt="{link_alt}">'
    return body

