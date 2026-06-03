
cadastro=[]


class Funcionario:

    def __init__(self,nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


    # O método da classe cuida APENAS de mostrar a si mesmo (Usa self!)
    def exibir_cadastro(self):
        print(f" Nome: {self.nome} | Cargo: {self.cargo} | Salário: R${self.salario}")






def confirmacao(nome,cargo,salario):
    print("Confirme se os dados estão certos:")
    print(f"Nome:{nome} , Cargo: {cargo} , Salário: {salario}")

    opcao = input("Os dados estão corretos? (S/N)").upper()

    if opcao == "S":
        novo_funcionario = Funcionario(nome,cargo,salario)
        cadastro.append(novo_funcionario)
        print("Cadastro feito com sucesso!")
        return True

    elif opcao == "N":
        print("Cadastro cancelado. Reiniciando")
        return False



def menu():
    while True:
        print(" --- MENU PRINCIPAL --- ")
        print("O que deseja fazer?")
        print("1 - Cadastrar funcionário")
        print("2 - Ver lista de funcionários cadastrados")
        print("3 - SAIR")
        menu_opcao = int(input("Qual a opção?"))

        if menu_opcao == 1:
            while True:
                nome = input("Qual o nome do funcionário?")
                cargo = input("Qual o cargo?")
                salario = float(input("Seu salário em R$:"))
                if confirmacao(nome,cargo,salario):
                    break
        elif menu_opcao == 2:
            print(" --- CADASTRO ---")
            if not cadastro:
                print("Cadastro vazio")
            else:
                for func in cadastro:
                    func.exibir_cadastro()
        elif menu_opcao == 3:
            print("Desligando sistema")
            break
        else:
            print("Erro! Tente novamente")


menu()
            




