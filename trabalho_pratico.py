import pandas as pd

pd.set_option("display.max_rows", 9999)

df = pd.read_csv("dados.csv", sep=";", engine="python",
                 encoding="utf-8", quotechar="'")

print("[Passo 5a] Informações gerais:")
df.info()
print("\n[Passo 5b] Primeiras 5 linhas:")
print(df.head(5))
print("\n[Passo 5b] Últimas 5 linhas:")
print(df.tail(5))

df_limpo = df.copy()

df_limpo["Calories"] = df_limpo["Calories"].fillna(0)
print("\n[Passo 7b] Dataframe após tratar Calories:")
print(df_limpo.to_string())

df_limpo["Date"] = df_limpo["Date"].fillna("1900/01/01")
print("\n[Passo 8b] Dataframe após tratar Date:")
print(df_limpo.to_string())

try:
    pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except ValueError as e:
    print("\n[Passo 8c] Erro esperado:", e)

df_limpo["Date"] = df_limpo["Date"].replace("1900/01/01", float("nan"))
try:
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except ValueError as e:
    print("\n[Passo 9b] Erro esperado:", e)
print("\n[Passo 9c] Dataframe após substituir por NaN:")
print(df_limpo.to_string())

df_limpo["Date"] = df_limpo["Date"].replace(
    "20201226", pd.to_datetime("20201226", format="%Y%m%d"))

df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
print("\n[Passo 11] Dataframe após conversão de Date:")
print(df_limpo.to_string())

df_limpo = df_limpo.dropna(subset=["Date"])

print("\n[Passo 13] Dataframe final:")
print(df_limpo.to_string())
print()
df_limpo.info()
