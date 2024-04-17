import pandas as pd

# Leggi il file Excel
df = pd.read_excel('file.xls')
print(df)
# Converti il DataFrame in JSON
df.to_json('data.json', orient='records', lines=True)