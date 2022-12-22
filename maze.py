from disjoint_set import DisjointSet
from collections import deque
from random import sample


def find_cells(height, length):
    dimensions = height * length
    edges = list()
    for i in range(1, dimensions + 1):
        if (i % length) > 0:
            edges.append((i, i + 1))
        if (i // length) < (height - 1):
            edges.append((i, i + length))
        if ((i % length) == 0) and ((i // length) == (height - 1)):
            edges.append((i, i + length))
    return edges


def generate_maze(height, length, start, end):
    dimensions = height * length
    removed_edges = list()
    cells = find_cells(height, length)
    cells = sample(list(cells), len(cells))
    ds = DisjointSet()
    v = list()
    for i in range(1, dimensions + 1):
        v.append(ds.find(i))
    temp = list()
    for x, y in cells:

        if ds.find(x) != ds.find(y):
            removed_edges.append((x, y))
            ds.union(ds.find(x), ds.find(y))
            if ds.find(start) == ds.find(end):
                break
        else:
            temp.append((x, y))

    return removed_edges


def convert_maze(walls):
    maze = dict()
    for x, y in walls:
        if x not in maze.keys():
            maze[x] = set()
        maze[x].add(y)
        if y not in maze.keys():
            maze[y] = set()
        maze[y].add(x)
    return maze


def bfs(graph, start, end):
    nodes_in_queue = deque()
    nodes_in_queue.append(start)
    visited_nodes = set()
    visited_nodes.add(start)
    prev = {start: None}
    while nodes_in_queue:
        current_node = nodes_in_queue.popleft()
        visited_nodes.add(current_node)
        for node in graph[current_node]:
            if node not in visited_nodes:
                nodes_in_queue.append(node)
                prev[node] = current_node
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path = path[::-1]
    if path[0] == start:
        return path
    return []


def visualize(width=1, height=1, maze={}):
    for i in range(height + 1):
        print('+', end='')
        for j in range(width):
            if ((i - 1, j), (i, j)) in maze or i == 0 or i == height:
                seq = '--'
            else:
                seq = '  '
            if ((i, j), (i, j + 1)) in maze or ((i - 1, j), (i - 1, j + 1)) in maze \
                    or j == width - 1:
                end = '+'
            elif seq == '--' or i == 0 or i == height:
                end = '-'
            else:
                end = ' '
            print(seq, end=end)
        print()
        if i == height:
            break

        for j in range(width):
            if ((i, j - 1), (i, j)) in maze or j == 0 and i != 0:
                seq = '|  '
            else:
                seq = '   '
            print(seq, end='')
        if i != height - 1:
            row_last_wall = '|'
        else:
            row_last_wall = ''
        print(row_last_wall)

    print("\033[%dA" % 2 * (height + 1))
