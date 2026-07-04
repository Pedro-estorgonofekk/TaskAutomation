# Aulas de Automação de Tarefas Repetitivas

## Aula 1:
- Aula sobre `inputs` 
    - Inputs `string` 
    - Inputs `integer`
    - Inputs `float`  

## Aula 2:
- Aula sobre condições
    - Condicional `if`
    - Condicional `else`
    - Condicional `match case`

## Aula 3:
- Aula sobre laços de repetição
    - Laço `for`
    - Quebras `break`
    - Continuações `continue`

- Aula sobre listas e dicionarios

## Aula 4:
- Aula sobre laços `while`, `try`, `except`

## Aula 5:
- Aula sobre funções
    - Sintaxe `def`
    - Importação `import`

- Aula com `pyautogui`

## Aula 6:
- Automações com `pyautogui`
    - Escreve 67 na calculadora do windows (Precisa estar aberta e na local especifico)

- Aula com `locateOnScreen`
    - Escreve 67 na calculadora do windows (Precisa estar aberta)
    - Tratamento de cor com `grayscale`, erro relacionado à efeito de preto e branco

## Aula 7:
- Aula com `import` e `pyautogui`, implementando ambas as features em uma aplicação única

## Aula 8:
- Aula sobre `pandas`
    - Abrir planilhas com `read_excel()`
    - Tamanho com `len`

- Correção da prova de `pyautogui`

## Aula 9:
- Aula sobre edição de planilhas localizando linha especifica com `loc`

## Aula 10:
- Aula sobre:
    - `drop` para remover uma linha
    - `groupby` para agrupar com um critério específico
        - `mean` critério da média
        - `sum` critério de soma
        - `median` critério de mediana
        - `min` critério do menor valor
        - `max` critério do maior valor
    - `sort_values` para ordenar valores
    - `merge` para juntar `dataframes` com um parâmetro da própria tabela
    - `to_excel` para exportar o `dataframe` para um arquivo de planilhas

## Aula 11:
- Aula com filtragem de dados

## Aula 12
- Aula com ambas as bibliotecas trabalhando em conjunto numa única aplicação

---
<br>

# Trabalho:

## Gerador de cartaz de procurado
O programa deve ler uma planilha, gerar imagem dos cartazes de procurado e cadastrar os valores em um formulario da policia 

---
<br>

## Bibliotecas:
- Ativar o ambiente virtual(opcional), e instalar dependencias:
    - `pip install -r requirements.txt`
- Ambiente virtual:

```bash
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  python -m venv .venv
  .venv\Scripts\Activate.ps1
```
- `pyautogui`
- `opencv`
- `pandas`