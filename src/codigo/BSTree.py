class BSTree:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None

  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"

    if self.leftchild:
      ret += self.leftchild.__str__(level+1)

    if self.rightchild:
      ret += self.rightchild.__str__(level+1)

    return ret
