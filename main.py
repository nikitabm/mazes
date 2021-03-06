import random


class Cell:
    x = y = 0
    symbol = " "
    walls = []
    visited = False

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.walls = [0, 0, 0, 0]


class Cell_Data:
    cell = None
    neighs = []


class Map:
    cells = []
    size_x = 0
    size_y = 0

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        for y in range(size_y):
            for x in range(size_x):
                self.cells.append(Cell(x, y))

    def draw(self):
        cell_line = ""

        for y in range(self.size_y):
            hor_wall = ""
            temp_cell_line = ""
            for x in range(self.size_x):
                cell = self.cells[y*self.size_y+x]
                previous_cell = None
                above_cell = None
                if x > 0:
                    previous_cell = self.cells[y*self.size_y+x-1]
                if y > 0:
                    above_cell = self.cells[(y-1)*self.size_y+x]
                hor_wall += "+"
                cell_vert_wall = " "
                cell_hor_wall = " "
                hor_wall += "-" if cell.walls[1] == 1 or (
                    above_cell != None and above_cell.walls[3] == 1) else " "
                cell_vert_wall = "|" if cell.walls[0] == 1 or (
                    previous_cell != None and previous_cell.walls[2] == 1) else " "

                temp_cell_line += cell_vert_wall+cell.symbol
            hor_wall += "+\n"
            cell_line += hor_wall+temp_cell_line+"\n"

        print(cell_line)


def depth_first_search(map):
    # random cell to start with
    start_cell_x = random.randrange(0, map.size_y)
    start_cell_y = random.randrange(0, map.size_x)

    visited_cells = []
    cells_data = []

    def mark_cell(x, y):
        cell_index = y*(map.size_y)+x
        cell = map.cells[cell_index]
        cell.symbol = "*"
        cell.walls = [1, 1, 1, 1]
        visited_cells.append(cell_index)

        cell_data = Cell_Data()
        cell_data.cell = cell
        cell_data.neighs = []
        if x > 0:
            if not y*map.size_y+x-1 in visited_cells:
                cell_data.neighs.append(map.cells[y*map.size_y+x-1])
            else:
                map.cells[cell_index].walls[1] = 1
                map.cells[cell_index].walls[3] = 1
        if y > 0:
            if not (y-1)*map.size_y+x in visited_cells:
                cell_data.neighs.append(map.cells[(y-1)*map.size_y+x])
            else:
                map.cells[cell_index].walls[0] = 1
                map.cells[cell_index].walls[2] = 1
        if x < map.size_x-1:
            if not y*map.size_y+x+1 in visited_cells:
                cell_data.neighs.append(map.cells[y*map.size_y+x+1])
            else:
                map.cells[cell_index].walls[1] = 1
                map.cells[cell_index].walls[3] = 1
        if y < map.size_x-1:
            if not (y+1)*map.size_y+x in visited_cells:
                cell_data.neighs.append(map.cells[(y+1)*map.size_y+x])
            else:
                map.cells[cell_index].walls[3] = 1

        cells_data.append(cell_data)
        return cell_data

    def remove_wall(cell_a, cell_b):
        if cell_a.x > cell_b.x and cell_a.y == cell_b.y:
            cell_a.walls[0] = 0
            cell_b.walls[2] = 0
        if cell_a.x < cell_b.x and cell_a.y == cell_b.y:
            cell_a.walls[2] = 0
            cell_b.walls[0] = 0
        if cell_a.x == cell_b.x and cell_a.y > cell_b.y:
            cell_a.walls[1] = 0
            cell_b.walls[3] = 0
        if cell_a.x == cell_b.x and cell_a.y < cell_b.y:
            cell_a.walls[3] = 0
            cell_b.walls[1] = 0

    def depth_first(cell_data):
        visited_cells.append(cell_data.cell)
        while len(cell_data.neighs) > 0:
            next_cell = cell_data.neighs.pop(
                random.randrange(0, len(cell_data.neighs), 1))
            if next_cell not in visited_cells:
                data = mark_cell(next_cell.x, next_cell.y)
                remove_wall(cell_data.cell, next_cell)
                depth_first(data)

    depth_first(mark_cell(start_cell_x, start_cell_y))


def Start():
    map_size_x = 5
    map_size_y = 5
    map = Map(map_size_x, map_size_y)

    # algorithm
    depth_first_search(map)
    map.draw()


Start()
