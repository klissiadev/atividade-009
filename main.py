import university as university
from university import University
from professor import Professor
from discipline import  Discipline

#arrays
professors = []
disciplines = []
universities = []

def see_professor_list(department):
    global professors

    print("Professores: ")
    if len(professors) > 0:
        for i, professor in enumerate(professors):
            if (professor.department is None or professor.department == department) and len(professor.disciplines) < 5:
                status = "Disponível"
            else:
                status = "Indisponível"

            professor.status = status
            print(f"{i + 1} - {professor.name} : {professor.status}")

        return True
    else:
        print("Não há professores disponíveis")
        return False

def see_discipline_list():
    global disciplines

    print("Disciplinas: ")
    if len(disciplines) > 0:
        for i, discipline in enumerate(disciplines):
            print(f"{i + 1} - {discipline.name}")

        return True
    else:
        print("Não há disciplinas disponíveis")
        return False

def create_discipline(name):
    global disciplines
    discipline = Discipline(name)
    disciplines.append(discipline)

def create_professor(name, age):
    global professors
    for i in range(len(professors)):
        if professors[i].name == name:
            print('Este professor já esta cadastrado.')
            return False
    professor = Professor(name, age, len(professors))
    professors.append(professor)
    return True

def create_university(key):
    global universities
    for i in range(len(universities)):
        if universities[i].name == key:
            print(f'A universidade informada já existe.')
            return False
    op = input('Selecione o tipo:\n 1- Pública\n 2- Privada: ')
    if op == '1':
        university = University(key,'Pública')
    elif op == '2':
        university = University(key,'Privada')
    else:
        university = University(key, ' ')
    universities.append(university)
    return True

def delete_university(university):
    global universities
    print(f'\nDeletando a universidade ... {university.name}')
    for i in range(len(university.departments) - 1, -1, -1):  # runs from last to first
        university.departments[i].delete_department()
    universities.remove(university)
    del university
    return True

def menu():
    print("\nBEM-VINDO AO SISTEMA UNIVERSITÁRIO")
    print("------------------------------------\n")

    while True:

        print("\n1 - CADASTRAR UNIVERSIDADE")
        print("\n2 - CONSULTAR UNIVERSIDADES")
        print("\n3 - CRIAR PROFESSOR")
        print("\n4 - CONSULTAR PROFESSORES")
        print("\n5 - CRIAR DISCIPLINA")
        print("\n6 - CONSULTAR DISCIPLINAS")
        print("\n7 - FECHAR PROGRAMA")

        option = int(input("\nEscolha uma das opções: "))

        if option == 1:
            print("\nCadastrando nova universidade...")
            name = str(input(("\nInsira o nome da universidade: ")))
            if create_university(name):
                print("\nUniversidade cadastrada com sucesso!")
        elif option == 2:
            print("\nConsultando universidades...")
            for i, uni in enumerate(universities):
                print(f"\n{i+1} - {uni.name}")
            index = int(input("\nEscolha uma universidade para consultar: ")) - 1

            if index >= 0 and index < len(universities):
                uni = universities[index]
                uni_menu(uni)
            else:
                print("\nopção inválida, tente novamente.")
        elif option == 3:
            print("\nCadastrando novo professor...")
            name = str(input(("\nInsira o nome do(a) professor(a): ")))
            age = str(input(("\nInsira a idade do(a) professor(a): ")))
            if create_professor(name, age):
                print("\nProfessor(a) cadastrado com sucesso!")
        elif option == 4:
            print("\nConsultando professores...\n")
            for i, professor in enumerate(professors):
                print(f"{i + 1} - {professor.name}\n")

            index = int(input("\nEscolha um professor para consultar: ")) - 1

            if index >= 0 and index < len(professors):
                print("\nConsultando Professor:\n")
                professor = professors[index]
                professor.consult_professor()
            else:
                print("\nopção inválida, tente novamente.")
        elif option == 5:
            print("\nCadastrando nova disciplina...")
            name = str(input(("\nInsira o nome da disciplina: ")))
            create_discipline(name)
            print("\nDisciplina cadastrada com sucesso!")
        elif option == 6:
            print("\nConsultando disciplinas...\n")
            for i, discipline in enumerate(disciplines):
                print(f"\n{i + 1} - {discipline.name}\n")

            index = int(input("\nEscolha uma disciplina para consultar: ")) - 1

            if index >= 0 and index < len(disciplines):
                print("\nConsultando Disciplina:\n")
                discipline = disciplines[index]
                discipline.consult_discipline()
        elif option == 7:
            exit()
        else:
            print("\nopção invalida, tente novamente\n")


def uni_menu(university):
    print("\nPORTAL DA UNIVERSIDADE")
    print("\n------------------------------------")
    university.consult_university()

    while True:

        print("\n1 - CADASTRAR DEPARTMANENTO")
        print("\n2 - CONSULTAR DEPARTAMENTOS")
        print("\n3 - CONSULTAR INFO DESTA UNIVERSIDADE")
        print("\n4 - DESTRUIR UNIVERSIDADE")
        print("\n5 - VOLTAR AO MENU PRINCIPAL")
        print("\n6 - SAIR DO PROGRAMA")

        option = int(input("\nEscolha uma das opções: "))

        if option == 1:
            print("\nCadastrando novo departamento...")
            university.create_department()
        elif option == 2:
            print(f"\nConsultando departamentos da Universidade {university.name} ...")
            for i, dep in enumerate(university.departments):
                print(f"\n{i + 1} - {dep.name}")
            index = int(input("\nEscolha um departamento para consultar: ")) - 1
            if index >= 0 and index < len(university.departments):
                dep = university.departments[index]
                dep_menu(dep)
            else:
                print("\nopção inválida, tente novamente.")
        elif option == 3:
            university.consult_university()
        elif option == 4:
            delete_university(university)
            print('Universidade deletada com sucesso!')
            menu()
        elif option == 5:
            menu()
        elif option == 6:
            exit()


def dep_menu(department):
    print("\nPORTAL DO DEPARTAMENTO")
    print("\n------------------------------------")
    department.consult_department()

    while True:

        print("\n1 - CONTRATAR PROFESSOR")
        print("\n2 - DEMITIR PROFESSOR")
        print("\n3 - REMOVER DISICIPLINA DE PROFESSOR")
        print("\n4 - RETIRAR DISCIPLINA DO DEPARTAMENTO")
        print("\n5 - CONSULTAR INFO DESTE DEPARTAMENTO")
        print("\n6 - DESTRUIR DEPARTAMENTO")
        print("\n7 - VOLTAR AO MENU PRINCIPAL")
        print("\n8 - SAIR DO PROGRAMA")

        option = int(input("Escolha uma das opções: "))

        if option == 1:
            print("\nContratando novo professor...")
            if see_professor_list(department) and see_discipline_list():
                professor_index = int(input("\nEscolha um(a) professor para contratar: ")) - 1
                discipline_index = int(input("\nEscolha uma disciplina para o professor: ")) - 1
                department.add_professor(professors[professor_index], disciplines[discipline_index])
            else:
                print("")
        elif option == 2:
            department.delete_professor()
        elif option == 3:
            department.delete_discipline_professor()
        elif option == 4:
            department.delete_discipline()
            print('Disciplina deletada com sucesso!')
        elif option == 5:
            department.consult_department()
        elif option == 6:
            op = input('\nDeseja prosseguir com a destruição do departamento? s/n ')
            if op == 's':
                department.university.delete_department(department)
                print('Departamento deletado com sucesso!')
                menu()
        elif option == 7:
            menu()
        elif option == 8:
            exit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
