class Discipline:
    def __init__(self, name):
        self.name = name
        self.professors = []
        self.status = 'Disponível'

    def add_professor(self, professor):
        if len(self.professors) <= 5:
            self.professors.append(professor)
            if len(self.professors) == 5:
                self.status = 'Indisponível'
            print(
                f'A disciplina {self.name} será lecionada pelo(a) professor(a) "{professor.name}" na universidade {professor.university.name} com sucesso.')
            return True
        else:
            print('Limite de professores atingido.')
            return False

    def consult_discipline(self):
        print(f'\n  Disciplina: {self.name}\n  Status: {self.status}\n  Disciplina ministrada por:')
        for professor in self.professors:
            print(f'   - {professor.name} : {professor.university.name}')

    def delete_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
            if len(self.professors) < 5:
                self.status = 'Disponível'
                if len(self.professors) == 0:
                    print('Essa matéria foi removida da universidade.')
