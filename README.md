# Exercício: Tratamento de Exceções na Prática

## Descrição
Aplicação GUI simples em Python que realiza a divisão de dois números com tratamento de exceções. Mostra mensagens de erro para entradas inválidas e para divisão por zero, e apresenta o resultado em uma caixa de diálogo.

## Pré-requisitos
- Python 3.8+ (Windows)
- `tkinter` (normalmente incluído na instalação do Python)

## Como executar
1. Abra o Prompt de Comando (cmd) no Windows.
2. Navegue até a pasta do projeto (onde estão `tratamento_execoes.py` e `README.md`).
3. Execute:

```bat
python tratamento_execoes.py
```

## Uso
- Insira o dividendo em `Dividendo:`.
- Insira o divisor em `Divisor:`.
- Clique em `Dividir`.
- Será exibida uma caixa de diálogo com o resultado ou com uma mensagem de erro:
  - `Por favor, insira números válidos.` para entradas não numéricas.
  - `Divisão por zero não é permitida.` para divisor igual a zero.

## Estrutura do projeto
- `tratamento_execoes.py` - código da aplicação GUI e lógica de tratamento de exceções.
- `README.md` - este arquivo.

## Tratamento de exceções (resumo)
O código captura:
- `ValueError` - quando as entradas não podem ser convertidas para `float`.
- `ZeroDivisionError` - quando o divisor é zero.
Em ambos os casos, são exibidas mensagens claras ao usuário usando `messagebox`.

## Autor
Aluno: Bruno Moura (exercício de Análise e Desenvolvimento de Sistemas)

