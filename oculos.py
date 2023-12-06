import random
class Lente:
    def __init__(self, grau, marca):
        self.grau = grau
        self.marca = marca

 #polimorfismo
    def verificar_cpf(self):
            pass

class Armacao(Lente):
    def __init__(self, grau, marca, cor, modelo, preco, protecao_uv):
        super().__init__(grau, marca)
        self.__cor = cor
        self.__modelo = modelo
        self.preco = preco
        self.protecao_uv = protecao_uv
#Polimorfismo
    def verificar_cpf(self):
        return ("\nO seu cpf está limpo, pode comprar!\n")

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
    @property
    def escolher_modelo(self):
        return self.__modelo

    @escolher_modelo
    def escolher_modelo(self,novo_modelo):
        self.__modelo =novo_modelo



 #getter
    @property
    def escolher_cor(self):
     return self.__cor

#setter
    @escolher_cor.setter
    def escolher_cor(self,nova_cor):
      self.__cor = nova_cor

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

# Polimorfismo
class Teste(Lente):
    def __init__(self):
        super().__init__(grau=None, marca=None)

    def verificar_cpf(self):
        return "\nO seu cpf está limpo, pode comprar na melhor!\n"



print("=====Bem-vindo à Ótica da Ana🕶️🕶️🕶️=====")
print("===Melhores modelos e preços só aqui!===")

oculos = Armacao(grau=None, marca="Sutéro", cor=None, modelo=None, preco=random.randint(100, 1000), protecao_uv=None)
oculos2=Teste()

print(oculos.verificar_cpf())
print(oculos2.verificar_cpf())

oculos.escolher_lente()
novo_modelo=input("escreva o modelo que voce deseja:")
oculos.escolher_modelo =novo_modelo

nova_cor=input("\nInsira a cor que deseja para o seu oculos:")
oculos.escolher_cor =nova_cor

oculos.colocar_protecao_uv()
oculos.fazer_pagamento()
Armacao.receber_brinde()
oculos.finalizar_compra()



print(f"\nÓtima compra! Seu óculos da marca {oculos.marca}, modelo {oculos.escolher_modelo}, cor {oculos.escolher_cor}, preço {oculos.preco}, com proteção UV: {oculos.protecao_uv}, foi comprado com sucesso!!😎😎")