#pip install openpyxl (instalar essa biblioteca para conseguir ler arquivos em excel)

import pandas as pd

df_eletricos = pd.read_excel('vendas_eletronicos.xlsx')
print(df_eletricos)

#deixa o parêntese vazio para imprimir somente as primeiras linhas
print(df_eletricos.head(10))

print('\nMaior valor do Faturamento')
print(45 * '=')
print(df_eletricos['Faturamento Total (R$)'].max())


print('\nMenor valor do Faturamento')
print(45 * '=')
print(df_eletricos['Faturamento Total (R$)'].min())


print('\nTotal do Faturamento')
print(45 * '=')
print(df_eletricos['Faturamento Total (R$)'].sum())


print('\nTotal de Unidades Vendidas')
print(45 * '=')
print(df_eletricos['Unidades Vendidas'].sum())


print('\nMédia de Preços')
print(45 * '=')
print(df_eletricos['Preço por Unidade (R$)'].mean())


print('\nProdutos acima da média')
print(45 * '=')
media = df_eletricos['Faturamento Total (R$)'].mean()
print(df_eletricos[df_eletricos['Faturamento Total (R$)'] >= media])

