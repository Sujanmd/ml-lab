from queue import PriorityQueue 
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':[],
    'G':[]
}
heaur={
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 4,
    'G': 0
}
def bfs(start,goal):
    pq=PriorityQueue()
    pq.put((heaur[start],start))
    vis=[]
    while not pq.empty():
        h, node=pq.get()
        if node not in vis:
            print(node,end=" ")
            vis.append(node)
        if node==goal:
            print("\nGoal reached")
            return
        for neighbour in graph[node]:
            if neighbour not in vis:
                pq.put((heaur[neighbour],neighbour))
bfs('A','G')

