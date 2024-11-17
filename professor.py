class Professor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = 'Disponível'
        self.discipline = []
        self.university = []

    def add_discipline(self, discipline, university):
        if len(self.discipline) <= 5:
            self.discipline.append(discipline)
            self.university.append(university)
            if len(self.discipline) == 5:
                self.status = 'Indisponível'
            print(f'Professor {self.name} contratado para lecionar a disciplina {discipline} com sucesso.')
            return True
        else:
            print("Professor indisponível.")
            return False

    def consult_teacher(self):
        print(f'\nInformações: \n   Professor(a): {self.name}\n   Idade: {self.age}\n   Status: {self.status}\n   Disciplinas ministradas:')
        for i, discipline in enumerate(self.discipline):
            print(f'    {discipline} - {self.university[i]}')