import csv
import sqlite3
import re

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS tabela (id INTEGER,Date DATE, User_Phone_Number TEXT, Brand_ID INTEGER, Brand_Name TEXT, Store_Name TEXT, Order_Number TEXT, Orden_revisada TEXT, Orden_aprobada TEXT, Submission_Amount REAL, Quantity_SKU INTEGER, Quantity_Itens INTEGER)')

with open('/workspaces/case-estagio/dados.csv') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    
    next(leitor_csv)
    
    for linha in leitor_csv:
        # converter a string com vírgulas para um único valor
        linha[1] = re.sub(r',(?=\d)', '', linha[1])
        
        conn.execute('INSERT INTO tabela ( id,Date, User_Phone_Number, Brand_ID, Brand_Name, Store_Name, Order_Number, Orden_revisada, Orden_aprobada, Submission_Amount, Quantity_SKU, Quantity_Itens) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', linha)

conn.commit()

# fechar a conexão com o banco de dados
conn.close()
