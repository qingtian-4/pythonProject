import matplotlib.pyplot as plt
import numpy as np
import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance


def a_star(start, goal, grid):
    open_set = []
    closed_set = set()
    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_set, (start_node.f, start_node))

    path = []  # Initialize path
    while open_set:
        current_node = heapq.heappop(open_set)[1]
        closed_set.add(current_node.position)

        # Check if we reached the goal
        if current_node == goal_node:
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 possible directions
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            if (0 <= node_position[0] < grid.shape[0] and
                    0 <= node_position[1] < grid.shape[1] and
                    grid[node_position[0]][node_position[1]] == 0 and
                    node_position not in closed_set):

                neighbor_node = Node(node_position, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(node_position, goal)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if this node is already in the open set with a lower cost
                if all(neighbor_node.f < node[1].f for node in open_set if node[1].position == neighbor_node.position):
                    heapq.heappush(open_set, (neighbor_node.f, neighbor_node))

        # Dynamic display of the search process
        plt.imshow(grid, cmap='gray')

        # Visualizing open set (blue), closed set (red), and the current path (green)
        if open_set:
            plt.scatter(*zip(*[node[1].position for node in open_set]), color='blue')  # Open nodes
        plt.scatter(*zip(*closed_set), color='red')  # Closed nodes
        if path:
            plt.scatter(*zip(*path), color='green')  # Path
        plt.pause(0.1)  # Pause to see the update
        plt.clf()  # Clear figure for the next update

    return path  # Return the final path if found


# Example grid: 0 for free space, 1 for obstacles
grid = np.array([[0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0]])

start = (0, 0)
goal = (4, 4)
path = a_star(start, goal, grid)

# Final display with the found path
plt.imshow(grid, cmap='gray')
if path:
    plt.scatter(*zip(*path), color='green', label='Path')
plt.legend()
plt.show()
