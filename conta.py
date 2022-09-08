
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Cronstruindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo: {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_saca(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_saca(valor)):
            self.__saldo -= valor
            print(f"Seu saldo é: {self.__saldo}")
        else:
            print("Você não tem saldo o suficiente!")
    def trafere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
