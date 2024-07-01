import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MH:
    def __init__(self) -> None:
        self.n_doors = 3
        self.n_trials = 0
        self.n_sw = 0
        self.sw_w_n = 0
        self.sw_w = []
        self.st_w_n = 0
        self.st_w = []
    
    def __str__(self) -> str:
        return (f"MH problem\n"
                f"  n_doors = 3\n"
                f"  n_trials = {self.n_trials}\n"
                f"  n_sw = {self.n_sw}\n"
                f"  sw_w_n = {self.sw_w_n}\n"
                f"  sw_w [0] = {self.sw_w[:1]}...\n"
                f"  st_w_n = {self.st_w_n}\n"
                f"  st_w [0] = {self.st_w[:1]}...")

    def trial(self, verbose=False):
        doors = [0, 1, 2]
        removed = []
        correct = random.choice(doors)
        chosen = random.choice(doors)
        open = None

        for door in doors:
            if door != chosen and door != correct:
                open = door
                break
        
        switched = random.choice([True, False])
        if switched:
            for door in doors:
                if door != chosen and door != open:
                    switch = door
                    break
        else:
            switch = chosen
        
        if switch == correct:
            sw_d = True
        else:
            sw_d = False
        
        self.update(switched, chosen, correct, sw_d)

    def update(self, sw_d, chosen_door, correct_door, switched):
        self.n_trials += 1
        
        if switched:
            self.n_sw += 1
            if sw_d == correct_door:
                self.sw_w_n += 1
                current_sw_freq = self.sw_w_n / self.n_sw
            else:
                current_sw_freq = self.sw_w_n / self.n_sw if self.n_sw > 0 else 0
            self.sw_w.append(current_sw_freq)
        else:
            last_sw_freq = self.sw_w[-1] if self.sw_w else 0
            self.sw_w.append(last_sw_freq)

        if not switched:
            if chosen_door == correct_door:
                self.st_w_n += 1
            current_st_freq = self.st_w_n / (self.n_trials - self.n_sw) if (self.n_trials - self.n_sw) > 0 else 0
            self.st_w.append(current_st_freq)
        else:
            last_st_freq = self.st_w[-1] if self.st_w else 0
            self.st_w.append(last_st_freq)

    def experiment(self, nt=10):
        for i in range(nt):
            self.trial(self)

    def plot(self):
        plt.plot(range(1, self.n_trials + 1), self.sw_w, label="Switch", color='red')
        plt.plot(range(1, self.n_trials + 1), self.st_w, label="No Switch", color='blue')

        plt.xlabel("n")
        plt.ylabel("Prob")
        plt.title("Monty Hall Simulation")

        plt.legend()
        plt.grid(True)
        plt.savefig('mh_1000.png')
        plt.show()

    def animate_plot(self):
        fig, ax = plt.subplots()
        x = []
        y = []

        def animate(i):
            if i < len(self.sw_w): 
                x.append(i)
                y.append(self.sw_w[i])
                ax.clear()
                ax.plot(x, y, color='red')
                ax.set_xlabel("n")
                ax.set_ylabel("prob")
                ax.set_title("Monty Hall Simulation")

        ani = FuncAnimation(fig, animate, frames=len(self.sw_w), interval=30, repeat=False)
        plt.show()
    
if __name__ == "__main__":
    random.seed(42)
    mh = MH()
    print(mh)

    # mh.trial()
    # print(mh)
    # mh.trial()
    # print(mh)
    # mh.trial()
    # print(mh)
    mh.experiment(1000)
    print(mh)

    mh.plot()

    mh.animate_plot()
