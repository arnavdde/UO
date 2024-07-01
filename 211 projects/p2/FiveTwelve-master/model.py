"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixme:  We need a constructor, and __add__ method, and __eq__.
    def __init__(self, x, y) -> None:
        # assert x <= 4 and x >= 0 and y <= 4 and y>= 0, f"row or column out of bounds"
        self.x = x
        self.y = y

    def __add__(self, other:"Vec") -> "Vec":
        return Vec(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other:"Vec") -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False





class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self, pos: Vec, value: int):
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self. value = value

        def move_to(self, new:Vec):
            self.pos = new.pos
            self.notify_all(GameEvent(EventKind.tile_updated, self))


class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = [ ]
        for row in range(rows):
            row_tiles = [ ]
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)
    
    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]

    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

    def _empty_positions(self) -> list[Vec]:
        empties = []
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles)):
                if self.tiles[row][col] is None:
                    empties.append(Vec(row, col))
        return empties

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        if len(self._empty_positions()) > 0:
            return True
        return False
    

    def place_tile(self, value=2):
        """Place a tile on a randomly chosen empty square."""
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = random.choice(empties)
        row, col = choice.x, choice.y
        if value is None:
            value = 4 if random.random() < 0.1 else 2

        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = [ ]
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result
    
    def from_list(self, in_list: List[List[int]]):
        """using an input list, form a board, one tile per row/col value"""
        for row in range(self.rows):
            for col in range(self.cols):
                if in_list[row][col] == 0:
                    self.tiles[row][col] = None
                else:
                    value = in_list[row][col]
                    self.tiles[row][col] = Tile(Vec(row, col), value)
                    self.notify_all(GameEvent(EventKind.tile_created, self.tiles[row][col]))
    
    def in_bounds(self, pos: Vec) -> bool:
        if 0 <= pos.x < self.rows and 0 <= pos.y < self.cols:
            return True
        return False 
    
    def slide(self, pos: Vec,  dir: Vec):
        """Slide tile at row,col (if any)
        in direction (dx,dy) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos

        self.notify_all(GameEvent(EventKind.tile_merged, next))




    def _move_tile(self, old_pos: Vec, new_pos:Vec):
        temp = Vec(old_pos.x, old_pos.y)
        break

    def merge(self, pos:Vec, other:Vec):
        



    def left(self):
        """slide all tiles left"""


    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        final = 0
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    final += tile.value
        return final
        #FIXME
    

    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]:{self.value}"
    
    def __str__(self) -> str:
        return str(self.value)


