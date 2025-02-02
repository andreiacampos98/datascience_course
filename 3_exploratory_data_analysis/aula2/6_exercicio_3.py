import pandas as pd
#1
path='/home/acer/Desktop/datascience_course/exploratory_data_analysis/aula2/7_data2.csv'
#2
dados = pd.read_csv(path)
#3
print(dados)

#4
print(dados.info())
print(dados.describe())


print(dados.dtypes)

#5
print(dados.duplicated().any())

#6
print(dados.drop_duplicates(inplace=True))
#fazer reset index
print(dados.info())

#7
dados['tran_date']=dados['tran_date'].dt.strftime('%d/%m/%y')

#8
dados['tran_date']=pd.to_datetime(dados['tran_date'], dayfirst=True)
print(dados.info())

#9
dicio={'e-shop': ['E-shop', 'e-shop'],
       'mbr': ['Mbr', 'MBR', 'mbr'],
       'teleshop': ['Teleshop']}

#10
dados['Store_type']=dados['Store_type'].map(dicio)
print(dados)