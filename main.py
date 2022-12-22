import random
from random import sample
import sys
from maze import (find_cells, generate_maze, convert_maze, visualize, bfs)


def convert_coords(num):
    return num // width, num % width


height = int(sys.argv[1])
width = int(sys.argv[2])
start = 1
end = height * width
counter = 0

cells = find_cells(height, width)

removed_edges = generate_maze(height, width, start, end)

maze = convert_maze(removed_edges)

result = set(cells) - set(removed_edges)

bfs_result = bfs(maze, start, end)

maze_set = set()

print("*** Initial Labyrinth ***\n")
visualize(width, height, maze_set)
print("\033[%dB" % (2 * height))

for x, y in sorted(result):
    x -= 1
    y -= 1
    counter += 1
    maze_set.add((convert_coords(x), convert_coords(y)))
    if counter == len(result):
        print("*** Final Labyrinth ***\n")
        print('\n')
        visualize(width, height, maze_set)
        print("\033[%dB" % (2 * height))
print('\n')
print("*** Path to solution using bfs ***\n")
print(*bfs_result, sep=' --> ')
