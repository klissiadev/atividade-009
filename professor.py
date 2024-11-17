class Professor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = 'Disponível'
        self.discipline = []
        self.department = None
        self.university = None

    def add_discipline(self, discipline):
        if len(self.discipline) <= 5:
            self.discipline.append(discipline)
            # self.university.append(university)
            if len(self.discipline) == 5:
                self.status = 'Indisponível'
            print(f'Professor {self.name} contratado para lecionar a disciplina {discipline} com sucesso.')
            return True
        else:
            print("Professor indisponível.")
            return False

    def consult_professor(self):

        if self.university == None:
            uni = "Não está contratado(a) no momento"
            dep = "Não está contratado(a) no momento"
        else:
            uni = self.university.name
            dep = self.department.name

        print(f'\nInformações do Professor: \n   Nome: {self.name}\n   Status: {self.status}\n   Departamento:{uni} - {dep}\n   Disciplinas ministradas:')
        for university, disciplines in self.discipline:
            print(f'   {university.name}:')
            for discipline in disciplines:
                print(f'      {discipline}')