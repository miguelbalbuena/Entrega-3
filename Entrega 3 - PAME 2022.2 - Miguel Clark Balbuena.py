class Gerente:
    def __init__(self, id, usuario, senha, nome, area) -> None:
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.area = area
        self.projetos = []

    def ver_dados(self):
        print(f"ID: {self.id}, Usuário: {self.usuario}, Nome: {self.nome}, Área: {self.area}")
    
    def alterar_dados(self):
        altera = input("Deseja mudar o usuário?(Sim ou Não): ")
        if altera == "Sim":
            usuario_novo = input("Usuário novo: ")
            self.usuario = usuario_novo

        altera = input("Deseja alterar o nome?(Sim ou Não): ")
        if altera == "Sim":
            nome_novo = input("Nome novo: ")
            self.nome = nome_novo
        
        altera = input("Deseja mudar a senha?(Sim ou Não): ")
        if altera == "Sim":
            senha_nova = input("Senha nova: ")
            self.senha = senha_nova

        altera = input("Deseja mudar a área? (Sim ou Não): ")
        if altera == "Sim":
            area_nova = input("Área nova: ")
            self.area = area_nova
        
    def ver_projetos(self):
        for projeto in sistema.projetos:
            if projeto.gerente.id == self.id:
                print(projeto.nome)

    def avancar_entregar_projeto(self, projeto):

        if projeto.fase < 3:
            print(f"O projeto {projeto.nome} se situa na fase {projeto.fase}.")
            altera = input("Deseja avançar a fase do projeto? (Sim ou Não): ")
            if altera == "Sim":
                projeto.fase = projeto.fase + 1
                projeto.avancar_entregar = False
                print(f"O projeto {projeto.nome} avançou para {projeto.fase} fase.")
            else:
                projeto.avancar_entregar = False
                print(f"O projeto {projeto.nome} ficou na {projeto.fase} fase.")
        
        elif projeto.fase == 3:
            print(f"O projeto {projeto.nome} se situa na fase {projeto.fase}.")
            entrega = input("Deseja realizar a entrega? (Sim ou Não): ")
            if entrega == "Sim":
                sistema.remover_projeto(projeto)
                print(f"O projeto {projeto.nome} foi entregue.")
            else:
                projeto.avancar_entregar = False
                print(f"O projeto {projeto.nome} não foi entregue.")

    def transferir_projeto(self, projeto, gerente_novo):
        if not gerente_novo.projetos:
            gerente_novo.projetos.append(projeto)
            self.projetos.remove(projeto)
            projeto.gerente = gerente_novo
            print(f"O projeto {projeto.nome} foi devidamente transferido para o gerente {gerente_novo}")
        else:
            print(f"O gerente {gerente_novo.nome} não pode aceitar pois já possui projetos.")

class Consultor(Gerente):
    def __init__(self, id, usuario, senha, nome, area) -> None:
        super().__init__(id, usuario, senha, nome, area)

    def ver_dados(self):
        super().ver_dados()

    def alterar_dados(self):
        super().alterar_dados()
    
    def ver_projetos(self):
        for projeto in self.projetos:
            print(projeto.nome)

class Projeto:
    def __init__(self, nome, gerente, consultores, area, cliente) -> None:
        self.nome = nome
        self.gerente = gerente
        self.consultores = consultores
        self.area = area
        self.cliente = cliente
        self.etapa = 1
        self.avancar_entregar = False

    def mais_consultor(self, consultor):
        self.consultores.append(consultor)
        consultor.projetos.append(self)

    def retirar_consultor(self, consultor):
        self.consultores.remove(consultor)
        consultor.projetos.remove(self)

    def ver_dados(self):
        return self.nome

class Sistema:
    def __init__(self) -> None:
        self.consultores = []
        self.gerentes = []
        self.projetos = []
        self.pendencias = []
    
    def menu(self):
        while True:
            print("\n")
            print("A - Novo consultor")
            print("B - Retirar consultor")
            print("C - Novo gerente")
            print("D - Retirar gerente")
            print("E - Novo projeto")
            print("F - Retirar projeto")
            print("G - Mostrar consultores/gerentes/projetos")
            print("H - Entrar como consultor")
            print("I - Entrar como gerente")
            print("J - Sair")
            opcao = input("Escolha sua opção de desejo: ")
            print("\n")

            if opcao == "A":

                id = input("Insira o ID: ")
                usuario = input("Insira o usuário: ")
                senha = input("Insira a senha: ")
                nome = input("Insira o nome: ")
                area = input("Insira a área: ")
            
                self.novo_consultor(id, usuario, senha, nome, area)
                print(f"Novo consultor {nome} criado com êxito.")

            elif opcao == "B":
                id = input("Insira o ID do consultor do qual você deseja remover: ")
                consultor = self.mostrar_consultor(id)

            elif opcao == "E":
                nome = input("Criar projeto:")
                projeto = self.mostrar_projeto(projeto)
                if not projeto:
                    self.criar_projeto(projeto):
                    print(f"{projeto.nome} criado.")

            elif opcao == "F":
                nome = input("Retirar projeto: ")
                projeto = self.mostrar_projeto(projeto)

                if projeto:
                    self.retirar_projeto(projeto)
                    print(f"{projeto.nome} retirado.")
                
                else:
                    print(f"Nome inválido.")
            
            elif opcao == "G":
                self.listar()

            elif opcao == "H":
                id = input("Insira seu ID: ")
                senha = input("Insira sua senha: ")
                self.entrar_consultor(id, senha)
            
            elif opcao == "I":
                id = input("Insira seu ID: ")
                senha = input("Insira sua senha: ")
                self.entrar_gerente(id, senha)
            
            elif opcao == "J": break

            else:
                print("A opção não está registrada nos campos.")
        
    def entrar_consultor(self, id, senha):
        for consultor in self.consultores:
            if consultor.id == id and consultor.senha == senha:
                print (f"Seja bem vindo, {consultor.nome}!")
                while True:
                    print("\n")
                    print("A - Ver dados")
                    print("B - Alterar dados")
                    print("C - Mostrar projetos")
                    print("D - Avançar projeto")
                    print("E - Sair de projeto")
                    print("F - Sair")
                    opcao = input("Digite a opção desejada: ")
                    print("\n")

                    if opcao == "A":
                        consultor.mostrar_dados()
                    if opcao == "B":
                        consultor.altera_dados()
                    elif opcao == "C":
                        consultor.mostrar_projetos()
                    elif opcao == "D":
                        resposta = input("Selecione o projeto: ")
                        projeto = self.mostrar_projeto(resposta)
                        if projeto:
                            if consultor in projeto.consultores:
                                projeto.permissao_avancar_ou_entregar = True
                                print(f"Pedido realizado, aguardando permissão.")

                            else:
                                print("Não é consultor.")
                        else: 
                            print("Projeto não existe")

                    elif opcao == "E":
                        resposta = input("Selecione o projeto: ")
                        projeto = self.mostrar_projetos(resposta)
                        if projeto: 
                            if consultor in projeto.consultores:
                                self.pendencias.append([consultor, pronjeto])
                                print(f"Pedido feito, aguardando permissão")
                            else:
                                print("Não é consultor.")
                        else:
                            print("Projeto não existe")
                    elif opcao == "F": break
                    else:
                        print("Opção inexistente.")
            else: 
                print("Dados inválidos.")
    def entrar_gerente(self, id, senha):
        for gerente in self.gerentes:
            if gerente.id == id and gerente.senha == senha:
                print(f"Seja bem vindo, {gerente.nome}!")
                print("\n")

                while True:
                    print("\n")
                    print("A - Ver dados")
                    print("B - Alterar dados")
                    print("C - Mostrar projetos")
                    print("D - Avançar projeto")
                    print("E - Sair de projeto")
                    print("F - Transferir projeto")
                    print("G - Sair")

sistema=Sistema()
sistema.menu()
