import pandas as pd






#Importar os dados do ficheiro Carros2 para uma DataFrame chamada Carros2 José P.M.
df = pd.read_csv(r"C:\Users\Andreia.CAMPOS\OneDrive - CLASQUIN SA\Desktop\datascience/3_exploratory_data_analysis/aula3/Carros2.csv")

#Linha 2 Explorar conteúdo da tabela e identificar potenciais situações de erro Nuno
print(df.head())
print(df.isnull().sum)

#Linha 3 Identificar missing values e converte-los para o formato NaN Carolina M.

#Linha 4 Corrigir tipologia das colunas, caso necessário Andreia

#Linha 5 Indicar o total de observações com missing values e o número de missing values por variável Susana

#Linha 6 No caso da variável price, caso ela tenha missing values, fazer drop Tamara

#Linha 7 Caso existam missing values noutras variáveis quantitativas, substitui-os pela média José M.

#Linha 8 Caso existam missing values noutras variáveis qualitativas, substitui-os pela moda Stefane

#Linha 9 Confirmar que não existem mais valores em falta José F

#Linha 10 Exportar os dados de Carros2 num ficheiro csv com o nome Carros3