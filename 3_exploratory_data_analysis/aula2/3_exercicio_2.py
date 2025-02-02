import os
import pandas as pd
#1
path='/home/acer/Desktop/datascience_course/exploratory_data_analysis/aula2/5_data.csv'
#2
dados = pd.read_csv(path)
#3
print(dados.to_string())
#4
print(type(dados))
#5
print(dados.head(3))
#6
print(dados.tail(4))
#7
print(dados.info())