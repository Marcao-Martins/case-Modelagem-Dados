import csv
import sqlite3
import re

# estabelecer conexão com o banco de dados
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS tabela (id INTEGER,Date DATE, User_Phone_Number TEXT, Brand_ID INTEGER, Brand_Name TEXT, Store_Name TEXT, Order_Number TEXT, Orden_revisada TEXT, Orden_aprobada TEXT, Submission_Amount REAL, Quantity_SKU INTEGER, Quantity_Itens INTEGER)')

# abrir o arquivo CSV e ler os dados
with open('/workspaces/case-estagio/dados.csv') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    
    # pular a primeira linha, que contém os nomes das colunas
    next(leitor_csv)
    
    # inserir os dados na tabela "tabela"
    for linha in leitor_csv:
        # converter a string com vírgulas para um único valor
        linha[1] = re.sub(r',(?=\d)', '', linha[1])
        
        conn.execute('INSERT INTO tabela ( id,Date, User_Phone_Number, Brand_ID, Brand_Name, Store_Name, Order_Number, Orden_revisada, Orden_aprobada, Submission_Amount, Quantity_SKU, Quantity_Itens) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', linha)

# salvar as alterações no banco de dados
conn.commit()

# fechar a conexão com o banco de dados
conn.close()
