
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
    def saca(self, valor):
        self.__saldo -= valor
    def trafere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
