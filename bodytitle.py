from random import choice


def random_subject():
    email_title = ['Kto odkąd PiS jest u władzy odpowiada za brak działań międzynarodowych aby odzyskać wrak?',
                   'Gdzie jest wrak?',
                   'Czy był zamach na Prezydenta i Rzeczpospolitą?',
                   'Gdzie jest raport Smoleński?',
                   'Czy Jarosław kazał lądować bratu?',
                   'Ile kosztuje Polskę indolencja Antoniego Maciarewicza?'
                   'Czy Jarosława gryzie sumienie za nakazanie bratu lądowania'
                   'Ile jeszcze czasu potrzeba aby Rząd zadbał o sprawiedliwość #zamachsmoleński?']
    subject = choice(email_title)
    return subject


print(random_subject())
