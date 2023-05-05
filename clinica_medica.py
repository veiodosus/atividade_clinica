from paciente import Paciente
from medico import Medico
from consulta import Consulta
from funcoes import *

def main():
    data = datetime.datetime.now()
    lista_paciente = [Paciente(1, 'Jorge', data, 123), 
                      Paciente(2, 'Marcelo', data, 321), 
                      Paciente(3, 'Alberto', data, 456), 
                      Paciente(4, 'Fulano', data, 544)]
    lista_medico = [Medico(1, 123, 'Nico', 'Ortopedista'),
                    Medico(2, 321, 'Ciclano', 'Dentista'),
                    Medico(3, 456, 'Kelvin', 'Veterinário'),
                    Medico(4, 654, 'Baiano', 'Astrólogo')]
    lista_consulta = [Consulta(1, lista_medico[1], lista_paciente[1], data),
                      Consulta(2, lista_medico[2], lista_paciente[2], data),
                      Consulta(3, lista_medico[3], lista_paciente[3], data)]

    while True:
        menu()

        escolha = escolha_interface()

        if escolha == 1:
            id = entradas_consu('id', lista_consulta, lista_medico, lista_paciente)
            while True:
                try:
                    print('\nEscolha o médico cadastrado.')
                    listar(lista_medico)
                    id_medico = entradas_consu('id_escolhido_med', lista_consulta, lista_medico, lista_paciente)
                    if id_medico == None:
                        raise Exception
                    break
                except:
                    print('\nID inválido. Tente novamente.')
            while True:
                try:
                    medico = escolher_pessoa(lista_medico, id_medico)
                    print('\nEscolha o paciente cadastrado.')
                    listar(lista_paciente)
                    id_paciente = entradas_consu('id_escolhido_pac', lista_consulta, lista_medico, lista_paciente)
                    if id_paciente == None:
                        raise Exception
                    break
                except:
                    print('ID inválido!')
            paciente = escolher_pessoa(lista_paciente, id_paciente)
            data = entradas_consu('data', lista_consulta, lista_medico, lista_paciente)
            lista_consulta.append(Consulta(id, medico, paciente, data))
            print(f'\n{lista_consulta[3]}')
        elif escolha == 2:
            pass
        elif escolha == 3:
            if len(lista_consulta) == 0:
                print('\nNão há consultas para listar.')
            else:
                listar_consultas(lista_consulta)
        elif escolha == 4:
            if len(lista_consulta) == 0:
                print('\nNão há consultas pagas.')
            else:
                listar_consultas(lista_consulta, paga = True)
                id_consu = entradas_consu('id_escolhido_consu', lista_consulta, lista_medico, lista_paciente)
                consulta = escolher_pessoa(lista_consulta, id_consu)
                if consulta.com_retorno == True:
                    print('Consulta já possui retorno.')
                else:
                    consulta.adicionar_retorno()
                    id = entradas_consu('id', lista_consulta, lista_medico, lista_paciente)
                while True:
                    try:
                        print('\nEscolha o médico cadastrado.')
                        listar(lista_medico)
                        id_medico = entradas_consu('id_escolhido_med', lista_consulta, lista_medico, lista_paciente)
                        if id_medico == None:
                            raise Exception
                        break
                    except:
                        print('\nID inválido. Tente novamente.')
                while True:
                    try:
                        medico = escolher_pessoa(lista_medico, id_medico)
                        print('\nEscolha o paciente cadastrado.')
                        listar(lista_paciente)
                        id_paciente = entradas_consu('id_escolhido_pac', lista_consulta, lista_medico, lista_paciente)
                        if id_paciente == None:
                            raise Exception
                        break
                    except:
                        print('ID inválido!')
                paciente = escolher_pessoa(lista_paciente, id_paciente)
                data = entradas_consu('data', lista_consulta, lista_medico, lista_paciente)
                lista_consulta.append(Consulta(id, medico, paciente, data, retorno = True))
        elif escolha == 5:
            if len(lista_consulta) == 0:
                print('\nNão há consultas para pagar.')
            else:
                listar_consultas(lista_consulta, paga = False) 
                id_consu = entradas_consu('id_escolhido_consu', lista_consulta, lista_medico, lista_paciente)
                consulta = escolher_pessoa(lista_consulta, id_consu)
                if consulta.paga == True:
                    print('Consulta já está paga.')
                else:
                    consulta.pagar_consulta()
        elif escolha == 6:
            if len(lista_consulta) == 0:
                print('\nNão há consultas para pagar.')
            else:
                listar_consultas(lista_consulta, cancelada = False) 
                id_consu = entradas_consu('id_escolhido_consu', lista_consulta, lista_medico, lista_paciente)
                consulta = escolher_pessoa(lista_consulta, id_consu)
                if consulta.cancelada == True:
                    print('Consulta já está cancelada.')
                else:
                    consulta.cancelar_consulta()
        elif escolha == 7:
            pass
        elif escolha == 8:
            pass
        elif escolha == 9:
            id = entradas_pac('id', lista_paciente)
            nome = entradas_pac('nome', lista_paciente)
            dt_nasc = entradas_pac('dt_nascimento', lista_paciente)
            contato = entradas_pac('contato', lista_paciente)
            lista_paciente.append(Paciente(id, nome, dt_nasc, contato))
        elif escolha == 10:
            id = entradas_med('id', lista_medico)
            crm = entradas_med('crm', lista_medico)
            nome = entradas_med('nome', lista_medico)
            especialidade = entradas_med('especialidade', lista_medico)
            lista_medico.append(Medico(id, crm, nome, especialidade))
        elif escolha == 0:
            break

if __name__ == '__main__':
    main()