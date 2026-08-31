import csv
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
y = np.sin(t)

plt.plot(t, y)
plt.xlabel("time (s)")
plt.ylabel("angle (rad)")
plt.grid(True)
plt.savefig("joint_angle.png", dpi=120)

with open("log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "angle"])
    for ti, yi in zip(t, y):
        writer.writerow([round(ti, 4), round(yi, 4)])

print("saved: joint_angle.png, log.csv")   # 눈으로 확인할 한 줄
