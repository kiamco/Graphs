"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
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
                print(current_vertex)
                path.append(current_vertex)
                visited.add(current_vertex)
                edges = self.get_neighbors(current_vertex)

                for edge in edges:
                    queue.enqueue(edge)

        return path


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # init stack
        path = []
        stack = Stack()

        # push starting to stack
        stack.push(starting_vertex)

        # set with visited nodes
        visited = set()

        # iterate through stack
        while stack.size() > 0:
            current_vertex =  stack.pop()

            if current_vertex not in visited:
                path.append(current_vertex)
                print(current_vertex)
                visited.add(current_vertex)
                edges = self.get_neighbors(current_vertex)

                for edges in edges:
                    stack.push(edges)
        
        return path


    def dft_recursive(self, starting_vertex,visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)
        edges = self.get_neighbors(starting_vertex)

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge,visited)


        


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make queu
        queue = Queue()

        # make visited
        visited = set()

        path = [starting_vertex]

        queue.enqueue(path)
    
        while queue.size() > 0:
            #dequeue
            current_path = queue.dequeue()
            current_node = current_path[-1]
            # if destionation == current_node return true
            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                print(current_path)
                visited.add(current_node)
                edges = self.get_neighbors(current_node)

                for edge in edges:
                    path_copy = current_path[:]
                    path_copy.append(edge)
                    queue.enqueue(path_copy)

        


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO

        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            current_node = path[-1]
            
            if current_node not in visited:
                if current_node == destination_vertex:
                    return path
                
                visited.add(current_node)

                edges = self.get_neighbors(current_node)

                for edge in edges:
                    new_path = path[:]
                    new_path.append(edge)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO

        # add to path
        path = [starting_vertex]
        print(path)
        if visited is None:
            visited = set()
        # mark node as visited
        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)

        #iterate over the neightbors
        edges = self.get_neighbors(starting_vertex)

        for edge in edges:
            if edge not in visited:
                new_path = path + [edge]
                path_result = self.dfs_recursive(edge, destination_vertex, visited, new_path)

                if path_result is not None:
                    print(path_result)
                    return path_result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
    # graph.dft_recursive(1)