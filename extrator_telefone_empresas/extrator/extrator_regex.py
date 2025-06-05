import re
from typing import Optional

TELEFONE_REGEX = re.compile(r"\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}")


def extrair_telefone(texto: str) -> Optional[str]:
    """Extrai o primeiro telefone válido de um texto."""
    if not texto:
        return None
    match = TELEFONE_REGEX.search(texto)
    if match:
        return match.group()
    return None
