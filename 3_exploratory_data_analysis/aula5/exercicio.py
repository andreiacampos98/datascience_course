import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Carros5 = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula5/Carros5.csv")

# Linha 1 Sobre o Carros5 criar uma nova variável numérica com base na \
# variável num-of-doors

print(Carros5['num-of-doors'].unique())
Carros5['num-of-doors-nb'] = Carros5['num-of-doors'].map({'two': 2, 'four': 4})
print(Carros5)


print(Carros5['body-style'].unique())
Carros5_dummy = pd.get_dummies(Carros5['body-style'], prefix='body-style', drop_first=False)
print(Carros5_dummy)
# adicionar as colunas na tabela inicial
Carros5 = pd.concat([Carros5, pd.get_dummies(Carros5['body-style'], prefix='body-style', drop_first=True)], axis=1)
print(Carros5['body-style'])
print(Carros5)

lista = ['wheel-base', 'length', 'width', 'height']
for i in lista:
    Carros5[i] = (Carros5[i] * 2.54).round(0).astype(int)

print(Carros5[['wheel-base', 'length', 'width', 'height']])


Carros5['price'] = round(Carros5['price'] * 0.96, 2)

print(Carros5.describe())

plt.hist(Carros5['price'], bins=10, edgecolor='black')
plt.show()

Carros5['price_nivel'] = np.where(
    Carros5['price'] < 7470.24, 'baixo',
    np.where(Carros5['price'] <= 24000, 'médio', 'alto')
)

print(Carros5[['price', 'price_nivel']])

# linha 6
Carros5['wheel_base_outliers'] = np.where(
    Carros5['wheel-base'] < 117.03 * 2.54, False, True)

Carros5['horsepower_outliers'] = np.where(
    Carros5['horsepower'] < 215.77 * 2.54, False, True)


print(Carros5[['wheel_base_outliers', 'wheel-base', 'horsepower_outliers', 'horsepower']])