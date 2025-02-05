import pandas as pd
import numpy as np

#Importar os dados do ficheiro df para uma DataFrame chamada df José P.M.
df = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula3/df.csv")


#Linha 2 Explorar conteúdo da tabela e identificar potenciais situações de erro Nuno
print(df.head())
print(df.info())
print(df.describe())


#Linha 3 Identificar missing values e converte-los para o formato NaN
print(df.isnull().sum())

print(df.isnull())

print(df.isnull().any().any())
df.replace('', np.nan, inplace=True)
print(df.isnull().sum())

#Linha 4 Corrigir tipologia das colunas, caso necessário Andreia
print(df.info())
df['height']=df['height'].astype(float)
df['price']=df['price'].astype(float)

#Linha 5 Indicar o total de observações com missing values e o número de missing values por variável Susana
print(df.isnull().any(axis=1).sum())
print(df.isnull().sum())


#Linha 6 No caso da variável price, caso ela tenha missing values, fazer drop Tamara
Carros2 = Carros2.dropna(subset=['price'])

#Linha 7 Caso existam missing values noutras variáveis quantitativas, substitui-os pela média José M.

#Linha 8 Caso existam missing values noutras variáveis qualitativas, substitui-os pela moda Stefane
df['fuel-type'] = df['fuel-type'].fillna(df['fuel-type'].mode()[0])
df['aspiration'] = df['aspiration'].fillna(df['aspiration'].mode()[0])
df['body-style'] = df['body-style'].fillna(df['body-style'].mode()[0])
df['drive-wheels'] = df['drive-wheels'].fillna(df['drive-wheels'].mode()[0])
df['engine-location'] = df['engine-location'].fillna(df['engine-location'].mode()[0])

#Linha 9 Confirmar que não existem mais valores em falta José F
m_horsepower=Carros2['horsepower'].mean()
print(m_horsepower)
Carros2['price'].replace(np.nan, m_horsepower, inplace = True)

#Linha 10 Exportar os dados de df num ficheiro csv com o nome Carros3

carros2.to_csv('Carros3.csv', index=False)
