
import pandas as pd



df = pd.read_csv(r"/home/acer/Desktop/datascience_course/3_exploratory_data_analysis/aula1/2_Transactions.csv")

print(df.head())
print(df.isnull())
print(df.info())

df['tran_date']=df['tran_date'].str.replace('/', '-')
df['tran_date']=pd.to_datetime(df['tran_date'])
df['prod_subcat_code']=df['prod_subcat_code'].astype(str)
df['prod_cat_code']=df['prod_cat_code'].astype(str)
print(df.info())
print(df.head())