import os
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
y = np.sin(t)

plt.plot(t, y)
plt.xlabel("time (s)")
plt.ylabel("angle (rad)")
plt.title("joint angle")
plt.grid(True)
plt.savefig("joint_angle.png", dpi=120)
print("backend:", plt.get_backend())
print("saved:", os.path.abspath("joint_angle.png"))
