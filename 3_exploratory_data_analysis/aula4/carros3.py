#Linha 1 Importar os dados do ficheiro Carros3 para uma DataFrame chamada Carros3
import pandas as pd
import numpy as np

Carros3 = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula4/carros3.csv")

#Linha 2 Avaliar os principais indicadores das variáveis quantitativas do DataFrame Carros3 
#e verifica se existe um problema de escalas.
print("Avaliar os principais indicadores das variáveis quantitativas do DataFrame Carros3")
print(Carros3.describe())
print("As variáveis height e price têm uma amplitude muito maior do que as outras.")

#Linha 3 Criar uma nova variável length_min_max através da transformação Min-Max aplicada a length.
#Validar se os novos valores da variável são os previstos pela transformação. 
print("---------------------------------------- Min-Max-----------------------------------")
Carros3['length_min_max']=(Carros3['length']-Carros3['length'].min())/(Carros3['length'].max()- Carros3['length'].min())
print(Carros3.describe())

#Linha 4 Criar uma nova variável width_std através da estandardização da variável width.
#Validar se os novos valores da variável são os previstos pela transformação.
print("---------------------------------------- Estandadização-----------------------------------")
Carros3['width_std']=(Carros3['width'] -Carros3['width'].mean())/(Carros3['width'].std())
print(Carros3.describe())

#Linha 5 Criar uma nova variável height_log através de uma transformação Logarítmica aplicada a height.
#Validar se os novos valores da variável são os previstos pela transformação.
print("---------------------------------------- Logaritmica-----------------------------------")
Carros3['height_log']=np.log1p(Carros3['height'])
print(Carros3.describe())

#Linha 6 Criar uma nova variável price_decile através da transformação em decis da variável price.
#Validar se os novos valores da variável são os previstos pela transformação.
print("---------------------------------------- 10 decis-----------------------------------")
Carros3['price_decile']=pd.qcut(Carros3['price'], q=10, labels=False) + 1
print(Carros3.describe())


#Linha 7 Exportar os dados de Carros3 num ficheiro csv com o nome Carros4
Carros3.to_csv('Carros3_final.csv', index=False)