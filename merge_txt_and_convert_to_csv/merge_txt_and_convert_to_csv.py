import os
import pandas as pd

# Test to explore file
#txt_file = 'DesmatamentoMunicipios2000.txt'
#encoding_type = 'ISO-8859–1'

#dataset=pd.read_csv(txt_file,encoding=encoding_type)
#dataset.head()

# Set the path to the files that you want to process (or use the current path)

path = os.getcwd()
#path = "C:\\Users\\Ricardo\\Desktop\\dados"
files = os.listdir(path)

# Set the encoding type
encoding_type = 'ISO-8859–1'

print("Path location:")
print(path)

files_txt = [f for f in files if f[-3:] == 'txt']

print("Files to merge:")
print(files_txt)

all_data = []
for f in files_txt:
    info = pd.read_csv(f,encoding=encoding_type,header=None,skiprows=1)
    info['File'] = str(f[-8:-4])
    all_data.append(info)


df = pd.concat(all_data, ignore_index=True, sort=False)
df.columns =['Nr','Lat','Long','Latgms','Longms','Municipio','CodIbge','Estado',\
             'AreaKm2','DesmatadoAno','IncrementoAnoAnt','FlorestaAno','NuvemAno',\
             'NaoObservadoAno','NaoFlorestaAno','HidrografiaAno','Soma','Ano']

print("Columns:")
print(df.columns)

print("Shape:")
print(df.shape)

print("Top 5 rows:")
print(df.head())

df.to_csv("dados-consolidados.csv", index = False, sep=';', encoding='utf-8')

print("All txt files were merged and converted to a csv file")