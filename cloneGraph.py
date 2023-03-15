# LeetCode #133 - Clone Graph
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Explanation: Use Depth First Search to make copy of the previous graph. 
# Then do a recursive call using DFS to connect each node in the graph's neighbors. 
# Only do it if the node given is not empty. 
class Solution(object):
    def cloneGraph(self, node):

        oldToNew = {}

        def dfs(node): 
            if node in oldToNew: 
                return oldToNew[node] 
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors: 
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node) if node else None