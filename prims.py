# Прима алгоритм O(E * logE) + память для heap O(E)

# используют если полносвязный граф

# Шаги: / (disjointSet.add) == DJS.add
# 1. выбираем случайную вершину в графе (DJS.add)
# 2. в heap добавляем все ребра к НЕ посещенным вершинам графа
# 3. берем минимальное ребро из heap в непосещенную вершину (DJS.add)
# 4. повторяем шаги 2 и 3, пока heap не пустой

# Для минимального островного дерева (Minimal spanning tree)
# применяем disjointSet, чтобы быстро проверять, что вершина
# не принадлежит MST и ее можно добавить в MST

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

  # нужно для корректной работы heap, чтобы он по весу определял min
  def __cmp__(self, other): # перегрузка сравнения объектов по weight
    return self.cmp(self.weight, other.weight)

  # нужно для корректной работы heap, чтобы он по весу определял min
  def __lt__(self, other): # less then / перегрузка знака < по weight
    selfPriority = self.weight
    otherPriority = other.weight

    return selfPriority < otherPriority


class PrimsJarnik(object):

  def __init__(self, unvisitedList):
    self.unvisitedList = unvisitedList # все не посещенные вершины
    self.spanningTree = [] # MST
    self.edgeHeap = [] # heap
    self.fullCost = 0 # sum of all MST edges

  def calculateSpanningTree(self, vertex): # начальная вершина
    self.unvisitedList.remove(vertex) # посетили начальную вершину

    while self.unvisitedList: # пока есть не посещенные вершины
      for edge in vertex.adjacenciesList: # смотрим все ребра vertex
        if edge.targetVertex in self.unvisitedList: # targ не посещена
          heapq.heappush(self.edgeHeap, edge) # in edgeHeap add edge

      minEdge = heapq.heappop(self.edgeHeap) # get min edge

      self.spanningTree.append(minEdge) # add in MST
      print('Edge adding to spanning tree: %s - %s ' % (
        minEdge.startVertex, minEdge.targetVertex
      ))
      self.fullCost += minEdge.weight # sum cost

      vertex = minEdge.targetVertex # set new current Vertex!
      self.unvisitedList.remove(vertex) # remove visited Vertex!

  def getSpanningTree(self):
    return self.spanningTree

# TESTING full connected graph with undirected edges
node1 = Vertex('A')
node2 = Vertex('B')
node3 = Vertex('C')

# A <-> B
edge1 = Edge(100, node1, node2)
edge2 = Edge(100, node2, node1)
# A <-> C
edge3 = Edge(1000, node1, node3)
edge4 = Edge(1000, node3, node1)
# B <-> C
edge5 = Edge(0.01, node3, node2)
edge6 = Edge(0.01, node2, node3)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge6)
node3.adjacenciesList.append(edge4)
node3.adjacenciesList.append(edge5)

unvisitedList = []
unvisitedList.append(node1)
unvisitedList.append(node2)
unvisitedList.append(node3)

algorithm = PrimsJarnik(unvisitedList)
algorithm.calculateSpanningTree(node1) # start searchin from node1 'A'
