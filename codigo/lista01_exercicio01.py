class Veiculo:

    def __init__(self):
        self.__marca = ""
        self.__modelo = ""
        self.__ano = 0
        self.__velocidade_atual = 0
        self.__ligado = False

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def set_velocidade_atual(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual

    def get_ligado(self):
        return self.__ligado

    def set_ligado(self, ligado):
        self.__ligado = ligado

    def acelerar(self, quantidade):
        self.__velocidade_atual += quantidade

    def frear(self, quantidade):
        self.__velocidade_atual -= quantidade
        if self.__velocidade_atual < 0:
            self.__velocidade_atual = 0