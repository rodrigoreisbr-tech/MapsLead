from __future__ import annotations

from pandas import DataFrame

from .logger import setup_logger

logger = setup_logger(__name__)


def salvar_planilha(df: DataFrame, caminho: str) -> None:
    """Salva o DataFrame em uma planilha Excel."""
    try:
        df.to_excel(caminho, sheet_name="Empresas", index=False)
        logger.info("Planilha salva em %s", caminho)
    except Exception as exc:
        logger.error("Erro ao salvar planilha: %s", exc)
        raise

    sem_telefone = df[df["Telefone Encontrado"].isna()]
    if not sem_telefone.empty:
        with open("empresas_sem_telefone.log", "w", encoding="utf-8") as f:
            for nome in sem_telefone["Nome da Empresa"]:
                f.write(f"{nome}\n")
        logger.info("%d empresas sem telefone", len(sem_telefone))
