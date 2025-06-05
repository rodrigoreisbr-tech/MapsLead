from __future__ import annotations

import pandas as pd
from pandas import DataFrame
from .logger import setup_logger

logger = setup_logger(__name__)


COLUNAS_OBRIGATORIAS = [
    "Nome da Empresa",
    "CNPJ",
    "Razão Social",
    "Região",
]


def ler_planilha(caminho: str) -> DataFrame:
    """Lê a planilha e retorna um DataFrame validado."""
    try:
        df = pd.read_excel(caminho, sheet_name="Empresas")
    except Exception as exc:
        logger.error("Erro ao ler planilha: %s", exc)
        raise

    faltantes = [col for col in COLUNAS_OBRIGATORIAS if col not in df.columns]
    if faltantes:
        raise ValueError(f"Colunas obrigatórias ausentes: {faltantes}")

    df = df.drop_duplicates(subset=["CNPJ"]).reset_index(drop=True)
    df["Telefone Encontrado"] = None
    logger.info("Planilha '%s' lida com %d registros", caminho, len(df))
    return df
