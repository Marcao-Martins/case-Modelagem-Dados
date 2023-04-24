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




conn.commit()

# fechar a conexão com o banco de dados
conn.close()