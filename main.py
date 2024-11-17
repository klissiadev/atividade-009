import university as university
from university import University
from professor import Professor
from discipline import  Discipline

#arrays
professors = []
disciplines = []
universities = []

def see_professor_list():
    global professors

    print("Professores: ")
    if len(professors) > 0:
        for i, professor in enumerate(professors):
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
    professor = Professor(name, age)

    professors.append(professor)

def create_university(name):
    global universities
    university = University(name)

    universities.append(university)

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
            create_university(name)
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
            create_professor(name, age)
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

            index = int(input("\nEscolha uma discipline para consultar: ")) - 1

            if index >= 0 and index < len(disciplines):
                print("\nConsultando Professor:\n")

                discipline = disciplines[index]
                discipline.consult_discipline()
        elif option == 7:
            exit()
        else:
            print("\nopção invalida, tente novamente\n")


def uni_menu(university):
    print("\nPORTAL DA UNIVERSIDADE")
    print("\n------------------------------------")
    university.consult_universiy()

    while True:

        print("\n1 - CADASTRAR DEPARTMANENTO")
        print("\n2 - CONSULTAR DEPARTAMENTOS")
        print("\n3 - CONSULTAR INFO DESTA UNIVERSIDADE")
        print("\n4 - VOLTAR AO MENU PRINCIPAL")
        print("\n5 - SAIR DO PROGRAMA")

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
            university.consult_universiy()
        elif option == 4:
            menu()
        elif option == 5:
            exit()


def dep_menu(department):
    print("\nPORTAL DO DEPARTAMENTO")
    print("\n------------------------------------")
    department.consult_department()

    while True:

        print("\n1 - CONTRATAR PROFESSOR")
        print("\n2 - ADICIONAR NOVA DISCIPLINA A PROFESSOR")
        print("\n3 - ADICIONAR NOVA DISCIPLINA")
        print("\n4 - CONSULTAR INFO DESTE DEPARTAMENTO")
        print("\n5 - VOLTAR AO MENU PRINCIPAL")
        print("\n6 - SAIR DO PROGRAMA")

        option = int(input("Escolha uma das opções: "))

        if option == 1:
            print("\nContratando novo professor...")
            if see_professor_list() and see_discipline_list():
                professor_index = int(input("\nEscolha um(a) professor para contratar: ")) - 1
                new_professor = professors[professor_index]
                discipline_index = int(input("\nEscolha uma disciplina para o professor: ")) - 1
                new_discipline = disciplines[discipline_index]

                department.add_professor(new_professor, new_discipline)
            else:
                print("")
        elif option == 2:
            print("\nConsultando departamentos...")
            for i, dep in enumerate(university.departments):
                print(f"\n{i + 1} - {dep.name}")
            index = int(input("\nEscolha uma universidade para consultar: ")) - 1

            if index >= 0 and index < len(university.departments):
                print("\nCONSULTANDO DEPARTAMENTOS:")
            else:
                print("\nopção inválida, tente novamente.")

        elif option == 3:
            print("\nadicionar disciplina")
        elif option == 4:
            department.consult_department()
        elif option == 5:
            menu()
        elif option == 6:
            exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
