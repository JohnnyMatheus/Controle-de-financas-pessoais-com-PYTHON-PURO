from sqlmodel import SQLModel, Field, create_engine
from enum import Enum

class Bancos(Enum):
    NUBANK ='Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'

class Status(Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'   

class Conta(SQLModel,table =True):
    id: int =Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)


sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url, echo=False)  

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)  


if __name__ == "__main__":  
    create_db_and_tables()  