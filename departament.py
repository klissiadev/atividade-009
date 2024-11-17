def unique_elements(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    l = unique_list.sort()
    return l

class Department:
    def __init__(self, name, university):
        self.name = name
        self.professors = []
        self.disciplines = []
        self.university = university

    def add_professor(self, professor, discipline):
        if len(self.professors) <= 5:
            if professor not in self.professors or (professor in self.professors and discipline not in self.disciplines):
                self.professors.append(professor)
                professor.department = self
                professor.university = self.university
                #self.disciplines.append(discipline)
                print(f'Professor(a) {professor.name} contratado para lecionar {discipline.name} com sucesso!')
                return True
            else:
                print(f'Professor(a) {professor.name} já leciona está disciplina!')
                return False
        else:
            print('A quantidade de professores por departamento foi atingida.')
            return False

    def add_new_discipline_to_teacher(self, professor, discipline):

        professor.add_discipline(self.university, discipline)
        discipline.add_teacher(self.university, professor)

    def delete_professor(self):
        for i, professor in enumerate(self.professors):
            print(f'{i} - {professor}:')
        while True:
            index = int(input('Selecione o professor(a):'))
            if 0 <= index < len(self.professors):
                print(f'O Professor {self.professors[index]} não leciona mais {self.disciplines[index]}.')
                professor = self.professors[index]
                del self.professors[index]
                del self.disciplines[index]
                if professor not in self.professors:
                    print(f'O professor(a) está demitido.')
                return True
            else:
                print('Opção inválida.')

    def consult_department(self):
        print(f'\nInformações do Departamento: \nNome: {self.name}  \nUniversidade: {self.university} \nProfessores: \n')
        if len(self.professors) > 0:
            for i, professor in enumerate(self.professors):
                print(f'- {professor.name}')
        else:
            print("Este departamento não possui professores ativos.")

