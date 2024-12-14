from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import reduce
from pynput import keyboard

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import operator
import math
import re

l = open('input.txt').read().strip().split('\n')
p = r"-?\d+"

COL = 101
ROW = 103
q = [((0, 0), (49, 50)), ((51, 52), (100, 102)), ((51, 0), (100, 50)), ((0, 52), (49, 102))]
coords, where_now = [], []
total_steps = math.lcm(COL, ROW)

class RobotSimulation:
    def __init__(self, main):
        self.main = main
        self.main.title("Robot Simulation")
        self.helper = 0 # 6512
        self.dig = False

        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main)
        self.canvas.get_tk_widget().pack()

        self.main.bind('<space>', self.next_step)
        self.main.bind('<Escape>', self.quit)

        self.update_plot()

    def update_plot(self):
        where_now = []
        matrix = np.zeros((ROW, COL))

        for x, y, dx, dy in coords: where_now.append(((x + dx * self.helper) % COL, (y + dy * self.helper) % ROW))
        for x, y in where_now: matrix[y, x] = 1

        self.ax.clear()
        self.ax.imshow(matrix, cmap='gray', vmin=0, vmax=1)

        if self.dig:
            self.ax.axvline(x=COL // 2, color='green', linewidth=2)
            self.ax.axhline(y=ROW // 2, color='green', linewidth=2)

        self.ax.set_title(f'Step: {self.helper}')
        self.ax.set_xlabel('Columns')
        self.ax.set_ylabel('Rows')
        self.canvas.draw()

    def next_step(self, event):
        self.main.quit() if self.helper > total_steps else self.update_plot()
        self.helper = (self.helper + 1)

    def quit(self, event): self.main.quit()

# part 1

for ll in l: coords.append(tuple(map(int, re.findall(p, ll))))
for x, y, dx, dy in coords: where_now.append(((x+dx*100)%COL, (y+dy*100)%ROW))
qd = list(map(lambda quad: sum(1 for x, y in where_now if x != 50 and y != 51 and quad[0][0] <= x <= quad[1][0] and quad[0][1] <= y <= quad[1][1]), q))
print(reduce(operator.mul, qd, 1))

def run_app():
    main1 = tk.Tk()
    app1 = RobotSimulation(main1)
    app1.helper = 100
    app1.dig = True
    app1.update_plot()
    # main1.after(3000, main1.destroy)
    main1.mainloop()
run_app()

# part 2
main2 = tk.Tk()
app2 = RobotSimulation(main2)
main2.mainloop()
