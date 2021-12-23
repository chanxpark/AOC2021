from collections import namedtuple
from dataclasses import dataclass
from typing import List

@dataclass
class Map: 
    rows: List[List[int]]
    col_size: int
    row_size: int

point = namedtuple('point', ['col', 'row'])
line = namedtuple('line', ['start', 'end'])


def printMap(map: Map) -> None: 
    for row in map.rows: 
        for col in row: 
            print(col, end="")
        print("")

def drawLine(line: line, map: Map) -> Map: 
    line_type: str = "diagnol"
    if line.start[0] == line.end[0]: 
        line_type = "horizontal"
    elif line.start[1] == line.end[1]: 
        line_type = "vertical"

    first_found: bool = False 
    point_to_mark = line.start
    for i in range(map.row_size): 
        for j in range(map.col_size): 
            # find first 
            if point(j, i) == line.start: 
                first_found = True 
            if first_found and point(j, i) == point_to_mark: 
                map.rows[i][j] += 1 
                if line_type == "horizontal": 
                    point_to_mark = point(j, i+1)
                elif line_type == "vertical": 
                    point_to_mark = point(j+1, i)
                else: 
                    col_increment = 1 if line.end[0] >= line.start[0] else -1
                    row_increment = 1 if line.end[1] >= line.start[1] else -1
                    point_to_mark = point(j+col_increment, i+row_increment)
            # print until last found 
            if point(j, i) == line.end: 
                return map
            # break if last found 
    return map

def intersections(map: Map) -> int: 
    results = 0
    for row in map.rows: 
        for col in row: 
            if col >= 2: 
                results += 1 

    return results

def drawMap(coordinates: List[line], col_size: int, row_size: int) -> Map: 
    map: Map = Map([ [0] * col_size for _ in range(row_size) ], col_size, row_size)
    # map: Map = [ [0] * size ] * size
    counter = 0
    for c in coordinates: 
        counter += 1 
        print(counter)
        map = drawLine(c, map)

    return map

if __name__ == "__main__": 
    f = "input.txt"
    # read lines 
    with open(f, "r") as input: 
        stdin_lines: List[str] = input.read().strip().split("\n")

    coordinates: List[line] = []
    row_max = 0 
    col_max = 0 
    for stdin_line in stdin_lines: 
        l = stdin_line.strip().split(" -> ")
        c1 = l[0].strip().split(",")
        c2 = l[1].strip().split(",")
        p1 = point(int(c1[0]), int(c1[1]))
        p2 = point(int(c2[0]), int(c2[1]))
        col_max = max(p1[0], p2[0], col_max)
        row_max = max(p1[0], p2[0], row_max)
        if sum(p1) == sum(p2): 
            if p1.row <= p2.row: 
                coordinates.append(line(p1, p2))
            else: 
                coordinates.append(line(p2, p1))
        elif sum(p1) < sum(p2): 
            coordinates.append(line(p1, p2))
        else: 
            coordinates.append(line(p2, p1))

    result = drawMap(coordinates, col_max+1, row_max+1)
    # printMap(result)
    print("Result:", intersections(result))