import pandas as pd


def gerar_excel() -> None:
    """Gera empresas.xlsx a partir do arquivo CSV."""
    df = pd.read_csv('empresas.csv')
    df.to_excel('empresas.xlsx', sheet_name='Empresas', index=False)


if __name__ == '__main__':
    gerar_excel()
