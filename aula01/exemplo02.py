import pandas as pd
import os

os.system('cls')

df_planilha_custos = pd.read_csv('planilha_de_custos.csv')
print('\nDados Obtidos')
print(91 * '-')
print(df_planilha_custos.head())

#Criando uma coluna nova
df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] + #PARA ACHAR UMA PORCENTAGEM: valor * porcentagem que eu quero (ex 120 * 6%)
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] / 100) +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
)
print(df_planilha_custos.head())
print()
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head(10))
