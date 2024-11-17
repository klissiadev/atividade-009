import university as university
from university import University
from professor import Professor
from discipline import  Discipline


#VARIABLES
option = 1
index = 0
index_dep = 0
index_prof = 0
index_dis = 0
menu_active = 1
active = True
universities = []
teachers = []
disciplines = []

def print_hi(name):
    print(f'Hi, {name}')


def consult_department(university, index):
    global universities, option, menu_active, active
    while True:  # Loop to handle user actions in this menu
        print("\nCONSULTAR DEPARTAMENTO")
        print("------------------------------------\n")

        department = university.departments[index]
        teachers = department.professors

        print(f"DEPARTAMENTO {department.name}\n")
        print(f"Nome: {department.name}\n")
        print(f"Professores: ")

        for i in teachers:
            print(i.name)

        print("\nO que deseja fazer a seguir?\n")
        print("1 - CONTRATAR UM PROFESSOR\n")
        print("2 - ADICIONAR DISCIPLINA NOVA A PROFESSOR\n")
        print("3 - ADICIONAR DISCIPLINA\n")
        print("4 - DEMITIR PROFESSOR\n")
        print("5 - RETIRAR DISCIPLINA DA EMENTA\n")
        print("6 - VOLTAR AO MENU PRINCIPAL\n")
        print("7 - FECHAR PROGRAMA\n")

        option = int(input("Escolha uma das opções: "))

        if option == 1:
            print("Criar professor")
        elif option == 2:
            print("Adicionar disciplina nova a professor")
        elif option == 3:
            print("Adicionar disciplina")
        elif option == 4:
            print("Demitir professor")
        elif option == 5:
            print("Retirar disciplina da ementa")
        elif option == 6:
            menu_active = 1
            break
        elif option == 7:
            active = False
            break
        else:
            print("Opção inválida, tente novamente.\n")



def consult_university(index):
    global universities, option, menu_active, active, index_dep
    while True:  # Loop to handle user actions in this menu
        count = 0
        print("\nCONSULTAR UNIVERSIDADE ESPECÍFICA")
        print("------------------------------------\n")

        university = universities[index]
        departments = university.departments

        print(f"UNIVERSIDADE {university.name}\n")
        print(f"Nome: {university.name}\n")
        print(f"Departamentos: ")

        for i in departments:
            print(f"{count + 1} - {i.name}")
            count = count + 1

        print("\nO que deseja fazer a seguir?\n")
        print("1 - CRIAR UM DEPARTAMENTO\n")
        print("2 - ACESSAR DEPARTAMENTO\n")
        print("3 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("4 - FECHAR PROGRAMA\n")

        option = int(input("Escolha uma das opções: "))

        if option == 1:
            university.create_department()
        elif option == 2:
            index_dep = int(input("Insira o numero do departamento: ")) - 1
            consult_department(university,index_dep)
        elif option == 3:
            menu_active = 1
            break
        elif option == 4:
            active = False
            break
        else:
            print("Opção inválida, tente novamente.\n")


def consult_professors():
    global universities, option, menu_active, teachers, index_prof, active
    count = 1
    print("\nCONSULTAR PROFESSORES")
    print("------------------------------------\n")

    while True:

        for i in teachers:
            print(f"{count} - {i.name}")
            count = count + 1

        print("\nO que deseja fazer a seguir?\n")
        print("1 - CONSULTAR UM PROFESSOR\n")
        print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("3 - FECHAR PROGRAMA\n")
        option = int(input("Escolha uma das opções: "))


        if option == 1:
            index_prof = int(input("Insira o numero do professor: ")) - 1
            teachers[index_prof].consult_teacher()
            print("\nO que deseja fazer a seguir?\n")
            print("1 - CONSULTAR UM PROFESSOR\n")
            print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
            print("3 - FECHAR PROGRAMA\n")
            option = int(input("Escolha uma das opções: "))
        elif option == 2:
            menu_active = 1
            break
        elif option == 3:
            active = False
            break
        else:
            print("opção invalida, tente novamente\n")

def consult_disciplines():
    global universities, option, menu_active, teachers, disciplines, index_dis, active
    count = 1
    print("\nCONSULTAR DISCIPLINAS")
    print("------------------------------------\n")

    while True:

        for i in disciplines:
            print(f"{count} - {i.name}")
            count = count + 1

        print("\nO que deseja fazer a seguir?\n")
        print("1 - CONSULTAR UMA DISICPLINA\n")
        print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("3 - FECHAR PROGRAMA\n")
        option = int(input("Escolha uma das opções: "))


        if option == 1:
            index_dis = int(input("Insira o numero do professor: ")) - 1
            disciplines[index_dis].consult_discipline
            print("\nO que deseja fazer a seguir?\n")
            print("1 - CONSULTAR UM PROFESSOR\n")
            print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
            print("3 - FECHAR PROGRAMA\n")
            option = int(input("Escolha uma das opções: "))
        elif option == 2:
            menu_active = 1
            break
        elif option == 3:
            active = False
            break
        else:
            print("opção invalida, tente novamente\n")

def consult_universities():
    global universities, option, menu_active, active
    count = 1
    print("\nCONSULTAR UNIVERSIDADEs")
    print("------------------------------------\n")

    while True:

        for i in universities:
            print(f"{count} - {i.name}")
            count = count + 1

        print("\nO que deseja fazer a seguir?\n")
        print("1 - ENTRAR EM UMA UNIVERSIDADE\n")
        print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("3 - FECHAR PROGRAMA\n")
        option = int(input("Escolha uma das opções: "))


        if option == 1:
            index = int(input("Insira o numero da universidade: ")) - 1
            consult_university(index)
        elif option == 2:
            menu_active = 1
            break
        elif option == 3:
            active = False
            break
        else:
            print("opção invalida, tente novamente\n")


def create_discipline():
    global universities, option, menu_active, active, teachers, disciplines
    print("\nCRIAR DISCIPLINA")
    print("------------------------------------\n")

    while True:

        name = str(input("Insira o nome da disciplina: "))

        discipline = Discipline(name)

        disciplines.append(discipline)

        print("\nDisciplina criada! O que deseja fazer a seguir?\n")
        print("1 - CONSULTAR INFORMAÇÃO DE DISCIPLINA\n")
        print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("3 - FECHAR PROGRAMA\n")
        option = int(input("Escolha uma das opções: "))


        if option == 1:
           discipline.consult_discipline()
           print("\nO que deseja fazer a seguir?\n")
           print("1 - CONSULTAR INFORMAÇÃO DE PROFESSOR\n")
           print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
           print("3 - FECHAR PROGRAMA\n")
           option = int(input("Escolha uma das opções: "))
        elif option == 2:
            menu_active = 1
            break
        elif option == 3:
            active = False
            break
        else:
            print("opção invalida, tente novamente\n")


def create_professor():
    global universities, option, menu_active, active, teachers
    print("\nCRIAR PROFESSOR")
    print("------------------------------------\n")

    while True:

        name = str(input("Insira o nome do professor: "))
        age = int(input("Insira a idade do professor: "))

        professor = Professor(name, age)
        teachers.append(professor)

        print("\nProfessor criado! O que deseja fazer a seguir?\n")
        print("1 - CONSULTAR INFORMAÇÃO DE PROFESSOR\n")
        print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("3 - FECHAR PROGRAMA\n")

        option = int(input("Escolha uma das opções: "))

        if option == 1:
            professor.consult_teacher()
            print("\nO que deseja fazer a seguir?\n")
            print("1 - CONSULTAR INFORMAÇÃO DE PROFESSOR\n")
            print("2 - VOLTAR PARA O MENU PRINCIPAL\n")
            print("3 - FECHAR PROGRAMA\n")
            option = int(input("Escolha uma das opções: "))
        elif option == 2:
            menu_active = 1  # Atualiza o menu_active para voltar ao menu principal
            break
        elif option == 3:
            active = False  # Define active como False para fechar o programa
            break
        else:
            print("Opção inválida, tente novamente.\n")


def create_university():
    global universities, option, menu_active, active
    print("\nCRIAR UNIVERSIDADE")
    print("------------------------------------\n")

    while True:

        name = str(input("Insira o nome da universidade: "))

        university = University(name)

        universities.append(university)

        print("\nUniversidade criada! O que deseja fazer a seguir?\n")
        print("1 - CRIAR OUTRA UNIVERSIDADE\n")
        print("2 - ENTRAR NA UNIVERSIDADE\n")
        print("3 - VOLTAR PARA O MENU PRINCIPAL\n")
        print("4 - FECHAR PROGRAMA\n")
        option = int(input("Escolha uma das opções: "))


        if option == 1:
            create_university()
        elif option == 2:
            function_index = universities.index(university)
            consult_university(function_index)
        elif option == 3:
            menu_active = 1
            break
        elif option == 4:
            active = False
            break
        else:
            print("opção invalida, tente novamente\n")



def menu():
    global option, menu_active, active

    print("\nBEM-VINDO AO SISTEMA UNIVERSITÁRIO")
    print("------------------------------------\n")

    print("1 - CRIAR UNIVERSIDADE\n")
    print("2 - CONSULTAR UNIVERSIDADES\n")
    print("3 - CRIAR PROFESSOR\n")
    print("4 - CONSULTAR PROFESSORES\n")
    print("5 - CRIAR DISCIPLINA\n")
    print("6 - CONSULTAR DISCIPLINAS\n")
    print("7 - FECHAR PROGRAMA\n")

    option = int(input("Escolha uma das opções: "))

    if option == 1:
        menu_active = 2
    elif option == 2:
        menu_active = 3
    elif option == 3:
        menu_active = 5
    elif option == 4:
        menu_active = 7
    elif option == 5:
        menu_active = 6
    elif option == 6:
        menu_active = 8
    elif option == 7:
        active = False
    else:
        print("opção invalida, tente novamente\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while active:

        if menu_active == 1:
            menu()
        elif menu_active == 2:
            create_university()
        elif menu_active == 3:
            consult_universities()
        elif menu_active == 4:
            consult_university(index)
        elif menu_active == 5:
            create_professor()
        elif menu_active == 6:
            create_discipline()
        elif menu_active == 7:
            consult_professors()
        elif menu_active == 8:
            consult_disciplines()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
