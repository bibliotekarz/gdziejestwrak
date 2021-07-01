from declension import declension_vocative
from politicians import get_name_for_body, random_email, parse_json


def test_declension_vocative():
    assert declension_vocative('arek marek') == 'Arku Marku'


def test_parse_json():
    output = parse_json()
    assert len(output) > 200
    assert type(output) == list
    assert len(output[-1]) == 3


def test_random_email():
    meps = [['Wojciech.Kossakowski@sejm.pl', 'Wojciech', 'Wojciech Kossakowski'],
            ['Jerzy.Malecki@sejm.pl', 'Jerzy', 'Jerzy Małecki'], \
            ['Michal.Wypij@sejm.pl', 'Michał', 'Michał Wypij'], ['Jan.Dziedziczak@sejm.pl', 'Jan', 'Jan Dziedziczak'], \
            ['Piotr.Kaleta@sejm.pl', 'Piotr', 'Piotr Kaleta'],
            ['Marlena.Malag@sejm.pl', 'Marlena', 'Marlena Magdalena Maląg'], \
            ['Jan.Mosinski@sejm.pl', 'Jan', 'Jan Mosiński'],
            ['Katarzyna.Sojka@sejm.pl', 'Katarzyna', 'Katarzyna Sójka']]
    output = random_email(meps)
    assert len(output) == 4
    assert type(output) == list


def test_get_name_for_body():
    chosen = ['Witold.Czarnecki@sejm.pl', 'Witold', 'Witold Czarnecki', 'Witoldzie Czarnecki']
    output = get_name_for_body(chosen)
    assert output == 'Witoldzie Czarnecki'
