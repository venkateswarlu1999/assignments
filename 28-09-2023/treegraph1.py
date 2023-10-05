# from collections import deque

# def bfs(graph, start):
#     visited_places = set()
#     placesToVisitQueue = deque([start])
#     while placesToVisitQueue:
#         place = placesToVisitQueue.popleft()
#         if place not in visited_places:
#             visited_places.add(place)
#             print(place)
#             placesToVisitQueue.extend(graph[place]-visited_places)

# graph = {}
# noOfEdges = int(input("please enter the number of edges you need : "))

# for i in range(noOfEdges):
#     print("enter the place1 and place2:\n")
#     val1, val2 = input().split()

#     if val1 not in graph:
#         graph[val1] = set()
#     if val2 not in graph:
#         graph[val2] = set()

#     graph[val1].add(val2)
#     graph[val2].add(val1)

# print("enter the start value")
# start = input()
# bfs(graph, start) 

from collections import deque
def bsf(graph,start):
    visitedplaces=set()
    placestovisit=deque([start])
    while placestovisit:
        place=placestovisit.popleft()
        if place not in visitedplaces:
            visitedplaces.add(place)
            print(place)
            placestovisit.extend(graph[place]-visitedplaces)
        
        
graph={}
noofnodes=int(input("how many nodes you want"))
for i in range(noofnodes):
    print("enter your places1 and place2:\n")
    val1,val2 = input().split()
    if val1 not in graph:
        graph[val1]= set()
    if val2  not in graph:
        graph[val2] =set()
    graph[val1].add(val2)
    graph[val2].add(val1)
print("enter the start value: ")
start=input()
bsf(graph,start)

