from declension import declension_vocative
from politicians import get_name_for_body, random_email


def test_declension_vocative():
    assert declension_vocative('arek marek') == 'Arku Marku'


def test_get_name_for_body():
    chosen = ['Witold.Czarnecki@sejm.pl', 'Witold', 'Witold Czarnecki', 'Witoldzie Czarnecki']
    assert get_name_for_body(chosen) == 'Witoldzie Czarnecki'

def test_random_email():
    meps =[['Wojciech.Kossakowski@sejm.pl', 'Wojciech', 'Wojciech Kossakowski'], ['Jerzy.Malecki@sejm.pl', 'Jerzy', 'Jerzy Małecki'], \
           ['Michal.Wypij@sejm.pl', 'Michał', 'Michał Wypij'], ['Jan.Dziedziczak@sejm.pl', 'Jan', 'Jan Dziedziczak'], \
           ['Piotr.Kaleta@sejm.pl', 'Piotr', 'Piotr Kaleta'], ['Marlena.Malag@sejm.pl', 'Marlena', 'Marlena Magdalena Maląg'], \
           ['Jan.Mosinski@sejm.pl', 'Jan', 'Jan Mosiński'], ['Katarzyna.Sojka@sejm.pl', 'Katarzyna', 'Katarzyna Sójka']]

    assert len(random_email(meps)) == 4
    assert type(random_email(meps)) == list
