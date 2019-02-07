import pandas as pd
inp=pd.read_csv('task1/input.txt',sep=',',encoding='UTF-16',engine='python',header=None,escapechar='\\')
new_header=inp.iloc[0]
inp=inp[1:]
inp.columns=new_header
inp.set_index('year',inplace=True)
pop_2010=pd.to_numeric(inp['2010'],errors='coerce')
