import pandas as pd

print('\nVisão Geral dos Dados da Planilha')
print(110 * '=')
df_roupas = pd.read_excel('vendas_roupas.xlsx')
print(df_roupas)


print('\nTotal de Peças Vendidas')
print(45 * '=')
print(df_roupas['Unidades Vendidas'].sum())


print('\nMédia dos Preços')
print(45 * '=')
print(df_roupas['Preço por Unidade (R$)'].mean())


print('\nProduto com Maior Faturamento')
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].max())


print('\nProduto com Menor Faturamento')
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].min())


print('\nProdutos com Nivel de Satisfação Baixo')
print(45 * '=')
print(df_roupas[df_roupas['Satisfação'] == 'Baixo'])


print('\nProdutos Acima da Média')
print(110 * '=')
media = df_roupas['Faturamento Total (R$)'].mean()
print(df_roupas[df_roupas['Faturamento Total (R$)'] >= media])