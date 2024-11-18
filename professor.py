class Professor:
    def __init__(self, name, age, index):
        self.name = name
        self.age = age
        self.index = index
        self.status = 'Disponível'
        self.disciplines = []
        self.department = None
        self.university = None

    def add_discipline(self, discipline):
        if len(self.disciplines) <= 5 and self.status == "Disponível":
            self.disciplines.append(discipline)
            # self.university.append(university)
            if len(self.disciplines) == 5:
                self.status = 'Indisponível'
            return True
        else:
            print("Professor indisponível.")
            return False

    def delete_discipline(self, disc):
        if disc in self.disciplines:
            self.disciplines.remove(disc)
            print(f"O(a) Professor(a) {self.name} não leciona mais a disciplina {disc.name}.")
            if len(self.disciplines) < 5:
                self.status = 'Disponível'
                if len(self.disciplines) == 0:
                    self.university = None
                    self.department = None

    def consult_professor(self):
        uni = self.university.name if self.university else "Não está contratado(a) no momento"
        dep = self.department.name if self.department else "Não está contratado(a) no momento"

        print(
            f'\nInformações do Professor: \n   Nome: {self.name}\n   Status: {self.status}\n   Departamento: {dep}'
            f'\n   Universidade: {uni}\n   Disciplinas ministradas:')
        if self.disciplines:
            for discipline in self.disciplines:
                print(f'      {discipline.name}')
        else:
            print("      Nenhuma disciplina atribuída.")
