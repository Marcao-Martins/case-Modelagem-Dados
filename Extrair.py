import sqlite3
conn = sqlite3.connect('database.db')


# criando um cursor
cursor = conn.cursor()

# executando a consulta
cursor.execute("SELECT COUNT(DISTINCT Order_Number) FROM tabela WHERE strftime('%m', Date) = '12' AND Store_Name = 'Super Baratão'")

# recuperando o resultado
resultado = cursor.fetchone()[0]

# exibindo o resultado
print(f"A loja Super Baratão teve {resultado} pedidos únicos no mês de Dezembro.")


#----------------------------------------------------------------------------------------------------------------------------------------------------#


cursor = conn.execute("""
    SELECT strftime('%m', Date) as Month, 
           AVG(CASE WHEN Orden_revisada = 'No' OR Orden_aprobada = 'No' THEN 1 ELSE 0 END) as Rejection_Rate
    FROM tabela
    WHERE Store_Name = 'Mercado Marisol'
    GROUP BY Month
    ORDER BY Rejection_Rate DESC
    LIMIT 1;
""")

# Obtendo o resultado da consulta
result = cursor.fetchone()

# Exibindo o resultado
print(f"O mês com a maior taxa de rejeição da loja Mercado Marisol foi {result[0]} com uma taxa de rejeição de {result[1]*100:.2f}%")


#----------------------------------------------------------------------------------------------------------------------------------------------------#


cursor.execute("SELECT COUNT(DISTINCT id) FROM tabela WHERE store_name = 'Mercado Preço Baixo' AND strftime('%Y-%m', Date) = '2022-12'")

# obtém o resultado da consulta
resultado = cursor.fetchone()[0]

# exibe o resultado
print("O número de usuários que fizeram pedidos na loja Mercado Preço Baixo no mês de Dezembro foi:", resultado)




#----------------------------------------------------------------------------------------------------------------------------------------------------#

cursor.execute("SELECT Brand_Name, strftime('%Y', Date) as Ano, COUNT(*) as TotalPedidos FROM tabela WHERE strftime('%Y', Date) IN ('2022', '2023') GROUP BY Brand_Name, Ano")

# Obter os resultados e separar em duas listas (uma para cada ano)
resultados_2022 = []
resultados_2023 = []
for linha in cursor.fetchall():
    loja, ano, total_pedidos = linha
    if ano == '2022':
        resultados_2022.append((loja, total_pedidos))
    else:
        resultados_2023.append((loja, total_pedidos))


conn.commit()

# fechar a conexão com o banco de dados
conn.close()