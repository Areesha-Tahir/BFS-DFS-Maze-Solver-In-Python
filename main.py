# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque

# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost


#BFS algo for the maze
def bfs(Grid, dest: Grid_Position, start: Grid_Position):
    # to get neighbours of current node
    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)]
                for j in range(n)]
    visited_blocks[start.x][start.y] = True
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)
    cells = 4
    cost = 0
    while queue:
        current_block = queue.popleft()  # Dequeue the front cell
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = BFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return current_block.cost
        #print("current node = ", current_pos.x, current_pos.y)
        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1
        x_pos = current_pos.x
        y_pos = current_pos.y
        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos < 12 and y_pos < 12 and x_pos >= 0 and y_pos >= 0:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        next_cell = Node(Grid_Position(x_pos, y_pos),
                                       current_block.cost + 1)
                        visited_blocks[x_pos][y_pos] = True
                        #print(x_pos,y_pos)
                        queue.append(next_cell)
    return -1

def create_node(x, y, c):
    val = Grid_Position(x, y)
    #print((x, y, c))
    return Node(val, c + 1)

#dfs algo for maze
def dfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)]
               for j in range(n)]
    visited_blocks[start.x][start.y] = True
    #adj_cell_x = [-1, 0, 0, 1]
    #adj_cell_y = [0, -1, 1, 0]
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    neighbours = []
    cost = 0
    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = DFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return current_block.cost
        x_pos = current_pos.x
        y_pos = current_pos.y
        #print("current node = ", x_pos, y_pos, current_block.cost)
        for i in range(neigh):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos != 12 and x_pos != -1 and y_pos != 12 and y_pos != -1:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(create_node(x_pos, y_pos, current_block.cost))
    return -1


def main():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    destination = Grid_Position(10, 0)
    starting_position = Grid_Position(4, 11)
    res = bfs(maze, destination, starting_position)
    if res != -1:
        print("Shortest path steps = ", res)
    else:
        print("Path does not exit")

    print()
    res2 = dfs(maze, destination, starting_position)
    if res2 != -1:
        print("Steps with backtracking = ", res2)
    else:
        print("Path does not exit")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("main start\n")
    main()
