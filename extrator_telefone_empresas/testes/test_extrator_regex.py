import pytest

from extrator.extrator_regex import extrair_telefone


@pytest.mark.parametrize(
    "texto,esperado",
    [
        ("Ligue para (11) 98765-4321 agora", "(11) 98765-4321"),
        ("Telefone: 11987654321", "11987654321"),
        ("Contato 11 3456-7890 adicional", "11 3456-7890"),
    ],
)
def test_extrair_telefone_valido(texto, esperado):
    assert extrair_telefone(texto) == esperado


def test_extrair_telefone_invalido():
    assert extrair_telefone("Sem número aqui") is None
