# Extrator de Telefone de Empresas

Aplicação em Python para ler uma planilha de empresas, buscar automaticamente o número de telefone de cada uma na internet e salvar o resultado em nova planilha.

## Instalação

```bash
pip install -r requirements.txt
```

Configure a chave da SerpAPI em um arquivo `.env`:

```bash
SERPAPI_KEY=xxxxxx
```

## Geração da planilha de exemplo

Este repositório inclui o arquivo `empresas.csv` com dados fictícios para testes. Caso deseje gerar a planilha Excel a partir desse CSV, execute:

```bash
python gerar_planilha_exemplo.py
```

O script criará `empresas.xlsx` que é usada como entrada padrão da aplicação.

## Uso

Depois de gerar a planilha (ou fornecer a sua própria), execute o script principal:

```bash
python main.py
```

Será gerado o arquivo `empresas_com_telefone.xlsx` com a coluna `Telefone Encontrado` preenchida quando possível.

## Testes

```bash
pytest
```

## Exemplo de entrada e saída

- `empresas.csv`: arquivo de exemplo utilizado para gerar a planilha Excel.
- `empresas_com_telefone.xlsx`: planilha gerada após a execução.
