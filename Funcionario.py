
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


# Classe filha (Subclasse)
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario,bonus):
        # Entendi que o bonus apareceu em cima pq é p construtor de Gerente()
        # E o super() chama os dados do construtor da classe Funcionario
        # mas pq o self.bonus = bonus está de baixo do super()? não era pra estar de baixo do primeiro construtor?

        # Basicamente seria o seguinte: Começou a conexão de herança Gerente(Funcionario), termine primeiro a herança, 
        # dps complemente com o que falta da subclasse

        super().__init__(nome, cargo, salario)
        self.bonus = bonus
    
    def exibir_cadastro(self):
        super().exibir_cadastro()
        print(f"Bônus de Gerencia: R$ {self.bonus}")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, cargo, salario, linguagem_programacao):    
        super().__init__(nome, cargo, salario)
        self.linguagem_programacao=linguagem_programacao

    def exibir_cadastro(self):
        super().exibir_cadastro(self)
        print(f"linguage de programação: {self.linguagem_programacao}")

    






# Para ter um costume mais profissional, usasse comandos que relembre o main do JAVA.
if __name__ == "__main__": 
# Se este arquivo aqui for o principal que o usuário está executando
# diretamente (dando play), execute a função menu()

    while True:
        print(" --- MENU PRINCIPAL --- ")
        print("O que deseja fazer?")
        print("1 - Cadastrar funcionário")
        print("2 - Ver lista de funcionários cadastrados")
        print("3 - SAIR")
        menu_opcao = int(input("Qual a opção?"))


# Com base na adição de subclasses, Gerente e Desenvolvedor, com o intuito de praticar herança e polimorfismo,
# precisa atualizar o menu para escolher uma das 3 opções


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




