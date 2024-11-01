import mvc  # for Listenable
import enum
import config 
import random
from typing import List, Tuple

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

    def __init__(self, kind: str, region: "Population", row: int, col: int):
        # Listener needs its own initialization
        super().__init__()
        self.kind = kind
        self.region = region
        self.row = row
        self.col = col
        # Initially we are 'vulnerable', not yet infected
        self._time_in_state = 0  # How long in this state?
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
        self.neighbors = region.neighbors(num=self.N_Neighbors, row=row, col=col, dist=self.Visit_Dist)

    def step(self):
        """Next state"""
        # Basic state transitions are in common
        if self.state == Health.asymptomatic:
            if self._time_in_state > self.T_Incubate:
                self.next_state = Health.symptomatic
        if self.state == Health.symptomatic:
            # We could die on any time step before we recover
            if self._time_in_state > self.T_Recover:
                self.next_state = Health.recovered
            elif random.random() < self.P_Death:
                self.next_state = Health.dead

        # Social behavior differs among concrete classes
        self.social_behavior()
    
    def social_behavior(self):
        raise NotImplementedError("Social behavior should be implemented in subclasses")


    def tick(self):
        """time passes"""
        self._time_in_state += 1
        if self.state != self.next_state:
            self.state = self.next_state
            self.notify_all("newstate")
            # Reset clock
            self._time_in_state = 0

    
    def meet(self, other: "Individual"):
        """Two individuals meet.  Either may infect the other."""
        self.maybe_transmit(other)  
        other.maybe_transmit(self)  


    def maybe_transmit(self, other: "Individual"):
        if not self._is_contagious():
            return
        if not other.state == Health.vulnerable:
            return
        #transmission possible
        if random.random() < self.P_Transmit:
            other.infect()

    def hello(self, other):
        raise NotImplementedError("each class must implement hello")

    
    def _is_contagious(self) -> bool:
        """COVID 19 apparently spreads before the individual is symptomatic."""
        return (self.state == Health.symptomatic
                or self.state == Health.asymptomatic)

    def infect(self):
        """Called by another individual spreading germs. May also be called on "patient 0" to start simulation."""
        if self.state == Health.vulnerable:
            self.next_state = Health.asymptomatic

class Population(mvc.Listenable):
    def __init__(self, nrows: int, ncols: int):
        super().__init__()
        self.cells = []
        self.nrows = nrows
        self.ncols = ncols
        for row in range(config.get_int("Grid", "Rows")):
            row_list = []
            for col in range(config.get_int("Grid", "Cols")):
                row.append(Typical(self, row, col))
            self.cells.append(row_list)
        return

    def seed(self):
        """patient zero"""
        row = random.randint(0,self.nrows-1)
        col = random.randint(0,self.ncols-1)
        self.cells[row][col].infect()
        self.cells[row][col].tick()


    def count_in_state(self, state: "Health") -> int:
        """individuals in passed in state"""
        count = 0
        for row in self.cells:
            for col in row:
                if col.state == state:
                    count += 1
        return count
    
    def _random_individual(self, row: int, col: int) -> "Individual":
        classes = [(AtRisk, config.get_float("Grid", "Proportion_AtRisk")),
                   (Typical, config.get_float("Grid", "Proportion_Typical"))]
        while True:
            for the_class, proportion in classes:
                dice = random.random()
                if dice < proportion:
                    return the_class(self, row, col)


    def neighbors(self, num: int, row: int, col: int, dist: int) -> List[Tuple[int, int]]:
       """Give me addresses of up to num neighbors
       up to dist away from here(Manhattan distance)
       """
       result = []
       count = 0
       attempts = 0
       while count < num:
           attempts += 1
           if attempts >= 1000:
               raise ValueError(f"Can't find {num} neighbors at distance {dist}")
           row_step = random.randint(0-dist,dist)
           col_step = random.randint(0-dist,dist)
           row_addr = row + row_step
           col_addr = col + col_step
           if row_addr < 0 or row_addr >= self.nrows or col_addr < 0 or col_addr >= self.ncols or (row_addr == row and col_addr == 0):
               continue
           neighbor_addr = (row_addr, col_addr)
           if neighbor_addr in result:
               continue
           result.append(neighbor_addr)
           count += 1
       return result

    def step(self):
        """determine next states"""
        for row in self.cells:
            for cell in row:
                cell.step()
        for row in self.cells:
            for cell in row:
                cell.tick()
        self.notify_all("timestep")


    def visit(self, address: Tuple[int, int]):
        """Who lives there?"""
        row_num, col_num = address
        return self.cells[row_num][col_num]

class Typical(Individual):
    """Typical individual. May visit different neighbors each day."""
    def __init__(self, region: "Population", row: int, col: int):
        super().__init__("Typical", region, row, col)
    
    def hello (self, other):
        return True

    def social_behavior(self):
        if random.random() < self.P_Visit:
            addr = random.choice(self.neighbors)
            neighbor = self.region.visit(addr)
            if neighbor.hello(self):
                neighbor.meet(self)

class Wanderer(Individual):
    def __init__(self, region: "Population", row: int, col: int):

        super().__init__("Wanderer", region, row, col)

    def social_behavior(self):
        if random.random() < self.P_Visit:
            addr = random.choice(self.neighbors)
            neighbor = self.region.visit(addr)
            if neighbor.hello(self):
                neighbor.meet(self)

    def hello(self, other) -> bool:
        return True
    
    
class AtRisk(Individual):
    """Immunocompromised or elderly.
    Vulnerable and cautious.
    """
    def __init__(self, region: "Population", row: int, col: int):
        # Much of the constructor has been "factored out" into
        # the abstract base class
        super().__init__("AtRisk", region, row, col)
        self.prior_visit = None
    

    def social_behavior(self):
        """The way an AtRisk individual interacts with neighbors"""
        if random.random() >= self.P_Visit:
            # No visits today! 
            return
        if self.prior_visit is None:
            # Time for someone new
            addr = random.choice(self.neighbors)
            neighbor = self.region.visit(addr)
            self.prior_visit = neighbor
        else:
            # Second visit to the same person
            neighbor = self.prior_visit
            self.prior_visit = None
        if neighbor.hello(self):
            neighbor.meet(self)


    def hello (self, other: "Individual") -> bool:
        return (other.row, other.col) in self.neighbors