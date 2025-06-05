from __future__ import annotations

import os
from tqdm import tqdm

from extrator import ler_planilha, buscar_telefone, salvar_planilha, setup_logger

logger = setup_logger("main")


def main() -> None:
    entrada = "empresas.xlsx"
    saida = "empresas_com_telefone.xlsx"

    if not os.path.exists(entrada):
        logger.error("Arquivo %s não encontrado", entrada)
        return

    df = ler_planilha(entrada)

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Buscando telefones"):
        nome = row["Nome da Empresa"]
        regiao = row["Região"]
        telefone = buscar_telefone(nome, regiao)
        if telefone:
            df.at[idx, "Telefone Encontrado"] = telefone

    salvar_planilha(df, saida)


if __name__ == "__main__":
    main()
