from random import choice


def random_subject():
    email_title = ['Kto odkąd PiS jest u władzy odpowiada za brak działań międzynarodowych aby odzyskać wrak',
                   'Gdzie jest wrak?',
                   'Czy był zamach na Prezydenta i Rzeczpospolitą?',
                   'Gdzie jest raport Smoleński?',
                   'Czy Jarosław kazał lądować bratu?',
                   'Ile kosztuje Polskę indolencja Antoniego Maciarewicza?',
                   'Czy Jarosława gryzie sumienie za nakazanie bratu lądowania',
                   'Ile jeszcze czasu potrzeba aby Rząd zadbał o sprawiedliwość #zamachsmoleński?']
    subject = choice(email_title)
    return subject


def random_body(name: str = "adrian duda") -> str:
    email_photo = [['https://pl.wikipedia.org/wiki/Katastrofa_polskiego_Tu-154_w_Smole%C5%84sku#/media/Plik:Katastrofa_w_Smole%C5%84sku.jpg',
                       'szczątki tupolewa'],
                   ['https://pl.wikipedia.org/wiki/Katastrofa_polskiego_Tu-154_w_Smole%C5%84sku#/media/Plik:Tu-154-crash-in-smolensk-20100410-01.jpg',
                       'szczątki tupolewa'],
                   ['https://pl.wikipedia.org/wiki/Katastrofa_polskiego_Tu-154_w_Smole%C5%84sku#/media/Plik:Tragedia_w_Smolensku_3.jpg',
                       'szczątki tupolewa']]
    #TODO: check the method of attaching photos to the email

    citations = [
        'Jarosław Kaczyński obiecywał, że sprowadzi wrak do Polski i Kaczyński słowa nie dotrzymał. Państwo PiS okazuje się być bardzo słabe i bezwolne.',
        'Antoni Maciarewicz jest blokowany z publikacją raportu o prawdziwych wydarzeniach jakie miały miejsce 11 lat temu.',
        'Apelacje Premiera sprzed 2 lat nic nie dały i nadal nie możemy godnie rozliczyć tego zamachu na nasz kraj.',
        'Noty dyplomatyczne nic nie dają, a żadne pisma żeby nasi sojusznicy pomogli odzyskać wrak nie zostały wysłane.',
        'Czy pamietasz że wrak polskiego Tu-154M rozbitego pod Smoleńskiem nadal jest przetrzymywany przez ruskich?',
        'Kiedy Polska doprowadzi do zakończenia „smoleńskiego teatru Putina”']

    drawn = choice(email_photo)
    link_photo, link_alt = drawn
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[-1]

    body = f'<h1>Dzień dobry</h1>\n\n<p><b>Nadszedł czas aby podjąć bardziej zdecydowane działania. <h2>{first_name} {last_name}</h2>' \
            f' wyciągnij rękę po to co nasze, bez oglądania się na Unię Europejską czy NATO</b></p>\n\n' \
            f'<p>{choice(citations)}</p>\n\n<p>Mimo szumnych wyborczych obietnic od 11 lat Polki i Polacy nie odzyskali tego symbolu narodowej '\
            f'tragedii wyrażonej śmiercią Prezydentów.</p>\n\n' \
            f'<img src="{link_photo}" alt="{link_alt}"> \n\n<p>{first_name} weź się do roboty i napraw to.</p>'

    return body
