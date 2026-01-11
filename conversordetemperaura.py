# Conversor de temperatura 
# Formula C -> F: Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.
# Formula F -> C: C = 5/9 x (F – 32)

print('Bem vindo ao conversor de Fahrenheit e Celsius')

print('Opções: °C -> F, ou F -> °C')
escolha = input('Escolha entre CF ou FC: ').strip().upper()


if escolha == 'CF':
 escolha_celsius = int(input('Quantos graus celsius: '))
 resultado_cf = escolha_celsius  * 1.8 + 32.0
 print(f'Conversão: {resultado_cf:.2f}')

elif escolha == 'FC' or 'fc' or 'Fc':
 escolha_fahrenheit = int(input('Quantos em F: '))
 resultado_fc = (escolha_fahrenheit - 32.0) * 5/9 
 print(f'Conversao: {resultado_fc:.2f}')
 
else:
  print('Invalido')