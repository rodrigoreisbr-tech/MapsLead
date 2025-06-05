"""Módulo de extração de telefones de empresas."""

from .leitor_planilha import ler_planilha
from .buscador_telefone import buscar_telefone
from .extrator_regex import extrair_telefone
from .gravador_planilha import salvar_planilha
from .logger import setup_logger

__all__ = [
    "ler_planilha",
    "buscar_telefone",
    "extrair_telefone",
    "salvar_planilha",
    "setup_logger",
]
