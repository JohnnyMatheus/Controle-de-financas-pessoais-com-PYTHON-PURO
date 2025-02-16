from model import Conta,engine
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
        print(conta.banco)


#conta = Conta(valor=10, banco=Bancos.INTER)
#criar_conta(conta)
desativar_conta(1)

print(listar_contas())