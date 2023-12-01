class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def insert_node(self, node):
        # check if node already exists
        if node in self.adjacent_list:
            print('node already exists')
            return
        else:
            self.adjacent_list.update({node: []})
            self.number_of_nodes += 1

    def insert_edge(self, vertex_1, vertex_2):
        if vertex_2 not in self.adjacent_list[vertex_1]:
            self.adjacent_list[vertex_1].append(vertex_2)
            self.adjacent_list[vertex_2].append(vertex_1)

    def show_connections(self):
        for node in self.adjacent_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacent_list[node]))}')


my_graph = Graph()
my_graph.insert_node(0)
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_node(4)
my_graph.insert_node(5)
my_graph.insert_node(6)
my_graph.insert_edge(3, 1)
my_graph.insert_edge(3, 4)
my_graph.insert_edge(4, 2)
my_graph.insert_edge(4, 5)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(1, 0)
my_graph.insert_edge(0, 2)
my_graph.insert_edge(6, 5)
