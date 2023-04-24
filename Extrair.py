import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("SELECT COUNT(DISTINCT Order_Number) FROM tabela WHERE strftime('%m', Date) = '12' AND Store_Name = 'Super Baratão'")

resultado = cursor.fetchone()[0]

print(f"A loja Super Baratão teve {resultado} pedidos únicos no mês de Dezembro.")

cursor.execute("""
SELECT strftime('%m', Date) as Month,
AVG(CASE WHEN Orden_revisada = 'No' OR Orden_aprobada = 'No' THEN 1 ELSE 0 END) as Rejection_Rate
FROM tabela
WHERE Store_Name = 'Mercado Marisol'
GROUP BY Month
ORDER BY Rejection_Rate DESC
LIMIT 1;
""")

result = cursor.fetchone()

print(f"O mês com a maior taxa de rejeição da loja Mercado Marisol foi {result[0]} com uma taxa de rejeição de {result[1]*100:.2f}%")

cursor.execute("SELECT COUNT(DISTINCT id) FROM tabela WHERE store_name = 'Mercado Preço Baixo' AND strftime('%Y-%m', Date) = '2022-12'")

resultado = cursor.fetchone()[0]

print("O número de usuários que fizeram pedidos na loja Mercado Preço Baixo no mês de Dezembro foi:", resultado)

cursor.execute("""
SELECT
Store_Name,
strftime('%Y', Date) as Ano,
COUNT(*) as TotalPedidos
FROM
tabela
WHERE
strftime('%Y', Date) IN ('2022', '2023')
GROUP BY
Store_Name,
Ano;
""")

resultados = cursor.fetchall()

totais_lojas = {}

for linha in resultados:
    store_name, ano, total_pedidos = linha
    if store_name not in totais_lojas:
        totais_lojas[store_name] = {}
    totais_lojas[store_name][ano] = total_pedidos

df = pd.DataFrame.from_dict(totais_lojas, orient='index')

df = df.stack().reset_index().rename(columns={'level_0': 'Store_Name', 'level_1': 'Year', 0: 'TotalPedidos'})

sns.catplot(x='Store_Name', y='TotalPedidos', hue='Year', data=df, kind='bar', height=6, aspect=2)

plt.savefig('grafico.png', dpi=300, bbox_inches='tight')

cursor.execute("""
SELECT
Store_Name,
strftime('%Y', Date) as Ano,
COUNT(DISTINCT Order_Number) as TotalPedidos
FROM
tabela
WHERE
strftime('%Y', Date) IN ('2022', '2023')
GROUP BY
Store_Name,
Ano;
""")

resultados = cursor.fetchall()

totais_lojas = {}

for linha in resultados:
    store_name, ano, total_pedidos = linha
    if store_name not in totais_lojas:
        totais_lojas[store_name] = {}
    totais_lojas[store_name][ano] = total_pedidos

df = pd.DataFrame.from_dict(totais_lojas, orient='index')

df['Variacao'] = (df['2023'] / df['2022'] - 1) * 100

print(df)

conn.commit()

conn.close()
