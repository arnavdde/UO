"""Simple grid model of contagion"""

import mvc # for Listenable
import enum
from typing import List, Tuple
import random

class Health(enum.Enum):
    """Each individual is one discrete state of health"""
    vulnerable = enum.auto()
    asymptomatic = enum.auto()
    symptomatic = enum.auto()
    recovered = enum.auto()
    dead = enum.auto()

    def __str__(self) -> str:
        return self.name


class Individual(mvc.Listenable):
    def __init__(self):
        super().__init__()
        self.state = Health.vulnerable
        self.next_state = None
    
    def step(self):
        pass #FIXME

    def tick(self):
        """time passes"""
        self.state = self.next_state
    
    def infect(self):
        """called by a germ spreading individual, or to patient 0 to start sim"""
        if self.state == Health.vulnerable:
            self.next_state = Health.asymptomatic


class Population(mvc.Listenable):
    def __init__(self, nrows: int, ncols: int):
        super().__init__()
        self.cells = []
        self.nrows = nrows
        self.ncols = ncols
        for row in range(nrows):
            rcells = []
            for col in range(ncols):
                rcells.append(Individual())
            self.cells.append(rcells)
    
    def seed(self):
        """patient 0"""
        row = random.randint(0, self.nrows-1)
        col = random.randint(0, self.ncols-1)
        self.cells[row][col].infect()
        self.cells[row][col].tick()

    def step(self):
        """determine next states"""
        for row in self.cells:
            for cell in row:
                cell.step()
        for row in self.cells:
            for cell in row:
                cell.tick()
        self.notify_all("timestep")

    def count_in_state(self, state: Health) -> int:
        """how man individuals in the passed in state"""
        count = 0
        for row in self.cells:
            for cell in row:
                if cell.state == state:
                    count += 1
        return count
    
    

        """Simple grid model of contagion"""

import mvc # for Listenable
import enum
from typing import List, Tuple
import random

class Health(enum.Enum):
    """Each individual is one discrete state of health"""
    vulnerable = enum.auto()
    asymptomatic = enum.auto()
    symptomatic = enum.auto()
    recovered = enum.auto()
    dead = enum.auto()

    def __str__(self) -> str:
        return self.name


class Individual(mvc.Listenable):
    """An individual in the population, e.g., a person who might get and spread disease. 
    The 'state' instance variable is public read-only, e.g., listeners can check it"""
    
    def __init__(self, kind: str, region: Population, row: int, col: int):
        # Listener needs its own initialization
        super().__init__()
        self.next_state = None
        self.kind = kind
        self.region = region
        self.row = row
        self.col = col
        # Initially, an Individual is 'vulnerable', not yet infected
        self._time_in_state = 0 # How long in this state?
        self.state = Health.vulnerable
        self.next_state = Health.vulnerable
        # Configuration parameters based on kind
        self.T_Incubate = config.get_int(kind, "T_Incubate")
        self.P_Transmit = config.get_float(kind, "P_Transmit")
        self.T_Recover = config.get_int(kind, "T_Recover")
        self.P_Death = config.get_float(kind, "P_Death")
        self.P_Greet = config.get_float(kind, "P_Greet")
        self.N_Neighbors = config.get_int(kind, "N_Neighbors")
        self.P_Visit = config.get_float(kind, "P_Visit")
        self.Visit_Dist = config.get_int(kind, "Visit_Dist")
        
    
    def step(self):
        pass #FIXME

    def tick(self):
        """time passes"""
        self.state = self.next_state
    
    def infect(self):
        """called by a germ spreading individual, or to patient 0 to start sim"""
        if self.state == Health.vulnerable:
            self.next_state = Health.asymptomatic

class Typical(Individual):
    """Typical individual. May visit different neighbors each day."""
    def __init__(self, region: Population, row: int, col: int):
        # Much of the constructor has been "factored out" into the abstract base class
        super().__init__("Typical", region, row, col)



class Population(mvc.Listenable):
    def __init__(self, nrows: int, ncols: int):
        super().__init__()
        self.cells = []
        self.nrows = nrows
        self.ncols = ncols
        for row in range(nrows):
            rcells = []
            for col in range(ncols):
                rcells.append(Individual())
            self.cells.append(rcells)
    
    def seed(self):
        """patient 0"""
        row = random.randint(0, self.nrows-1)
        col = random.randint(0, self.ncols-1)
        self.cells[row][col].infect()
        self.cells[row][col].tick()

    def step(self):
        """determine next states"""
        for row in self.cells:
            for cell in row:
                cell.step()
        for row in self.cells:
            for cell in row:
                cell.tick()
        self.notify_all("timestep")

    def count_in_state(self, state: Health) -> int:
        """how man individuals in the passed in state"""
        count = 0
        for row in self.cells:
            for cell in row:
                if cell.state == state:
                    count += 1
        return count
    
    

        