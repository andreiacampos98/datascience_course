import pandas as pd
import numpy as np

#Importar os dados do ficheiro df para uma DataFrame chamada df José P.M.
df = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula3/Carros2.csv")


#Linha 2 Explorar conteúdo da tabela e identificar potenciais situações de erro
print("Explorar conteúdo da tabela e identificar potenciais situações de erro\n\n")
print(df.head())
print(df.info())
print("----------------------Principais estatisticas--------------------")
print(df.describe())


#Linha 3 Identificar missing values e converte-los para o formato NaN
print(f"\nNo dataframe df temos {df.isnull().sum().sum()} valores ausentes no total.\n")

print("Numero de missing values por cada coluna: \n")
print(df.isnull().sum())

print("----------Substituir os valores----------")
df.replace('', np.nan, inplace=True)
print(f"\nNo dataframe df temos {df.isnull().sum().sum()} valores ausentes no total.\n")
df.replace('?',np.nan, inplace = True)
print(f"\nNo dataframe df temos {df.isnull().sum().sum()} valores ausentes no total.\n")

#Linha 4 Corrigir tipologia das colunas, caso necessário Andreia
print(df.info())
df['height']=df['height'].astype(float)
df['price']=df['price'].astype(float)
print("Analisar o tipo de variaveis depois de fazer a correção.")
print(df.info())

#Linha 5 Indicar o total de observações com missing values e o número de missing values por variável 

print(f"O numero total de observações com missing values é {df.isnull().any(axis=1).sum()}")
print(f"O número de missing values por variável \n{df.isnull().sum()}")


#Linha 6 No caso da variável price, caso ela tenha missing values, fazer drop
df = df.dropna(subset=['price'])

#Linha 7 Caso existam missing values noutras variáveis quantitativas, substitui-os pela média
df['height'] = df['height'].fillna(df['height'].mean())
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
df['price'] = df['price'].fillna(df['price'].mean())

#Linha 8 Caso existam missing values noutras variáveis qualitativas, substitui-os pela moda
df['fuel-type'] = df['fuel-type'].fillna(df['fuel-type'].mode()[0])
df['num-of-doors'] = df['num-of-doors'].fillna(df['num-of-doors'].mode()[0])

print("----------------------------Verificar se ainda existe missing values--------------------")
print(df.isnull().sum())

#Linha 9 Confirmar que não existem mais valores em falta
m_horsepower=df['horsepower'].mean()
print(m_horsepower)
df['price'] = df['price'].replace(np.nan, m_horsepower)


#Linha 10 Exportar os dados de df num ficheiro csv com o nome Carros3

df.to_csv('3_exploratory_data_analysis/aula3/Carros2_final.csv', index=False)
