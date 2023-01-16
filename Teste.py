class Pessoa:

#init e o que cria o objeto
#self e o nome do objeto a ser invocado, responsavel por vincular os atributos com os argumentos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("hello, world")

pessoa1 = Pessoa("Jonas", 31)
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar()

class Casa:
    def __init__(self, moradores, quartos) -> None:
        self.moradores = moradores
        self.quartos = quartos
    
    def get_quartos(self):
        return self.quartos

    def set_quartos(self, n_quartos):
        self.quartos = n_quartos

    def entrar(self):
        print("Abrir porta.")
        print("Entra na casa")
        print("Fecha porta")

    def dormir(self):
        print("Deitar na cama")
        print("Boa noite")
    
    def ouvir_musica(self, musica):
        print(f"Estou escutando {musica}")

class Apartamento(Casa):#apartamento vai herdar os atributos de casa
    
    def __init__(self, moradores, quartos, vizinhos) -> None:
        super().__init__(moradores,quartos)
        self.vizinhos = vizinhos

    def ouvir_musica(self, musica, passou_das_10: bool):
        if passou_das_10:
            print("Nada de musica")
        else:
            print(f"Estou escutando {musica}")

    def subir_elevador(self):
        print("Subi de elevador")

    def entrar(self):
        self.subir_elevador()
        super().entrar()

ap1 = Apartamento(2, 2, 7)
ap1.ouvir_musica("Los Hermanos", True)
#se passou_das_10 for True, nada de musica, se False, estou ouvindo "Los Hermanos"
ap1.entrar()
print(ap1.moradores)

#Para encapsular argumentos, colocar __ antes, ai ela ficara privada
