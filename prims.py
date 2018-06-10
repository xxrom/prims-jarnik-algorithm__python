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

  def __cmp__(self, other): # перегрузка сравнения объектов по weight
    return self.cmp(self.weight, other.weight)

  def __lt__(self, other): # less then / перегрузка знака < по weight
    selfPriority = self.weight
    otherPriority = self.weight

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


