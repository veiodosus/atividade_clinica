import datetime

def listar_consultas(lista_de_consu, retorno = None, com_retorno = None, paga = None, cancelada = None):
    print('')
    if paga == False:
        for n in range(len(lista_de_consu)):
            if lista_de_consu[n].paga == False and lista_de_consu[n].cancelada == False:
                print(lista_de_consu[n])
    elif cancelada == False:
        for n in range(len(lista_de_consu)):
            if lista_de_consu[n].cancelada == False and lista_de_consu[n].paga == False:
                print(lista_de_consu[n])
    elif paga == True:
        for n in range(len(lista_de_consu)):
            if lista_de_consu[n].cancelada == False and lista_de_consu[n].paga == True:
                print(lista_de_consu[n])
    elif retorno == None and com_retorno == None and paga == None and cancelada == None:
        for n in range(len(lista_de_consu)):
            print(lista_de_consu[n])

def listar(lista):
    print('')
    for n in range(len(lista)):
        print(lista[n])

def escolher_pessoa(lista, valor):
    for n in range(len(lista)):
        if lista[n].id == valor:
            return lista[n]
    print('\nO ID digitado é inválido.')

def menu():
    print('\n[1]_ Marcar consulta.    [2]_ Remarcar consulta. [3]_ Listar consultas.    [4]_ Marcar retorno.')
    print('[5]_ Pagar consulta.     [6]_ Cancelar consulta. [7]_ Relatório do médico. [8]_ Relatório da clínica.')
    print('[9]_ Cadastrar paciente. [10]_ Cadastrar médico. [0]_ Encerrar programa.')

def escolha_interface():
    while True:
        try:
            digito = int(input('\nEscolha uma opção: '))
            if digito < 0 or digito > 10:
                raise Exception
            else:
                return digito
        except:
            print('\nEscolha inválida. Tente novamente!')

def entradas_med(tipo, lista_med):
    lista_id = []
    for n in range(len(lista_med)):
        lista_id.append(lista_med[n].id)
    if tipo == 'id':
        while True:
            try:
                id = int(input('\nDigite o ID do médico: '))
                if id in lista_id:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'crm':
        while True:
            try:
                crm = input('\nDigite o crm: ')
                return crm
            except:
                print('\nCRM inválido. Tente novamente.')
    elif tipo == 'nome':
        while True:
            try:
                nome = input('\nDigite o nome: ')
                return nome
            except:
                print('\nNome inválido. Tente novamente.')
    elif tipo == 'especialidade':
        while True:
            try:
                especialidade = input('\nDigite a especialidade: ')
                return especialidade
            except:
                print('\nEspecialidade inválida. Tente novamente.')

def entradas_pac(tipo, lista_pac):
    lista_id = []
    for n in range(len(lista_pac)):
        lista_id.append(lista_pac[n].id)
    if tipo == 'id':
        while True:
            try:
                id = int(input('\nDigite o ID do paciente: '))
                if id in lista_id:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'nome':
        while True:
            try:
                nome = input('\nDigite o nome: ')
                return nome
            except:
                print('\nNome inválido. Tente novamente.')
    elif tipo == 'dt_nascimento':
        while True:
            try:
                dt_nasc = input('\nDigite a data de nascimento: ')
                dt_nascimento = datetime.datetime.strptime(dt_nasc, '%d/%m/%Y')
                return dt_nascimento
            except:
                print('\nData inválida. Tente novamente.')
    elif tipo == 'contato':
        while True:
            try:
                contato = input('\nDigite o contato: ')
                return contato
            except:
                print('\nContato inválido. Tente novamente.')

def entradas_consu(tipo, lista_consu, lista_med, lista_pac):
    lista_id_med = []
    lista_id_pac = []
    lista_id = []
    for n in range(len(lista_med)):
        lista_id_med.append(lista_med[n].id)
    for n in range(len(lista_pac)):
        lista_id_pac.append(lista_pac[n].id)
    for n in range(len(lista_consu)):
        lista_id.append(lista_consu[n].id)
    if tipo == 'id':
        while True:
            try:
                id = int(input('\nDigite o ID da consulta: '))
                if id in lista_id:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'id_escolhido_med':
        while True:
            try:
                id = int(input('\nDigite o ID escolhido: '))
                if not id in lista_id_med:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'id_escolhido_pac':
        while True:
            try:
                id = int(input('\nDigite o ID escolhido: '))
                if not id in lista_id_pac:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'id_escolhido_consu':
        while True:
            try:
                id = int(input('\nDigite o ID escolhido: '))
                if not id in lista_id:
                    raise Exception
                return id
            except:
                print('\nID inválido. Tente novamente.')
    elif tipo == 'data':
        while True:
            try:
                data = input('\nDigite a data: ')
                data = datetime.datetime.strptime(data, '%d/%m/%Y')
                return data
            except:
                print('\nData inválida. Tente novamente.')