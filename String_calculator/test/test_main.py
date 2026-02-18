import pytest
from src.main import suma_string_numeros


def test_suma_basica():
    assert suma_string_numeros("1,2,3") == 6


def test_numero_uno():
    assert suma_string_numeros("1") == 1


def test_cadena_vacia():
    assert suma_string_numeros("") == 0


def suma_3():
    assert suma_string_numeros("1,2") == 3

def test_suma_saltos_linea():
    assert suma_string_numeros("1\n2\n3") == 6