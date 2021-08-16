import pandas as pd


data = pd.DataFrame()
data = pd.read_csv('/Users/kimsumin/Desktop/final project_final/ThreadAdded/파이슨자료/house_info_result.csv')
middle_list = pd.read_csv('/Users/kimsumin/Desktop/final project_final/ThreadAdded/파이슨자료/df_middle_district_list.csv')
data = data.filter(regex='^(?!Unnamed).+', axis="columns")
data.drop_duplicates(['name'])

data=data.drop_duplicates(['url'],keep='first')
data.to_csv('cleansing_result.csv')
print(len(data))
