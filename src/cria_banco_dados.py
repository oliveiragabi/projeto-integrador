# arquivo que inicia o banco de dados e apaga antigo, se houver
import sqlite3 as sql

con = sql.connect('db.sqlite') # conector com banco de dados
cur =con.cursor()
cur.execute('DROP TABLE IF EXISTS client') # substitui tabela, caso exista

table_clients = ''' CREATE TABLE "client" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "SERVICO" VARCHAR(10) NOT NULL,
    "DENTRADA" VARCHAR(10) NOT NULL,
    "DSAIDA" VARCHAR(10) NULL,
    "DESCRICAO" VARCHAR(60) NOT NULL,
    "EQUIPAMENTO" VARCHAR(30) NOT NULL,
    "NOME" VARCHAR(30) NOT NULL,
    "ENDERECO" VARCHAR(50) NOT NULL,
    "FONE" INTEGER(12) NOT NULL,
    "ORCAMENTO" VARCHAR(200) NOT NULL
          
);

''' 

cur.execute(table_clients) # colocar os campos na tabela
con.commit()     # registra dados
con.close()      # fecha banco

# ao final da execução criará o arquivo de BD