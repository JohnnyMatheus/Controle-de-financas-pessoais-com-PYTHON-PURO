from model import Conta,engine,Bancos, Status
from sqlmodel import Session,select

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco==conta.banco)
        results = session.exec(statement).all()
        print(results)

        if results:
            print('Já existe uma conta nesse banco')
            return
        session.add(conta)
        session.commit()
        return conta



def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
    return results


def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id ==id)
        conta = session.exec(statement).first()
        if conta.valor > 0:
            raise ValueError('Essa conta ainda possui saldo!')
        conta.status = Status.INATIVO
        session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada,valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id_conta_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente')
        
        statement = select(Conta).where(Conta.id==id_conta_entrada)
        conta_entrada = session.exec(statement).first()
        
        conta_saida.valor -= valor
        conta_entrada.valor += valor
        session.commit()
        
        #print(conta_saida)

#conta = Conta(valor=0, banco=Bancos.INTER)
#conta = Conta(valor=10, banco=Bancos.SANTANDER)
#conta = Conta(valor=10, banco=Bancos.NUBANK)

#criar_conta(conta)
#desativar_conta(1)

transferir_saldo(2,3,1)
#print(listar_contas())