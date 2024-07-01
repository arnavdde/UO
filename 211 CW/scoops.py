class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
    
    def __str__(self) -> str:
        return f"{self.flavor}"
    
    def __repr__(self) -> str:
        return f"Scoop - {self.flavor}"

def create_scoops(flavors):
    scoops = [Scoop(x) for x in flavors]
    return scoops

def print_scoops(scoops):
    for scoop in scoops:
        print(f"flavor = {scoop}")

if __name__ == "__main__":
    one_scoop = Scoop("cinnamon")
    print(one_scoop)
    flavors = ["chocolate", "vanilla", "persimmon"]
    sc = create_scoops(flavors)
    print(sc)
    print_scoops(sc)