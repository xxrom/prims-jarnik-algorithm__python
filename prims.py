import heapq

class Vertex(object):

  def __init__(self, name):
    self.name = name
    self.visited = False
    self.predecessor = None
    self.adjacenciesList = []

  def __str__(self): # перегрузка print.out ???
    return self.name

class Edge(object):

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

  def __cmp__(self, other): # перегрузка сравнения объектов по weight
    return self.cmp(self.weight, other.weight)

  def __lt__(self, other): # less then / перегрузка знака < по weight
    selfPriority = self.weight
    otherPriority = self.weight

    return selfPriority < otherPriority

