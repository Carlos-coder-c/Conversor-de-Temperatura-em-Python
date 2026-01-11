# 🌡️ Conversor de Temperatura (CLI)

Conversor de temperatura em linha de comando entre **Celsius** e **Fahrenheit**, feito em Python.

O programa permite ao usuário escolher o sentido da conversão:

- `CF` → Celsius → Fahrenheit  
- `FC` → Fahrenheit → Celsius  

As entradas são normalizadas para evitar erros comuns (espaços, maiúsculas/minúsculas) e os cálculos utilizam valores reais.

## 📐 Fórmulas

- Celsius → Fahrenheit  
  `F = C * 1.8 + 32`

- Fahrenheit → Celsius  
  `C = (F - 32) * 5 / 9`

## ▶️ Execução

```bash
python main.py

Exemplo no terminal (após os  dados respondidos)
Bem vindo ao conversor de Fahrenheit e Celsius
Opções: °C -> F (CF) ou F -> °C (FC)
Escolha entre CF ou FC: Fc
Quantos graus Fahrenheit: 32
Conversão: 0.00 °C
