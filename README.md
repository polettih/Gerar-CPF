# 🧮 Gerador de CPF em Python

Um gerador simples de números de CPF válidos, com base no algoritmo oficial de cálculo dos dígitos verificadores. Ideal para fins de **teste, estudo e automação**.

## 🚀 Funcionalidades

- Gera CPFs válidos com 11 dígitos
- Permite exibir o CPF com ou sem formatação (pontos e traço)
- Código limpo e fácil de entender
- Pode ser usado como função em outros scripts

## 💻 Exemplo de uso

```python
from gerador_cpf import gerar_cpf

print(gerar_cpf(formatado=True))  # Saída: 140.362.187-00
print(gerar_cpf(formatado=False)) # Saída: 14036218700
```

## 📦 Instalação

Nenhuma dependência externa é necessária, basta ter o Python 3 instalado.

1. Clone o repositório ou copie o arquivo `gerador_cpf.py`
2. Execute no terminal ou importe no seu projeto Python

```bash
python gerador_cpf.py
```

## 🛠️ Como funciona

1. Gera 9 números aleatórios
2. Calcula os dois dígitos verificadores com base nos 9 primeiros
3. Retorna o CPF completo (formatado ou não)

## 📁 Estrutura

```bash
gerador-cpf/
├── gerador_cpf.py
├── README.md
```

## ⚠️ Aviso Legal

Este projeto é apenas para **fins educacionais e de teste**. O uso de CPFs gerados para fraudes, golpes ou qualquer atividade ilegal **é crime**.

## ✍️ Autor

Desenvolvido por [Seu Nome Aqui](https://github.com/seu-usuario).  
Contribuições e sugestões são bem-vindas!
