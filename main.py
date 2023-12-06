import random
class Lente:
    def __init__(self, grau, marca):
        self.grau = grau
        self.marca = marca

class Armacao(Lente):
    def __init__(self, grau, marca, cor, modelo, preco, protecao_uv):
        super().__init__(grau, marca)
        self.__cor = cor
        self.modelo = modelo
        self.preco = preco
        self.protecao_uv = protecao_uv

    def escolher_lente(self):
        grau = input("\nVocê usa oculos com grau? (s/n):").lower()
        try:
            if grau == "s":
                self.grau = float(input("Insira o grau dos seus óculos: "))
                print("Ok, grau adicionado no seu óculos 👓")
            else:
                print("Que bom, sua vista está boa!👓")
        except ValueError:
            print("Valor inválido!")
            return

    def escolher_modelo(self):
        modelo = input("\nEscolha qual modelo deseja comprar: Gatinho(1), Redondo(2), Quadrado(3)")
        if modelo == "1":
            self.modelo = "Gatinho"
            print(f"Ótima escolha, modelo Gatinho selecionado!")
        elif modelo == "2":
            self.modelo = "Redondo"
            print(f"Bom gosto, Redondo selecionado!")
        elif modelo == "3":
            self.modelo = "Quadrado"
            print(f"Combina com você, Quadrado selecionado!!")
        else:
            print("Valor inválido, insira um valor válido")

    @property
    def escolher_cor(self):
        return self.__cor

    @escolher_cor.setter
    def escolher_cor(self,nova_cor):
        self.__cor=nova_cor


    def colocar_protecao_uv(self) :
        protecao_uv = input("\nDeseja colocar proteção UV no seu óculos? (s/n):").lower()
        try:
            if protecao_uv == "s":
                self.protecao_uv = True
                print("No seu óculos foi adicionado proteção UV")
            else:
                self.protecao_uv = False
                print("O seu óculos não contém proteção UV")
        except ValueError:
            print("Valor inválido!")

    def fazer_pagamento(self):
        print("\nPara pagamento à vista 10% de desconto!!💸💸")
        print(f"Valor do oculos sem denconto {self.preco}")
        pagamento = input("\nO pagamento vai ser parcelado ou à vista, à vista(1) parcelado(2):")
        try:
            if pagamento == "1":
                desconto = self.preco * 0.1
                self.preco -= desconto
                print(f"O valor do seu óculos com o desconto à vista é {self.preco}")
            else:
                print(f"O valor do óculos é {self.preco} e as parcelas foram feitas em 3 vezes")
        except ValueError:
            print("Valor inválido!")
            return

    @staticmethod
    def receber_brinde():
        verificcao = input("\nDeseja receber um brinde ao finalizar compra?(s/n):").lower()
        if verificcao == "s":
            print("Ok , você recebeu brinde 🎉")
        else:
            print("opa, você nao recebeu brinde 😕")

    def finalizar_compra(self):
        verificacao = input("\nO seu óculos é para presente?🤔 (s/n):").lower()
        try:
            if verificacao == "s":
                print("Que legal, seu presente está embrulhado e pronto!!🎁🎁")
            else:
                print("Ok, compra finalizada")
        except ValueError:
            print("Valor inválido!")



print("=====Bem-vindo à Ótica da Ana🕶️🕶️🕶️=====")
print("===Melhores modelos e preços só aqui!===")

oculos = Armacao(grau=None, marca="Sutéro", cor=None, modelo=None, preco=random.randint(100, 1000), protecao_uv=None)

oculos.escolher_lente()
oculos.escolher_modelo()

nova_cor=input("\nInsira a cor que desja para o seu oculos:")
oculos.escolher_cor = nova_cor

oculos.colocar_protecao_uv()
oculos.fazer_pagamento()
Armacao.receber_brinde()
oculos.finalizar_compra()



print(f"\nÓtima compra! Seu óculos da marca {oculos.marca}, modelo {oculos.modelo}, cor {oculos.escolher_cor}, preço {oculos.preco}, com proteção UV: {oculos.protecao_uv}, foi comprado com sucesso!!😎😎")