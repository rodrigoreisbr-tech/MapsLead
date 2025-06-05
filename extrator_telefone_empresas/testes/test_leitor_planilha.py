import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from extrator.leitor_planilha import ler_planilha


def criar_planilha_temporaria(tmp_path):
    dados = {
        "Nome da Empresa": ["A", "B", "A"],
        "CNPJ": ["1", "2", "1"],
        "Razão Social": ["A SA", "B SA", "A SA"],
        "Região": ["X", "Y", "X"],
    }
    df = pd.DataFrame(dados)
    caminho = tmp_path / "empresas.xlsx"
    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Empresas", index=False)
    return caminho


def test_ler_planilha(tmp_path):
    caminho = criar_planilha_temporaria(tmp_path)
    df = ler_planilha(caminho)

    assert list(df.columns) == [
        "Nome da Empresa",
        "CNPJ",
        "Razão Social",
        "Região",
        "Telefone Encontrado",
    ]
    assert len(df) == 2  # removeu duplicata pelo CNPJ
