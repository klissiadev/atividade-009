import departament as dp

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def create_department(self):
        name = input('Nome do departamento: ')
        exist = False
        for i in range(len(self.departments)):
            if name == self.departments[i].name:
                exist = True
        if not exist:
            department = dp.Department(name, self)
            self.departments.append(department)
            print(f'Departamento {name} cadastrado com sucesso!')
        else:
            print('Este departamento já existe!')

    def consult_universiy(self):
        print(f'\nUNIVERSIDADE {self.name}')

        if len(self.departments) > 0:
            print(f'\nDepartamentos:')
            for i, dep in enumerate(self.departments):
                print(f"{i+1} - {dep.name}")
        else:
            print(f'\nEsta universidade não possui departamentos ativos.')
