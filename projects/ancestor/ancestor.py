
class Graph:
    def __init__(self):
        self.vertices = {}
        self.len = 0

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add new vertex in vertices
        self.vertices[vertex_id] = set()

        # increment len
        self.len += 1


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO

        # add directed edges
        self.vertices[v1].add(v2)
        # self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO

        # mark all vertices as not visited 
        visited = set()

        #create a queue
        queue = Queue()

        path = []

        #add starting vertex to the queueu
        queue.enqueue(starting_vertex)

        while len(queue.queue) > 0:
            # remove pop a vertex from the queue

            current_vertex = queue.dequeue()
            if current_vertex not in visited:           
                path.append(current_vertex)
                visited.add(current_vertex)
                edges = self.get_neighbors(current_vertex)

                for edge in edges:
                    queue.enqueue(edge)

        return path

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):

    ## problem: return earliest ancestor, (the farthest parent of the node)

    ## given : an array of tuples

    ## solution: use graph bfs the last node should be the earliest ancestor

    # step 1: init graph

    graph = Graph()

    # step 2: iterate over ancestors and add to graph

    ### add vertices 
    for node in ancestors:

        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
     
    ### add edges
    for node in ancestors:
        ## direction is child to parent
        graph.add_edge(node[1], node[0])    

        
    # step 3: implement bfs to find the earliest ancestor the last node in
    # the path is the latest ancestor

    early_ancestor = graph.bft(starting_node)

    if len(graph.vertices[starting_node]) == 0:
        return -1

    if early_ancestor is not None:
        return early_ancestor[-1]


    