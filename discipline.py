class Discipline:
    def __init__(self, name):
        self.name = name
        self.professors = []
        self.university = []

    def add_teacher(self, teacher):
        if len(self.professors) <= 5:
            self.professors.append(teacher)
            return True
        else:
            print('Limite de professores atingido.')
            return False

    def consult_discipline(self):
        print(f'\nInformações: \n   Disciplina: {self.name}\n   Disciplina ministrada por:')
        for professor in self.professors:
            print(f'    {professor}')