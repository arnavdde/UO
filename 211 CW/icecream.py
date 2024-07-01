class IceCream():
    def __init__(self, flavors):
        self.scoops = [Scoop(x) for x in flavors]
    
    def __str__(self):
        order_str = "ice cream with flavors"
        for scoop in self.scoops:
            order_str += f"{scoop}, "
        return order_str[:-2]

if __name__ == "__main__":
    

