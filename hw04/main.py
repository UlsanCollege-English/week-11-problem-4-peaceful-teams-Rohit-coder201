"""
HW04 — Peaceful Teams (Bipartite Check)

Implement:
- bipartition(graph)
"""

from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.

    Use BFS coloring over all components.

    color: node -> 0 or 1
    """

    color = {}

    # BFS for each component
    for start in graph:
        if start in color:
            continue

        # start this component with color 0
        color[start] = 0
        q = deque([start])

        while q:
            node = q.popleft()
            for nbr in graph.get(node, []):
                if nbr not in color:
                    # give opposite color
                    color[nbr] = 1 - color[node]
                    q.append(nbr)
                else:
                    # conflict → not bipartite
                    if color[nbr] == color[node]:
                        return None

    # build sets
    left = {u for u in color if color[u] == 0}
    right = {u for u in color if color[u] == 1}

    return (left, right)


if __name__ == "__main__":
    # Example graph
    g = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['C']
    }
    print(bipartition(g))   # should show ({'A','C'}, {'B','D'})
