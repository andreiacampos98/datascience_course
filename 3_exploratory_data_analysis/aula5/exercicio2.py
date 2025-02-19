import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Carros5 = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula5/Carros5.csv")


# linha 1 - Analisar a distribuição da variável price
# através de um boxplot.
# Que conlusões se podem tirar deste gráfico?
Carros5.boxplot(column='price', patch_artist=True)
plt.show()
# 50% dos carros têm um preço entre 7500 (q1) e 16000(q3).
# Temos alguns outliers com um preço acima dos 30k (limite superior),
# ou seja, temos alguns outliers.

# linha 2 - Escolher uma variável que seja adequado ser analisada
# via gráfico de barras e começar por criar uma tabela de frequências.
freq_tab = Carros5['body-style'].value_counts()
print(freq_tab)

# linha 3 - Criar um gráfico de barras e um pie chart com
# base na tabela de frequências criada no passo anterior
freq_tab.plot(kind='bar')
plt.show()

freq_tab.plot.pie()
plt.show()

# linha 4 - Explorar via Scatter Plot a relação entre
# a variável hoursepower e a variávl price.
# Que tipo de relação parece que as variáveis apresentam?
plt.scatter(Carros5['horsepower'], Carros5['price'])
plt.show()
# O gráfico confirma uma correlação linear positiva entre horsepower e price
# (à medida que a potência aumenta, o preço tende a subir).
# Existe uma alta concentração de pontos em valores mais baixos, indicando que
# a maioria dos carros tem potência menor.

# linha 5 - Criar um heatmap para explorar a correlação entre
# todas as variáveis quantitativas.
# Que conclusões podemos retirar desta representação gráfica?
print(Carros5.describe())
correl = Carros5[['wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-size', 'horsepower', 'price']].corr()
sns.heatmap(correl, annot=True, cmap='viridis')
plt.show()
# Variáveis com correlação forte
# Length & Wheel-base → Alta correlação (carros mais longos tendem a ter
# maior distância entre eixos).
# Curb-weight & Length → Carros mais longos geralmente são mais pesados.
# Width & Length → Veículos maiores em comprimento tendem a ser mais largos.
# Price & Engine-size → Motores maiores tendem a aumentar o preço do carro.

# Variável com correlação fraca
# Height (altura) tem pouca relação com outras variáveis, indicando que
# a altura do carro não impacta significativamente peso, potência ou preço.
