import pandas as pd
import os

df = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/datascience/datascience_course/data_science_fundamentals/Projeto/data/logistics_data.csv")

print(df.head())
result_folder="C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/datascience/datascience_course/data_science_fundamentals/Projeto/result/"

pending_requests=df[df['Status'] =='Pending']
print(pending_requests)


with open(f"{result_folder}/pending_shipments.txt", "w") as f:
    f.write(f"Remessas Pending programadas\n {pending_requests}\n")