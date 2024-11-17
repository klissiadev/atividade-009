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
        if len(unique_elements(self.professors)) <= 5:
            if professor not in self.professors or (professor in self.professors and discipline not in self.disciplines):
                self.professors.append(professor)
                self.disciplines.append(discipline)
                print(f'Professor(a) {professor} contratado para lecionar {discipline} com sucesso!')
                return True
            else:
                print(f'Professor(a) {professor} já leciona está disciplina!')
                return False
        else:
            print('A quantidade de professores por departamento foi atingida.')
            return False

    def delete_professor(self):
        for i, professor in enumerate(self.professors):
            print(f'{i} - {professor}:')
        while True:
            index = int(input('Selecione o professor:'))
            if 0 <= index < len(self.professors):
                print(f'Professor {self.professors[index]} is no longer teaching {self.disciplines[index]}.')
                professor = self.professors[index]
                del self.professors[index]
                del self.disciplines[index]
                if professor not in self.professors:
                    print(f'Professor has been dismissed.')
                return True
            else:
                print('Invalid option.')
