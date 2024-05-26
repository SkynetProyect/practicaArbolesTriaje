class Paciente:
    def __init__(self, triaje, idpaciente, nombre, edad, genero):
        self.triaje= triaje
        self.idPaciente = idpaciente
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


    def __str__(self):
        return f"Paciente {self.nombre} id {self.idPaciente} triaje {self.triaje}"