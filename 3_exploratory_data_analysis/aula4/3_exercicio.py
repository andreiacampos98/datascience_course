#Linha 1 Importar os dados do ficheiro Carros4 para uma DataFrame chamada Carros4 e apagar colunas criadas via transformações das variáveis originais

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Carros4  =  pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/3_exploratory_data_analysis/aula4/1_carros4.csv")

Carros4.drop(columns = 'length_min_max', inplace = True)
Carros4.drop(columns = 'width_std', inplace = True)
Carros4.drop(columns = 'height_log', inplace = True)
Carros4.drop(columns = 'price_decile', inplace = True)

#Linha 2 Analisar as variáveis quantitativas e calcula o número de outliers, segundo o IQR, que cada uma tem. 
print(Carros4.describe())

outliers_info_iqr = []

print("-------Wheel Base-------------")
q1_wheel_base = Carros4['wheel-base'].quantile(0.25)
q3_wheel_base = Carros4['wheel-base'].quantile(0.75)
iqr = q3_wheel_base-q1_wheel_base
limit_inf_wheel_base = q1_wheel_base-1.5*iqr
limit_sup_wheel_base = q3_wheel_base+1.5*iqr
print(f"Numero de  Outliers acima da wheel-base {Carros4['wheel-base'][Carros4['wheel-base'] > limit_sup_wheel_base].count()}")
print(f"Numero de  Outliers abaixo da wheel-base {Carros4['wheel-base'][Carros4['wheel-base'] < limit_inf_wheel_base].count()}")
outliers_info_iqr.append(['wheel-base', Carros4['wheel-base'][Carros4['wheel-base'] > limit_sup_wheel_base].count() + Carros4['wheel-base'][Carros4['wheel-base'] < limit_inf_wheel_base].count()])

print("-------Length-------------")
q1_length = Carros4['length'].quantile(0.25)
q3_length = Carros4['length'].quantile(0.75)
iqr = q3_length-q1_length
limit_inf_length = q1_length-1.5*iqr
limit_sup_length = q3_length+1.5*iqr
print(f"Numero de  Outliers acima da length {Carros4['length'][Carros4['length'] > limit_sup_length].count()}")
print(f"Numero de  Outliers abaixo da length {Carros4['length'][Carros4['length'] < limit_inf_length].count()}")
outliers_info_iqr.append(['length', Carros4['length'][Carros4['length'] > limit_sup_length].count() + Carros4['length'][Carros4['length'] < limit_inf_length].count()])


print("-------width-------------")
q1_width = Carros4['width'].quantile(0.25)
q3_width = Carros4['width'].quantile(0.75)
iqr = q3_width-q1_width
limit_inf_width = q1_width-1.5*iqr
limit_sup_width = q3_width+1.5*iqr
print(f"Numero de  Outliers acima da width {Carros4['width'][Carros4['width'] > limit_sup_width].count()}")
print(f"Numero de  Outliers abaixo da width {Carros4['width'][Carros4['width'] < limit_inf_width].count()}")
outliers_info_iqr.append(['width', Carros4['width'][Carros4['width'] > limit_sup_width].count() + Carros4['width'][Carros4['width'] < limit_inf_width].count()])


print("-------height-------------")
q1_height = Carros4['height'].quantile(0.25)
q3_height = Carros4['height'].quantile(0.75)
iqr = q3_height-q1_height
limit_inf_heigh = q1_height-1.5*iqr
limit_sup_heigh = q3_height+1.5*iqr
print(f"Numero de  Outliers acima da height {Carros4['height'][Carros4['height'] > limit_sup_heigh].count()}")
print(f"Numero de  Outliers abaixo da height {Carros4['height'][Carros4['height'] < limit_inf_heigh].count()}")
outliers_info_iqr.append(['height', Carros4['height'][Carros4['height'] > limit_sup_heigh].count() + Carros4['height'][Carros4['height'] < limit_inf_heigh].count()])


print("-------curb-weight-------------")
q1_curb_weight = Carros4['curb-weight'].quantile(0.25)
q3_curb_weight = Carros4['curb-weight'].quantile(0.75)
iqr = q3_curb_weight-q1_curb_weight
limit_inf_curb_weight = q1_curb_weight-1.5*iqr
limit_sup_curb_weight = q3_curb_weight+1.5*iqr
print(f"Numero de  Outliers acima da curb-weight {Carros4['curb-weight'][Carros4['curb-weight'] > limit_sup_curb_weight].count()}")
print(f"Numero de  Outliers abaixo da curb-weight {Carros4['curb-weight'][Carros4['curb-weight'] < limit_inf_curb_weight].count()}")
outliers_info_iqr.append(['curb-weight', Carros4['curb-weight'][Carros4['curb-weight'] > limit_sup_curb_weight].count() + Carros4['curb-weight'][Carros4['curb-weight'] < limit_inf_curb_weight].count()])


print("-------engine-size-------------")
q1_engine_size = Carros4['engine-size'].quantile(0.25)
q3_engine_size = Carros4['engine-size'].quantile(0.75)
iqr = q3_engine_size-q1_engine_size
limit_inf_engine_size = q1_engine_size-1.5*iqr
limit_sup_engine_size = q3_engine_size+1.5*iqr
print(f"Numero de  Outliers acima da engine-size {Carros4['engine-size'][Carros4['engine-size'] > limit_sup_engine_size].count()}")
print(f"Numero de  Outliers abaixo da engine-size {Carros4['engine-size'][Carros4['engine-size'] < limit_inf_engine_size].count()}")
outliers_info_iqr.append(['engine-size', Carros4['engine-size'][Carros4['engine-size'] > limit_sup_engine_size].count() + Carros4['engine-size'][Carros4['engine-size'] < limit_inf_engine_size].count()])


print("-------horsepower-------------")
q1_horsepower = Carros4['horsepower'].quantile(0.25)
q3_horsepower = Carros4['horsepower'].quantile(0.75)
iqr = q3_horsepower-q1_horsepower
limit_inf_horsepower = q1_horsepower-1.5*iqr
limit_sup_horsepower = q3_horsepower+1.5*iqr
print(f"Numero de  Outliers acima da horsepower {Carros4['horsepower'][Carros4['horsepower'] > limit_sup_horsepower].count()}")
print(f"Numero de  Outliers abaixo da horsepower {Carros4['horsepower'][Carros4['horsepower'] < limit_inf_horsepower].count()}")
outliers_info_iqr.append(['horsepower', Carros4['horsepower'][Carros4['horsepower'] > limit_sup_horsepower].count() + Carros4['horsepower'][Carros4['horsepower'] < limit_inf_horsepower].count()])


print("-------price-------------")
q1_price = Carros4['price'].quantile(0.25)
q3_price = Carros4['price'].quantile(0.75)
iqr = q3_price-q1_price
limit_inf_price = q1_price-1.5*iqr
limit_sup_price = q3_price+1.5*iqr
print(f"Numero de  Outliers acima da price {Carros4['price'][Carros4['price'] > limit_sup_price].count()}")
print(f"Numero de  Outliers abaixo da price {Carros4['price'][Carros4['price'] < limit_inf_price].count()}")
outliers_info_iqr.append(['price', Carros4['price'][Carros4['price'] > limit_sup_price].count() + Carros4['price'][Carros4['price'] < limit_inf_price].count()])


df_outliers = pd.DataFrame(outliers_info_iqr, columns = ['Variável', 'Quantidade'])
print("\n\n-------------------Numero de outliers segundo o metodo IQR------------------------------\n")
print(df_outliers.sort_values(by='Quantidade'))

#Linha 3 Considerar a variável quantitativa com menor número de outliers segundo os cálculos
#do passo anterior e eliminar os registos classificados como outliers.
Carros4['length'] = Carros4['length'].clip(lower=limit_inf_length, upper=limit_sup_length)


#Linha 4 Verificar que já não existem outliers, segundo o IQR, na variável em questão.
print("\n\n-------Length-------------")
print("Confirmação: Número de outliers na variável length após eliminar os mesmos")
q1_length = Carros4['length'].quantile(0.25)
q3_length = Carros4['length'].quantile(0.75)
iqr = q3_length-q1_length
limit_inf_length = q1_length-1.5*iqr
limit_sup_length = q3_length+1.5*iqr
print(f"Numero de  Outliers acima do length {Carros4['length'][Carros4['length'] > limit_sup_length].count()}")
print(f"Numero de  Outliers abaixo do length {Carros4['length'][Carros4['length'] < limit_inf_length].count()}")

# Linha 5 Analisar novamente as variáveis quantitativas e, calcular o número de outliers, 
#agora segundo o método de Estandardização, que cada uma tem.
outliers_info_est = []
print("\n\n-------Wheel Base-------------")
std_wheel_base = Carros4['wheel-base'].std()
mean_wheel_base = Carros4['wheel-base'].mean()
limit_inf_wheel_base = mean_wheel_base-3*std_wheel_base
limit_sup_wheel_base = mean_wheel_base+3*std_wheel_base
print(f"Numero de  Outliers acima da wheel-base {Carros4['wheel-base'][Carros4['wheel-base'] > limit_sup_wheel_base].count()}")
print(f"Numero de  Outliers abaixo da wheel-base {Carros4['wheel-base'][Carros4['wheel-base'] < limit_inf_wheel_base].count()}")
outliers_info_est.append(['wheel-base', Carros4['wheel-base'][Carros4['wheel-base'] > limit_sup_wheel_base].count() + Carros4['wheel-base'][Carros4['wheel-base'] < limit_inf_wheel_base].count()])


print("-------Length-------------")
std_length = Carros4['length'].std()
mean_length = Carros4['length'].mean()
limit_inf_length = mean_length-3*std_length
limit_sup_length = mean_length+3*std_length
print(f"Numero de  Outliers acima da length {Carros4['length'][Carros4['length'] > limit_sup_length].count()}")
print(f"Numero de  Outliers abaixo da length {Carros4['length'][Carros4['length'] < limit_inf_length].count()}")
outliers_info_est.append(['length', Carros4['length'][Carros4['length'] > limit_sup_length].count() + Carros4['length'][Carros4['length'] < limit_inf_length].count()])



print("-------width-------------")
std_width = Carros4['width'].std()
mean_width = Carros4['width'].mean()
limit_inf_width = mean_width-3*std_width
limit_sup_width = mean_width+3*std_width
print(f"Numero de  Outliers acima da width {Carros4['width'][Carros4['width'] > limit_sup_width].count()}")
print(f"Numero de  Outliers abaixo da width {Carros4['width'][Carros4['width'] < limit_inf_width].count()}")
outliers_info_est.append(['width', Carros4['width'][Carros4['width'] > limit_sup_width].count() + Carros4['width'][Carros4['width'] < limit_inf_width].count()])


print("-------height-------------")
std_height = Carros4['height'].std()
mean_height = Carros4['height'].mean()
limit_inf_height = mean_height-3*std_height
limit_sup_height = mean_height+3*std_height
print(f"Numero de  Outliers acima da height {Carros4['height'][Carros4['height'] > limit_sup_height].count()}")
print(f"Numero de  Outliers abaixo da height {Carros4['height'][Carros4['height'] < limit_inf_height].count()}")
outliers_info_est.append(['height', Carros4['height'][Carros4['height'] > limit_sup_height].count() + Carros4['height'][Carros4['height'] < limit_inf_height].count()])


print("-------curb-weight-------------")
std_curb_weight = Carros4['curb-weight'].std()
mean_curb_weight = Carros4['curb-weight'].mean()
limit_inf_curb_weight = mean_curb_weight-3*std_curb_weight
limit_sup_curb_weight = mean_curb_weight+3*std_curb_weight
print(f"Numero de  Outliers acima da curb-weight {Carros4['curb-weight'][Carros4['curb-weight'] > limit_sup_curb_weight].count()}")
print(f"Numero de  Outliers abaixo da curb-weight {Carros4['curb-weight'][Carros4['curb-weight'] < limit_inf_curb_weight].count()}")
outliers_info_est.append(['curb-weight', Carros4['curb-weight'][Carros4['curb-weight'] > limit_sup_curb_weight].count() + Carros4['curb-weight'][Carros4['curb-weight'] < limit_inf_curb_weight].count()])


print("-------engine-size-------------")
std_engine_size = Carros4['engine-size'].std()
mean_engine_size = Carros4['engine-size'].mean()
limit_inf_engine_size = mean_engine_size-3*std_engine_size
limit_sup_engine_size = mean_engine_size+3*std_engine_size
print(f"Numero de  Outliers acima da engine-size {Carros4['engine-size'][Carros4['engine-size'] > limit_sup_engine_size].count()}")
print(f"Numero de  Outliers abaixo da engine-size {Carros4['engine-size'][Carros4['engine-size'] < limit_inf_engine_size].count()}")
outliers_info_est.append(['engine-size', Carros4['engine-size'][Carros4['engine-size'] > limit_sup_engine_size].count() + Carros4['engine-size'][Carros4['engine-size'] < limit_inf_engine_size].count()])


print("-------horsepower-------------")
std_horsepower = Carros4['horsepower'].std()
mean_horsepower = Carros4['horsepower'].mean()
limit_inf_horsepower = mean_horsepower-3*std_horsepower
limit_sup_horsepower = mean_horsepower+3*std_horsepower
print(f"Numero de  Outliers acima da horsepower {Carros4['horsepower'][Carros4['horsepower'] > limit_sup_horsepower].count()}")
print(f"Numero de  Outliers abaixo da horsepower {Carros4['horsepower'][Carros4['horsepower'] < limit_inf_horsepower].count()}")
outliers_info_est.append(['horsepower', Carros4['horsepower'][Carros4['horsepower'] > limit_sup_horsepower].count() + Carros4['horsepower'][Carros4['horsepower'] < limit_inf_horsepower].count()])


print("-------price-------------")
std_price = Carros4['price'].std()
mean_price = Carros4['price'].mean()
limit_inf_price = mean_price-3*std_price
limit_sup_price = mean_price+3*std_price
print(f"Numero de  Outliers acima da price {Carros4['price'][Carros4['price'] > limit_sup_price].count()}")
print(f"Numero de  Outliers abaixo da price {Carros4['price'][Carros4['price'] < limit_inf_price].count()}")
outliers_info_est.append(['price', Carros4['price'][Carros4['price'] > limit_sup_price].count() + Carros4['price'][Carros4['price'] < limit_inf_price].count()])

df_outliers_est = pd.DataFrame(outliers_info_est, columns = ['Variável', 'Quantidade'])
print("\n\n-----------------Numero de outliers segundo o metodo de estandardização---------------------------\n")
print(df_outliers_est.sort_values(by = 'Quantidade'))

# Linha 6 Considerar as duas variáveis quantitativas com menor número de outliers segundo 
# os cálculos do passo anterior, e criar uma nova variável com base nessas, como o    
# sufixo “_lim”, onde se restringe os seus valores com base nos limites inferior e superior 
# calculados no método de Estandardização.
Carros4['wheel-base_lim'] = Carros4['wheel-base'].clip(lower = limit_inf_wheel_base, upper = limit_sup_wheel_base)
Carros4['horsepower_lim'] = Carros4['horsepower'].clip(lower = limit_inf_horsepower, upper = limit_sup_horsepower)


#Linha 7 Validar em que observações as variáveis originais e as “_lim” tomam valores diferentes
print("-----------------------Wheel Base----------------------------")
print(Carros4[Carros4['wheel-base'] != Carros4['wheel-base_lim']])
print("-----------------------Horsepower----------------------------")
print(Carros4[Carros4['horsepower_lim'] != Carros4['horsepower']])

#Linha 8 Considerando as variáveis do passo anterior, original e a limitada, comparar os seus 
# histogramas.

print("-----------------------Wheel Base----------------------------")
# Plot histogram for 'wheel-base_lim'
plt.figure()
counts, bin_edges, _ = plt.hist(Carros4['wheel-base_lim'], bins=10, edgecolor='black')

for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha='center', va='bottom', fontsize=10, color='black')
plt.title('Histogram of Wheel-Base_lim')
plt.xticks(bin_edges, rotation=45)
plt.xlabel('Wheel Base Lim')
plt.ylabel('Frequency')
plt.show()

# Plot histogram for 'wheel-base'
plt.figure()
counts, bin_edges, _  =  plt.hist(Carros4['wheel-base'], bins = 10, edgecolor = 'black')
for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha = 'center', va = 'bottom', fontsize = 10, color = 'black')
plt.title('Histogram of Wheel Base')
plt.xticks(bin_edges, rotation = 45)
plt.xlabel('Wheel Base')
plt.ylabel('Frequency')
plt.show()


print("-----------------------Horsepower----------------------------")
plt.figure()
counts, bin_edges, _  =  plt.hist(Carros4['horsepower_lim'], bins = 10, edgecolor = 'black')
for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha = 'center', va = 'bottom', fontsize = 10, color = 'black')
plt.title('Histogram of Horsepower Lim')
plt.xticks(bin_edges, rotation = 45)
plt.xlabel('Horsepower Lim')
plt.ylabel('Frequency')
plt.show()

# Plot histogram for 'horsepower'
plt.figure()
counts, bin_edges, _  =  plt.hist(Carros4['horsepower'], bins = 10, edgecolor = 'black')
for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha = 'center', va = 'bottom', fontsize = 10, color = 'black')
plt.title('Histogram of Horsepower')
plt.xticks(bin_edges, rotation = 45)
plt.xlabel('Horsepower')
plt.ylabel('Frequency')
plt.show()


#Linha 9 Calcular a correlação entre as variáveis do passo 7, original e a limitada, e a variável
#price. Que podemos concluir?
print("\n\n-----------------------Correlação----------------------------")
corr_wheel_base_lim_price = Carros4['wheel-base_lim'].corr(Carros4['price'])
corr_wheel_base_price = Carros4['wheel-base'].corr(Carros4['price'])
print(f"A correlação entre wheel_base e price é {corr_wheel_base_price}")
print(f"A correlação entre wheel_base_lim e price é {corr_wheel_base_lim_price}")
print("Após a correção dos outliers na variavel wheel-base, verifica-se um ligeiro decréscimo da correlação da variavel wheel-base e o price.\
      Isto mostra que os outliers não estavam distorcendo a relação entre wheel-base e price.")

corr_horsepower_lim_price = Carros4['horsepower_lim'].corr(Carros4['price'])
corr_horsepower_price = Carros4['horsepower'].corr(Carros4['price'])
print(f"A correlação entre horsepower e price é {corr_horsepower_price}")
print(f"A correlação entre horsepower_lim e price é {corr_horsepower_lim_price}")
print("Após a correção dos outliers na variavel horsepower, verifica-se um ligeiro aumento da correlação da variavel horsepower e o price.\
      Isto mostra que os outliers não estavam distorcendo a relação entre horsepower e price.")


#Linha 10 Considerando a variável quantitativa com maior número de outliers segundo os cálculos   
#do passo 5, criar uma nova variável com base nessa, como o sufixo “_decil”, que corresponde 
#ao valor da variável quando agrupada em 10 decis.
print("A variável engine-size tem o maior numero de outliers(5).")
Carros4['engine-size_decil'] = pd.qcut(Carros4['engine-size'], q = 10, labels = False) + 1




#Linha 11 Considerando as variáveis do passo anterior, original e a limitada, compara os seus 
#histogramas.
print("-----------------------Engine-Size----------------------------")
plt.figure()
counts, bin_edges, _  =  plt.hist(Carros4['engine-size_decil'], bins = 10, edgecolor = 'black')
for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha = 'center', va = 'bottom', fontsize = 10, color = 'black')
plt.title('Histogram of Engine Size Decil')
plt.xticks(bin_edges, rotation = 45)
plt.xlabel('Engine Size Decil')
plt.ylabel('Frequency')
plt.show()


plt.figure()
counts, bin_edges, _  =  plt.hist(Carros4['engine-size'], bins = 10, edgecolor = 'black')
for count, bin_edge in zip(counts, bin_edges[:-1]):  
    plt.text(bin_edge + (bin_edges[1] - bin_edges[0]) / 2, count, int(count),  
             ha = 'center', va = 'bottom', fontsize = 10, color = 'black')
plt.title('Histogram of Engine Size')
plt.xticks(bin_edges, rotation = 45)
plt.xlabel('Engine Size')
plt.ylabel('Frequency')
plt.show()

# Linha 12 Calcula a correlação entre as variáveis do passo 10, original e a limitada, e a variável price.
#Que podes concluir?
print("\n\n-----------------------Correlação Engine-Size/ Engine-Size_decil vs Price----------------------------")
corr_engine_size_decil_price = Carros4['engine-size_decil'].corr(Carros4['price'])
print(f"A correlação entre engine_size_decil e price é {corr_engine_size_decil_price}")

corr_engine_size_price = Carros4['engine-size'].corr(Carros4['price'])
print(f"A correlação entre engine_size e price é {corr_engine_size_price}")

print("\nO décil reduz o efeito dos outliers, pois agrupa os valores em faixas e minimiza sua influência direta.\
      \nPodemos concluir que a correlação diminuiu significativamente (de 0.87 para 0.76),\
      o que indica que os outliers estavam amplificando a relação entre engine-size e price.")


# Linha 13 Exportar os dados de Carros4 num ficheiro csv com o nome Carros5
Carros4.to_csv('3_exploratory_data_analysis/aula4/Carros5.csv', index = False)
