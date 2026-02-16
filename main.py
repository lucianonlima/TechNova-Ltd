import pandas as pd

# Ler dados
df = pd.read_csv("data/sales.csv")

print("\nPrimeiras linhas do dataset:")
print(df.head())

print("\nResumo estatístico:")
print(df.describe())

# Criar coluna de faturamento
df["revenue"] = df["price"] * df["quantity"]

# Total vendido
print("\nTotal de vendas:", df["revenue"].sum())

# Produto mais vendido
top_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("\nProdutos mais lucrativos:")
print(top_product)
