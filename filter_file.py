import pandas as pd

#df = pd.read_csv('data_files/commentData_TOI_Nov_19_till_Mar_20.csv')
df = pd.read_csv('data_files/working_dir/commentData_TOI_Apr_20_till_Aug_20.csv')

df = df.dropna(subset=['C_T'])
df = df[['_id', 'C_T']]

#df.to_csv('data_files/commentData_TOI_Nov_19_till_Mar_20_filtered.csv', index=False, encoding='utf-8')
df.to_csv('data_files/working_dir/commentData_TOI_Apr_20_till_Aug_20_filtered.csv', index=False, encoding='utf-8')
