from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('G', 2)],
    'C': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'G': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))

    g_cost = {start: 0}

    while not pq.empty():
        f, node = pq.get()

        if node == goal:
            print("Goal Found")
            return

        print("Visited:", node)

        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                pq.put((f_cost, neighbor))

astar('A', 'G')