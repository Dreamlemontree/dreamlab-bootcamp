import matplotlib.pyplot as plt
import numpy as np
import csv

t = np.linspace(0, 10, 100)
y = np.sin(t)

plt.plot(t, y)
plt.xlabel("time (s)")
plt.ylabel("angle (rad)")
plt.savefig("joint_angle.png")

with open("log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "angle"])
    for i, ti in enumerate(t):
        writer.writerow([ti, y[i]])
