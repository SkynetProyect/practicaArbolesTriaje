class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

  def values(self):
    result = [x.value for x in self]
    return result

  def eliminarValor(self, valorID, nodoCabeza):

    if self.head.value.idPaciente == valorID:
      self.head = self.head.next
    elif nodoCabeza.next.value.idPaciente == valorID:
      print("borrado")
      nodoCabeza.next = nodoCabeza.next.next
    else:
      self.eliminarValor(valorID, nodoCabeza.next)

