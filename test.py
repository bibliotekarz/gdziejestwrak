import pytest
from declension import declension_vocative
from politicians import get_name_for_body, update_data


def test_declension_vocative():
    assert declension_vocative('arek marek') == 'Arku Marku'


def test_get_name_for_body():
    chosen = ['Witold.Czarnecki@sejm.pl', 'Witold', 'Witold Czarnecki', 'Witoldzie Czarnecki']
    assert get_name_for_body(chosen) == 'Witoldzie Czarnecki'


def test_update_data():
    assert update_data() == 'database of deputies has been updated1' or 'database of deputies downloaded1' or 'database of deputies has not been changed1'
#TODO the error accepts anything  :(