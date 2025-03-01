import pandas as pd

import plotly.express as px


df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")



df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month


locations = df['Location'].unique()

months = range(1, 13)  # De 1 a 12

anos_disponiveis = sorted(df['Year'].unique())
base_df = df[['Location', 'Year', 'Month']].drop_duplicates()



#Evolução da temperatura máxima média mensal ao longo do tempo
df_monthly_temp = df.groupby(['Location','Year', 'Month'])['MaxTemp'].mean().reset_index()


month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']



df['dif_temp_max_min']=df['MaxTemp'] - df['MinTemp']
df_monthly_temp_max_min = df.groupby(['Location','Year', 'Month'])['dif_temp_max_min'].mean().reset_index()




#numero de dias com temperatura máxima 35
dias_acima_35=df[df['MaxTemp'] > 35].groupby(['Location','Year', 'Month'])['MaxTemp'].count().reset_index()
dias_acima_35.rename(columns={'MaxTemp': 'DaysAbove35'}, inplace=True)

dias_acima_35 = base_df.merge(dias_acima_35, on=['Location', 'Year', 'Month'], how='left')
dias_acima_35['DaysAbove35'] = dias_acima_35['DaysAbove35'].fillna(0)

dias_acima_35.to_csv("dias_acima_35.csv", index=False)

#numero de dias com temperatura abaixo de 0
dias_abaixo_0=df[df['MinTemp'] < 0].groupby(['Location','Year', 'Month'])['MinTemp'].count().reset_index()
dias_abaixo_0.rename(columns={'MinTemp': 'DaysBelow0'}, inplace=True)

