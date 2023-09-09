class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def find_route(self, start):
        visited = set()
        route = []

        def dfs(city):
            visited.add(city)
            route.append(city)

            if city in self.graph:
                for neighbor in self.graph[city]:
                    if neighbor not in visited:
                        dfs(neighbor)

        dfs(start)
        return route

def find_sons_route(start, tickets):
    graph = Graph()

    for ticket in tickets:
        u, v = ticket.split('-')
        graph.add_edge(u, v)

    return graph.find_route(start)

# Given train tickets and starting city (Kiev)
tickets = [
    "Paris-Skopje", "Zurich-Amsterdam", "Prague-Zurich",
    "Barcelona-Berlin", "Kiev-Prague", "Skopje-Paris",
    "Amsterdam-Barcelona", "Berlin-Kiev", "Berlin-Amsterdam"
]

start_city = "Kiev"

son_route = find_sons_route(start_city, tickets)
print("Son's Route:", son_route)