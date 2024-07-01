class Scoop:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.__size = size
        self.__private = 'unaccessible value'

    def __str__(self) -> str:
        return f"scoop({self.flavor}, {self.size}, {self.__private})"
    
    @property #defines a method as a getter for an attribute, called a decorator
    def size(self):
        return self.__size
    
    @size.setter #this decorator defines a method as a setter
    def size(self, size):
        self.__size = size
    
if __name__ == "__main__":
    one_scoop = Scoop("cinnamon", "small") 
    
    print(one_scoop)

    print(one_scoop.size)
    
    print(f"in main: size = {one_scoop.size}")

    # print(one_scoop.__private)

#    # print(one_scoop.__size)
#    # ERR - size is private, cannot be accessed directly
#    print(one_scoop.__Scoop__size)


