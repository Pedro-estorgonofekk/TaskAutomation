# Gerador de Cartazes de Procurado

Projeto desenvolvido em Python utilizando **Pandas**, **Pillow** e **PyAutoGUI** para gerar cartazes de "Procurado" a partir de uma planilha do Excel e automatizar o envio para o Google Docs.

## Requisitos

- Python 3.10 ou superior
- Google Chrome (ou outro navegador suportado)
- Resolução da tela utilizada durante o desenvolvimento
- Conexão com a internet

## Instalação

Clone o repositório ou extraia o projeto.

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Estrutura do projeto

```
Trabalho/
│
├── assets/
│   ├── font/
│   ├── pag/
│   └── pill/
│
├── funcs/
│   └── funcoes.py
│
├── procurados.xlsx
├── main.py
├── requirements.txt
└── README.md
```

## Como executar

Execute o arquivo principal:

```bash
python main.py
```

ou

```bash
py main.py
```

## Funcionamento

1. O programa solicita o navegador que será utilizado.
2. Os dados são lidos da planilha `procurados.xlsx`.
3. Um cartaz é gerado para cada registro da planilha.
4. O PyAutoGUI automatiza o navegador para inserir o cartaz no Google Docs.
5. O documento é exportado em PDF.

## Observações

- Não dê zoom do navegador durante a execução, ou, utilizar o computador.
- As imagens presentes em `assets/pag` são utilizadas pelo PyAutoGUI para localizar os elementos da interface, não removê-las.

## Tecnologias utilizadas

- Python
- Pandas
- Pillow
- PyAutoGUI

## Uso de Inteligência Artificial

Durante o desenvolvimento do projeto foi utilizada a ferramenta ChatGPT como apoio técnico e para esclarecimento de dúvidas.

### Como a IA foi utilizada

A IA foi utilizada para:

- Sugerir o tema do projeto, optando pela criação de um gerador de cartazes de "Procurado";
- Explicar o funcionamento de bibliotecas utilizadas no projeto, como Pandas, Pillow e PyAutoGUI;
- Auxiliar na resolução de erros encontrados durante o desenvolvimento;
- Sugerir melhorias na organização do código e na reutilização de funções;
- Esclarecer dúvidas sobre manipulação de imagens, posicionamento de texto e automação de interfaces gráficas.

### Como a IA ajudou

A ferramenta foi utilizada como suporte ao desenvolvimento, auxiliando na compreensão de conceitos e na identificação de soluções para problemas encontrados durante a implementação. As sugestões recebidas serviram como base para o desenvolvimento, sendo adaptadas conforme as necessidades do projeto.

### O que foi gerado pela IA

- Sugestões para a ideia do projeto;
- Exemplos de código para geração de imagens utilizando Pillow;
- Sugestões para automação com PyAutoGUI;
- Explicações sobre correção de erros e melhorias no código;
- Orientações para estruturação da documentação do projeto.

### O que foi desenvolvido pelos alunos

- Implementação do código final;
- Organização da estrutura do projeto;
- Criação e edição do modelo do cartaz;
- Captura das imagens utilizadas pelo PyAutoGUI;
- Integração entre a planilha, a geração dos cartazes e a automação;
- Testes, ajustes e validação do funcionamento da aplicação.