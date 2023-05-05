class Paciente():
    
    def __init__(self, id, nome, dt_nasc, contato):
        self.__id = id
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__contato = contato
        self.__consultas = []

    def __str__(self):
        return f'ID: {self.__id} | Nome: {self.__nome} | Data de Nascimento: {self.__dt_nasc.strftime("%d/%m/%Y")} | Contato: {self.__contato}'
    
    @property
    def id(self):
            return self.__id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def dt_nasc(self):
        return self.__dt_nasc
    
    @property
    def contato(self):
        return self.__contato
    
    @property
    def consultas(self):
        return self.__consultas