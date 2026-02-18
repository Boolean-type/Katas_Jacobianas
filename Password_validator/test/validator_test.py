import pytest
from src.pass_validator import validar_contrasena


def test_contrasena_valida_con_numero_y_longitud():
    assert validar_contrasena("abc12345") is True


def test_contrasena_valida_solo_numeros():
    assert validar_contrasena("12345678") is True


def test_falla_por_longitud():
    with pytest.raises(ValueError) as exc:
        validar_contrasena("abc123")
    assert "demasiado corta" in str(exc.value)


def test_falla_por_falta_de_numero():
    with pytest.raises(ValueError) as exc:
        validar_contrasena("abcdefgh")
    assert "al menos un número" in str(exc.value)


def test_falla_por_ambas_reglas():
    with pytest.raises(ValueError) as exc:
        validar_contrasena("abcdefg")
    error_msg = str(exc.value)
    assert "demasiado corta" in error_msg
    assert "al menos un número" in error_msg


def test_contrasena_vacia():
    with pytest.raises(ValueError) as exc:
        validar_contrasena("")
    error_msg = str(exc.value)
    assert "demasiado corta" in error_msg
    assert "al menos un número" in error_msg


def test_longitud_exacta_8_sin_numero():
    with pytest.raises(ValueError) as exc:
        validar_contrasena("abcdefgH")
    assert "al menos un número" in str(exc.value)
    assert "demasiado corta" not in str(exc.value)