import requests
from unittest.mock import patch

from extrator.buscador_telefone import buscar_telefone


def test_buscar_telefone_sem_chave(monkeypatch):
    monkeypatch.delenv("SERPAPI_KEY", raising=False)
    # evita sleep desnecessario
    with patch("extrator.buscador_telefone.time.sleep"):
        resultado = buscar_telefone("Empresa X", "Sul")
    assert resultado is None


def test_buscar_telefone_erro_requisicao(monkeypatch):
    monkeypatch.setenv("SERPAPI_KEY", "dummy")
    with patch("extrator.buscador_telefone.requests.get") as mock_get, \
         patch("extrator.buscador_telefone.time.sleep"):
        mock_get.side_effect = requests.RequestException()
        resultado = buscar_telefone("Empresa Y", "Norte")
    assert resultado is None
