import pandas as pd

# 1. Carrega a planilha para dentro de uma estrutura chamada DataFrame (df)
# Se o seu arquivo for .csv, mude para: pd.read_csv('dados.csv')

df = pd.read_csv('rotina_escolar.csv')

#print(df)

#print(df.info())   # Mostra informações sobre o DataFrame, como número de linhas, colunas e tipos de dados

#print(df.head())    # Mostra as primeiras linhas do DataFrame
#
#df.describe()      # Mostra estatísticas descritivas das colunas numéricas do DataFrame


#print(df.describe()) # estatísticas descritivas das colunas numéricas do Data Frame

#print(df.drop_duplicates())   # Remove linhas duplicadas do DataFrame e exibe o resultado