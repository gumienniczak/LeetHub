class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj_list1 = self.buildAdjList(n, edges1)
        adj_list2 = self.buildAdjList(m, edges2)

        diameter1 = self.findDiameter(n, adj_list1)
        diameter2 = self.findDiameter(m, adj_list2)

        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combined_diameter)

    def buildAdjList(self, size, edge_list):
        adj_list = [[] for _ in range(size)]
        for edge in edge_list:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list
        
    def findDiameter(self, size, adjList):
        farthest_node, _ = self.find_farthest_node(size, adjList, 0)
        _, diameter = self.find_farthest_node(size, adjList, farthest_node)
        return diameter

    def find_farthest_node(self, n, adj_list, source_node):
        queue = deque([source_node])
        visited = [False] * n
        visited[source_node] = True
            
        maximum_distance = 0
        farthest_node = source_node

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                farthest_node = current_node

                for neighbour in adj_list[current_node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append(neighbour)

            if queue:
                maximum_distance += 1

        return farthest_node, maximum_distance