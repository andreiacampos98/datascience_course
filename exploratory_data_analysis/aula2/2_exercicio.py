import pandas as pd
a=['Renault', 'Fiat', 'BMW']
print(a)
print(type(a))

b=['Twingo', '6oo', 'X5']
print(b)
print(type(b))

dicionario=dict(zip(a,b))
print(dicionario)
print(type(dicionario))

new_dicionario={'marca': a,
                'modelo':b}
print(new_dicionario)
print(type(new_dicionario))

df_dicionario=pd.DataFrame.from_dict(dicionario, orient='index')
print(df_dicionario)
print(type(df_dicionario))
print(df_dicionario.iloc[1])

new_df_dicionario=pd.DataFrame(new_dicionario)
print(new_df_dicionario)
print(f"O tipo de variavel do new_df_dicionario é {type(new_df_dicionario)}")
print(f"Linha 2 do dataframe\n{new_df_dicionario.loc[1]}")
