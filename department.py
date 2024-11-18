def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return list(set(unique_list))

class Department:
    def __init__(self, name, university):
        self.name = name
        self.professors = []
        self.disciplines = []
        self.university = university

    def add_professor(self, professor, discipline):
        if len(unique_elements(self.professors)) <= 5:
            if professor not in self.professors or (professor in self.professors and discipline not in professor.disciplines):
                if professor.add_discipline(discipline):  # and discipline.add_professor(professor,self.university)
                    self.professors.append(professor)
                    self.disciplines.append(discipline)
                    professor.department = self
                    professor.university = self.university
                    print(f'Professor(a) {professor.name} contratado para lecionar {discipline.name} com sucesso!')
            else:
                print(f'Professor(a) {professor.name} já leciona está disciplina!')
        else:
            print('A quantidade de professores por departamento foi atingida.')


    def delete_professor(self):
        professors = unique_elements(self.professors)
        for i, professor in enumerate(professors):
            print(f'{i+1} - {professor.name}')
        index = int(input('Selecione o professor(a): ')) - 1
        if 0 <= index < len(professors):
            professor = self.professors[index]
            print(f"Removendo o professor(a) {professor.name}...")
            for i in range(len(self.professors) - 1, -1, -1): # runs from last to first
                if self.professors[i].name == professor.name:
                    self.professors[i].delete_discipline(self.disciplines[i])
                    self.disciplines.remove(self.disciplines[i])
                    self.professors.remove(self.professors[i])
            if professor not in self.professors:
                print(f'O professor(a) está demitido.')
            return True
        else:
            print('Opção inválida.')
            return False

    def delete_discipline_professor(self):
        print()
        for i in range(len(self.professors)):
            print(f'{i+1} - {self.professors[i].name} : {self.disciplines[i].name}')
        index = int(input('\nSelecione o(a) professor(a) e a disiplina: ')) - 1
        if 0 <= index < len(self.professors):
            professor = self.professors[index]
            professor.delete_discipline(self.disciplines[index])
            self.disciplines.remove(self.disciplines[index])
            self.professors.remove(self.professors[index])
            if professor not in self.professors:
                print(f'O(a) professor(a) está demitido.')
            return True
        else:
            print('Opção inválida.')
            return False

    def consult_department(self):
        print(f'\nInformações do Departamento: \nNome: {self.name}  \nUniversidade: {self.university.name} \nProfessores: \n')
        if len(self.professors) > 0:
            for i, professor in enumerate(unique_elements(self.professors)):
                print(f'- {professor.name}')
        else:
            print("Este departamento não possui professores ativos.")

    def delete_department(self):
        print(f'\nDeletando o Departamento ... {self.name}')
        for i in range(len(self.professors) - 1, -1, -1):  # runs from last to first
            self.professors[i].delete_discipline(self.disciplines[i])
            #delete_discipline
        self.university.departments.remove(self)
        del self
        return True
