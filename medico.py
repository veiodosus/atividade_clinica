class Medico():
    def __init__(self, id, crm, nome, especialidade):
        self.__id = id
        self.__crm = crm
        self.__nome = nome
        self.__especialidade = especialidade
        self.__consultas = []

    def __str__(self) -> str:
        return f'ID: {self.__id} | CRM: {self.__crm} | Nome: {self.__nome} | Especialidade: {self.__especialidade}'
    
    @property
    def id(self):
        return self.__id
    
    @property
    def crm(self):
        return self.__crm

    @property
    def nome(self):
        return self.__nome
    
    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def consultas(self):
        return self.__consultas