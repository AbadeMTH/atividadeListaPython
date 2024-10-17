#Engenharia de Software - Software Básico - UMC
#07/10/2024
import os
import re

os.system('cls')

L1 = [['123', 'matheus', 'analista', 5423.0], ['1234', 'junior', 'analista', 5423.0]]

def InputMatrVerificada(perguntaInput):
    matr = ''
    while matr == '':
        matrTemp = input(f'\n{perguntaInput}')
        if re.match(r'^\d+$', matrTemp):
            matr = matrTemp
            return matr
        else:
            os.system('cls')
            print('\nDigite um valor válido.')
            matr = ''

def InputNumerosFloatVerificado(perguntaInput):
    dado = ''
    while dado == '':
        dadoTemp = input(f'\n{perguntaInput}')
        if re.match(r'^\d+(\.\d+)?$', dadoTemp):
            dado = float(dadoTemp)
            return dado
        else:
            os.system('cls')
            print('\nDigite um valor válido.')
            dado = ''

def InputTextoVerificado(perguntaInput):
    dado = ''
    while dado == '':
        dadoTemp = input(f'\n{perguntaInput}')
        if re.match(r'^[A-Za-z]+$', dadoTemp):
            dado = dadoTemp
            return dado
        else:
            os.system('cls')
            print('\nDigite um texto válido.')
            dado = ''

def VerificaMatrExiste(matr):
    for linha in range(0, len(L1)):
        if matr == L1[linha][0]:
            return linha

def AdicionarMatricula(matr):
    matrExiste = VerificaMatrExiste(matr)

    #Se a matrícula não exisitir adiciona
    if matrExiste != None:
        os.system('cls')
        print('\nA matrícula ja existe.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        nm = InputTextoVerificado(perguntaInput='\nDigite o nome: ')
            
        cg = InputTextoVerificado(perguntaInput='\nDigite o cargo: ')
        
        sal = InputNumerosFloatVerificado(perguntaInput='\nDigite o salário: ')

        L1.append([matr, nm, cg, sal])

def AlterarMatricula(matr):
    matrExiste = VerificaMatrExiste(matr)

    if matrExiste == None:
        print('\nA matrícula não existe.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        print(f'\nDigite em seguida a alteração dos dados da matrícula: {matr}')

        nm = InputTextoVerificado(perguntaInput='\nDigite o nome: ')
            
        cg = InputTextoVerificado(perguntaInput='\nDigite o cargo: ')
        
        sal = InputNumerosFloatVerificado(perguntaInput='\nDigite o salário: ')

        L1[matrExiste] = [L1[matrExiste][0], nm, cg, sal]

def ExcluiMatricula(matr):
    matrExiste = VerificaMatrExiste(matr)

    if matrExiste == None:
        print('\nA matrícula não existe.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        del L1[matrExiste]

def PesquisaPorNome(nm):
    os.system('cls')
    for linha in range(0, len(L1)):
        if nm == L1[linha][1]:
            print('\nRegistro de matrícula de acordo com o nome informado:\n')
            print(f'Matrícula: {L1[linha][0]} | Nome: {L1[linha][1]} | Cargo: {L1[linha][2]} | Salário: {L1[linha][3]}\n')
            input('\nPressione ENTER para voltar ao menu.')
            return
        
    print(f'\nNenhum registro com o nome {nm} foi encontrado.')
    input('\nPressione ENTER para voltar ao menu.')    
        

def RelatorioGeral():
    os.system('cls')
    if len(L1) == 0:
        print('\nNenhum registro encontrado.')
        input('\nPressione ENTER para voltar ao menu.')
    else:
        for linha in range(0, len(L1)):
            print(f'\nMatrícula: {L1[linha][0]} | Nome: {L1[linha][1]} | Cargo: {L1[linha][2]} | Salário: {L1[linha][3]}\n')
        
        input('\nPressione ENTER para voltar ao menu.')

while True:
    os.system('cls')
    menuOpç = input('''
    Escolha uma opção 
    (1) Adicionar Matricula
    (2) Alteração Baseado na Matricula
    (3) Exclusão Baseado na Matricula
    (4) Relatório Geral
    (5) Pesquisa por Nome
    (6) Fim do programa
    
    ===> ''') 

    #verificar se o usuario colocou a opção correta
    if menuOpç not in ['1', '2', '3', '4', '5', '6']:
        os.system('cls')
        print('Opção inválida.\n')
        input('Digite ENTER para voltar ao menu.')
    
    #Adicionar matricula 
    elif menuOpç == '1':
        os.system('cls')
        matr = InputMatrVerificada('\nDigite o número de matrícula que deseja adicionar: ')
        AdicionarMatricula(matr)
    
    #Alteracao Baseado na Matricula
    elif menuOpç =='2':
        os.system('cls')
        matr = InputMatrVerificada(perguntaInput='\nDigite o número de matrícula que deseja alterar: ')
        AlterarMatricula(matr)

    #Exclusão baseado na matrícula
    elif menuOpç == '3':
        os.system('cls')
        matr = InputMatrVerificada('\nDigite a matrícula que deseja excluir o registro: ')
        ExcluiMatricula(matr)

    #Relatorio Geral
    elif menuOpç =='4': 
        os.system('cls')
        RelatorioGeral()
        
    #Pesquisa por nome
    elif menuOpç == '5':
        os.system('cls')
        nm = InputTextoVerificado(perguntaInput='\nDigite o nome que deseja pesquisar em nosso sistema: ')
        PesquisaPorNome(nm)
        
    #Saída
    else:
        print('FIM DO PROGRAMA')
        break
