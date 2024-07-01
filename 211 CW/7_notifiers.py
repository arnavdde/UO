class M:
    def __init__(self) -> None:
        self.the_V = None

    def hookup(self, v: 'V'):
        print("M.hookup: I'm about to")
        self.the_V = v

    def f(self):
        
