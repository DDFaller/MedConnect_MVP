from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from sqlalchemy import text
# importando os elementos definidos no modelo
from models.base import Base
from models.schedule import Schedule



# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'postgresql://postgres:0812@localhost:5432/mvp'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)
session = Session()


# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

s1 = Schedule("Dr. Alvaro", "Lara","2023-09-10","Unimed","Barao","21996925019")
print(session.query(Schedule).all())