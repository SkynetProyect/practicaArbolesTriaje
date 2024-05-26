from src.codigo.BSTree import BSTree
from src.codigo.Queue import Queue


class TreeManager:
    def __init__(self, arbolminheap=None):
        self.arbolminheap = arbolminheap


    def printTree(self, Node, prefix="", is_left=True):

        if not Node:
            return

        if Node.rightchild:
            self.printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

        if Node.leftchild:
            self.printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)

    def levelOrderTraversal(self,rootNode, queue: Queue):
        if not rootNode:
            return
        else:
            customqueue = Queue()
            customqueue.enqueue(rootNode)
            while not (customqueue.is_empty()):
                current = customqueue.dequeue()
                queue.enqueue(current.value.data)
                if (current.value.leftchild is not None):
                    customqueue.enqueue(current.value.leftchild)
                if (current.value.rightchild is not None):
                    customqueue.enqueue(current.value.rightchild)
        return queue

    def insertBSTNode(self, rootNode, value):

        if rootNode.data == None:
            rootNode.data = value
        elif value.triaje < rootNode.data.triaje:
            if rootNode.leftchild is None:
                rootNode.leftchild = BSTree(value)

        else:
            if rootNode.rightchild is None:
                rootNode.rightchild = BSTree(value)
            else:
                self.insertBSTNode(rootNode.rightchild, value)

    def insertNode(self, rootNode, value):

        if rootNode.data == None:
            rootNode.data = value
        elif rootNode.leftchild is None:
            rootNode.leftchild = BSTree(value)
        elif rootNode.rightchild is None:
            rootNode.rightchild = BSTree(value)
        else:
            self.insertNode(rootNode.rightchild, value)

    def searchNode(self,rootNode, value):
        if rootNode is None:
            return

        if value < rootNode.data:
            print("ingresa izquierda")
            print(rootNode.data)
            if rootNode.leftchild is not None:
                if rootNode.leftchild.data == value:
                    return "el nodo con valor {} SI fue encontrado".format(value)
                return self.searchNode(rootNode.leftchild, value)
            else:
                return "el nodo con valor {} NO fue encontrado".format(value)
        else:
            print("ingresa derecha")
            print(rootNode.data)
            if rootNode.rightchild is not None:
                if rootNode.rightchild.data == value:
                    return "el nodo con valor {} SI fue encontrado".format(value)
                return self.searchNode(rootNode.rightchild, value)
            else:
                return "el nodo con valor {} NO fue encontrado".format(value)

    def deleteNode(self, rootNode, value):
        if rootNode is None:
            return rootNode

        if value < rootNode.data:
            rootNode.leftchild = self.deleteNode(rootNode.leftchild, value)
        elif value > rootNode.data:
            rootNode.rightchild = self.deleteNode(rootNode.rightchild, value)
        else:
            # caso 1 no tiene hijos
            if rootNode.leftchild is None and rootNode.rightchild is None:
                return None
            # caso 2 tiene ambos hijos
            elif rootNode.leftchild is not None and rootNode.rightchild is not None:
                tempNode = self.minsuccesor(rootNode.rightchild)
                tempData = tempNode.data
                self.deleteNode(rootNode, tempData)
                rootNode.data = tempData
            # caso hijo a la izquierda
            elif rootNode.leftchild is not None:
                return rootNode.leftchild
            # caso hijo a la derecha
            else:
                return rootNode.rightchild

        return rootNode

    def minsuccesor(self, rootNode):
        if rootNode.leftchild is not None:
            return self.minsuccesor(rootNode.leftchild)

        return rootNode


    def inOrderTraversal(self,rootNode, queue:Queue):
        if not rootNode:
            return

        self.inOrderTraversal(rootNode.leftchild, queue)
        queue.enqueue(rootNode)
        self.inOrderTraversal(rootNode.rightchild, queue)
        return queue


    def registrar(self, paciente):
        if self.arbolminheap is not None:
            priorityQueue = self.levelOrderTraversal(self.arbolminheap, Queue())
            priorityQueue.enqueue(paciente)

            bstree = BSTree(priorityQueue.dequeue().value)

            for i in priorityQueue.linkedlist.values():
                self.insertBSTNode(bstree, i)

            priorityQueue = self.inOrderTraversal(bstree, Queue())
            self.arbolminheap = BSTree(priorityQueue.dequeue().value.data)

            for i in priorityQueue.linkedlist.values():
                self.insertNode(self.arbolminheap, i.data)
        else:
            self.arbolminheap = BSTree(paciente)



    def consultarPacienteProximo(self):
        priorityQueue = self.levelOrderTraversal(self.arbolminheap, Queue())
        print(f" EL siguiente en atenderse sera: {priorityQueue.check().nombre} con triaje {priorityQueue.check().triaje}")
        return priorityQueue.check() #retorna el primer paciente

    def consultarPacientes(self):
        priorityQueue = self.levelOrderTraversal(self.arbolminheap, Queue())
        for i in priorityQueue.linkedlist.values():
            print(f"paciente: {i.nombre} con triaje {i.triaje}")

    def consultarPacientesPorTriaje(self, triaje):
        customqueue = Queue()
        priorityQueue = self.levelOrderTraversal(self.arbolminheap, Queue())
        for i in priorityQueue.linkedlist.values():
            if i.triaje == triaje:
                customqueue.enqueue(i)
        print("Pacientes con el triaje buscado: ")
        for i in customqueue.linkedlist.values():
            print(f"paciente {i.nombre} ")

    def eliminarPaciente(self, pacienteID):
        customqueue = Queue()
        priorityQueue = self.levelOrderTraversal(self.arbolminheap, customqueue)
        priorityQueue.linkedlist.eliminarValor(pacienteID, priorityQueue.linkedlist.head)
        if not priorityQueue.is_empty():
            self.arbolminheap = BSTree(priorityQueue.dequeue().value)
            for i in priorityQueue.linkedlist.values():
                self.registrar(i)
        else:
            print("el arbol se ha vaciado")
            self.arbolminheap = None



    def atenderSiguiente(self):
        customqueue = Queue()
        priorityQueue = self.levelOrderTraversal(self.arbolminheap, customqueue)
        atendiendo = priorityQueue.dequeue().value
        print(type(atendiendo))
        self.eliminarPaciente(atendiendo.idPaciente)
        print(f"atendiendo a {atendiendo}")

        return atendiendo


