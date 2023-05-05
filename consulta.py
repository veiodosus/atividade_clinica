class Consulta():

    def __init__(self, id, medico, paciente, data, convenio = None, retorno = False, com_retorno = False, data_retorno = None, paga = False, cancelada = False):
        self.__id = id
        self.__medico = medico
        self.__paciente = paciente
        self.__data = data
        self.__convenio = convenio
        self.__retorno = retorno
        self.__com_retorno = com_retorno
        self.__data_retorno = data_retorno
        self.__paga = paga
        self.__cancelada = cancelada

    @property
    def id(self):
        return self.__id
    
    @property
    def medico(self):
        return self.__medico

    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def data(self):
        return self.__data

    @property
    def convenio(self):
        return self.__convenio

    @property
    def retorno(self):
        return self.__retorno

    @property
    def com_retorno(self):
        return self.__com_retorno
    
    @property
    def data_retorno(self):
        return self.__data_retorno

    @property
    def paga(self):
        return self.__paga

    @property
    def cancelada(self):
        return self.__cancelada

    def __str__(self) :
        return f'ID: {self.__id} | Data: {self.__data.strftime("%d/%m/%Y")} | Médico: {self.__medico.nome} | Paciente: {self.__paciente.nome}.'

    def pagar_consulta(self):
        self.__paga = True

    def remarcar_consulta(self, data):
        self.__data = data

    def cancelar_consulta(self):
        self.__cancelada = True
    
    def adicionar_retorno(self):
        self.__com_retorno = True