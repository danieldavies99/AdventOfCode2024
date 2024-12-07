from dataclasses import dataclass
from enum import Enum

GROUND = "."
OBSTACLE = "#"

GUARD_UP = "^"

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass(unsafe_hash=True, eq=True)
class Coordinate:
    x: int
    y: int

def load_map(input: str) -> list[list[str]]:
    res = []
    for line in input.split("\n"):
        res.append([x for x in line])
    return res

def get_tile_at(coordinate: Coordinate, lab_map: list[list[str]]) -> str:
    if not coordinate_is_within_bounds(coordinate, lab_map):
        return ""
    return lab_map[coordinate.y][coordinate.x]

def find_start_pos(lab_map: list[list[str]]) -> Coordinate:
    for y in range(len(lab_map)):
        for x in range(len(lab_map[0])):
            if get_tile_at(Coordinate(x, y), lab_map) == GUARD_UP:
                return Coordinate(x, y)
    print("COULDN'T FIND GUARD STARTING POSITION")
    return Coordinate(0, 0)

def coordinate_is_within_bounds(coordinate: Coordinate, lab_map: list[list[str]]) -> bool:
    return coordinate.x >= 0 and coordinate.x < len(lab_map[0]) and coordinate.y >= 0 and coordinate.y < len(lab_map)

def get_direction_after_turning(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.LEFT    
    if direction == Direction.LEFT:
        return Direction.UP
    
    print("INVALID DIRECTION SUPPLIED")
    return Direction.UP

def get_next_tile(coordinate: Coordinate, direction: Direction, lab_map: list[list[str]]) -> tuple[Coordinate, Direction]:

    next_tile = OBSTACLE
    while next_tile == OBSTACLE:
        proposed_coordinate = Coordinate(coordinate.x, coordinate.y)
        if direction == Direction.UP:
            proposed_coordinate.y -= 1
        if direction == Direction.DOWN:
            proposed_coordinate.y += 1
        if direction == Direction.LEFT:
            proposed_coordinate.x -= 1
        if direction == Direction.RIGHT:
            proposed_coordinate.x += 1

        next_tile = get_tile_at(Coordinate(proposed_coordinate.x, proposed_coordinate.y), lab_map)
        
        if next_tile == OBSTACLE:
            direction = get_direction_after_turning(direction)
        else:
            return proposed_coordinate, direction
        
    print("COULDN'T FIND NEXT TILE")
    return Coordinate(coordinate.x, coordinate.y), direction
        
        
def solve_part_one(input: str) -> int:
    tiles_visited: list[Coordinate] = []

    lab_map = load_map(input)
    start_pos = find_start_pos(lab_map)

    current_pos: Coordinate = start_pos
    current_direction: Direction = Direction.UP

    while coordinate_is_within_bounds(current_pos, lab_map):
        tiles_visited.append(current_pos)
        current_pos, current_direction = get_next_tile(current_pos, current_direction, lab_map)
        print(current_direction)

    # remove duplicates
    tiles_visited = list(dict.fromkeys(tiles_visited))
    return len(tiles_visited)

txt_input = open("input.txt").read()

print("Part one:", solve_part_one(txt_input))
