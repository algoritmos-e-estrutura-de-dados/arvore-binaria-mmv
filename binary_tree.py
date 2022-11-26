from node import Node


class Tree:

  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def add(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      self._add(val, self.root)

  def _add(self, val, node):
    if val < node.v:
      if node.l is not None:
        self._add(val, node.l)
      else:
        node.l = Node(val)
    else:
      if node.r is not None:
        self._add(val, node.r)
      else:
        node.r = Node(val)

  def printTree(self):
    if self.root is not None:
      self._printTree(self.root)

  def _printTree(self, node):
    if node is not None:
      self._printTree(node.l)
      print(str(node.v) + ' ')
      self._printTree(node.r)

  
  def delete(self, v):
    parent = None
    curr = self.root
    while curr is not None:
        if v < curr.v:
            parent = curr
            curr = curr.l
        elif v > curr.v:
            parent = curr
            curr = curr.r
        else:
            break

    if curr is None:
        return False
    if curr.l is None:

        if parent is None:
            self.root = curr.r
        else:
            if v < parent.v:
                 parent.l = curr.r
            else:
                parent.r = curr.r
    elif curr.r is None:
            if parent is None:
                self.root = curr.l
            else:
                if v < parent.v:
                    parent.l = curr.l
                else:
                    parent.r = curr.l
    else:

            parentMaxNode = curr
            maxNode = curr.l
            while maxNode.r is not None:
                parentMaxNode = maxNode
                maxNode = maxNode.r
            curr.v = maxNode.v
            if parentMaxNode.r is maxNode:
                parentMaxNode.r = maxNode.l
            else:
                parentMaxNode.l = maxNode.l
    return True
  
  
  def find(self, val):
    if self.root is not None:
      return self._find(val, self.root)
    else:
      return None

  def _find(self, val, node):
    if val == node.v:
      return node
    elif (val < node.v and node.l is not None):
      return self._find(val, node.l)
    elif (val > node.v and node.r is not None):
      return self._find(val, node.r)
  
  
  #  Nao funciona :(
  # def printTree(self, level=0):
  #     if self.root.v != None:
  #       self.printTree( level + 1)
  #       print(' ' * 4 * level + '-> ' + str(self.root.v))
  #       self.printTree( level + 1)