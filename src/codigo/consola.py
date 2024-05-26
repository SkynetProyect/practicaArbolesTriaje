from src.codigo.Paciente import Paciente
from src.codigo.TreeManager import TreeManager


class Consola:
    def __init__(self):
        self.programa = TreeManager()

    def registrar(self):
        print("digite triaje: ")
        triaje = input()
        print("digite id del paciente: ")
        idpaciente = input()
        print("digite nombre del paciente")
        nombre = input()
        print("digite edad")
        edad = input()
        print("digite genero")
        genero = input()
        paciente = Paciente(triaje, idpaciente, nombre, edad, genero)
        self.programa.registrar(paciente)
        print("paciente registrado")
        self.programa.printTree(self.programa.arbolminheap)

    def consultarPacienteProximo(self):
        self.programa.consultarPacienteProximo()
        self.programa.printTree(self.programa.arbolminheap)

    def atenderSiguiente(self):
        self.programa.atenderSiguiente()
        self.programa.printTree(self.programa.arbolminheap)

    def consultarPacientes(self):
        self.programa.consultarPacientes()
        self.programa.printTree(self.programa.arbolminheap)

    def consultarPorTriaje(self,triaje):
        self.programa.consultarPacientesPorTriaje(triaje)
        self.programa.printTree(self.programa.arbolminheap)

    def eliminarPaciente(self,id):
        self.programa.eliminarPaciente(id)
        self.programa.printTree(self.programa.arbolminheap)

    def menu(self):
        print("Iniciando manejador de triajes")
        print("escoja una opcion")
        programa = TreeManager()
        print("1 registrar, 2. consultar proximo paciente 3. atender siguiente ")
        print("4. consultar todos los pacientes 5. consultar por triaje 6. eliminar paciente ")
        opcion = int(input())
        print(f"Escogiste {opcion}")
        if opcion == 1:
            self.registrar()
        if opcion == 2:
            self.consultarPacienteProximo()
        if opcion == 3:
            self.atenderSiguiente()
        if opcion == 4:
            self.consultarPacientes()
        if opcion == 5:
            print("escoja el triaje")
            triaje = input()
            self.consultarPorTriaje(triaje)
        if opcion == 6:
            print("digite id del paciente")
            id = input()
            self.eliminarPaciente(id)
        self.menu()

c = Consola()
c.menu()