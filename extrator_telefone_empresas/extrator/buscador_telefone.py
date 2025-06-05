from __future__ import annotations

import os
import random
import time
from typing import Optional

import requests
from dotenv import load_dotenv

from .logger import setup_logger
from .extrator_regex import extrair_telefone

logger = setup_logger(__name__)
load_dotenv()

SERPAPI_URL = "https://serpapi.com/search.json"


def buscar_telefone(nome: str, regiao: str) -> Optional[str]:
    """Busca o telefone de uma empresa utilizando a SerpAPI."""
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        logger.warning("SERPAPI_KEY não configurada")
        return None

    query = f"telefone empresa {nome} {regiao}"
    params = {
        "engine": "google",
        "q": query,
        "hl": "pt",
        "gl": "br",
        "api_key": api_key,
    }

    time.sleep(random.uniform(5, 10))
    try:
        resp = requests.get(SERPAPI_URL, params=params, timeout=20)
        resp.raise_for_status()
    except requests.RequestException as exc:
        logger.error("Erro na requisição para SerpAPI: %s", exc)
        return None

    try:
        data = resp.json()
    except ValueError:
        logger.error("Resposta inválida da SerpAPI")
        return None

    # Verifica snippets nos resultados orgânicos
    for result in data.get("organic_results", []):
        snippet = result.get("snippet") or ""
        telefone = extrair_telefone(snippet)
        if telefone:
            logger.info("Telefone encontrado via snippet para %s: %s", nome, telefone)
            return telefone

    # Verifica caixa de respostas
    answer_box = data.get("answer_box") or {}
    if isinstance(answer_box, dict):
        for value in answer_box.values():
            if isinstance(value, str):
                telefone = extrair_telefone(value)
                if telefone:
                    logger.info(
                        "Telefone encontrado via answer_box para %s: %s", nome, telefone
                    )
                    return telefone

    logger.info("Telefone não encontrado para %s", nome)
    return None
