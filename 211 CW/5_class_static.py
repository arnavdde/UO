import math

class Fruit:
    name = 'Fruits'

    def __init__(self, name:str) -> None:
        self.name = name
    
    @classmethod
    def printName(cls): #cls receives class rather than object/instance
        print(f"A class method: {cls}")
        print(f"Name: {cls.name}")

    
class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

if __name__ == "__main__":
    Fruit.printName() #class method called on class itself, not instance

    Music.play()
    m = Music()
    m.stop()

