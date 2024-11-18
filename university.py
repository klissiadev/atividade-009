import department as dp

class University:
    def __init__(self, name, type):
        self.name = name
        self.type = type
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

    def consult_university(self):
        print(f'\nUNIVERSIDADE {self.name}')
        print(f'Tipo de universidade: {self.type}')
        if len(self.departments) > 0:
            print(f'\nDepartamentos:')
            for i, dep in enumerate(self.departments):
                print(f"{i+1} - {dep.name}")
        else:
            print(f'\nEsta universidade não possui departamentos ativos.')

    def delete_department(self, department):
        print(f'\nDeletando o Departamento {department.name}...')
        for i in range(len(department.professors) - 1, -1, -1):  # runs from last to first
            department.professors[i].delete_discipline(department.disciplines[i])
            department.disciplines[i].delete_professor(department.professors[i])
        self.departments.remove(department)
        del department
        return True
