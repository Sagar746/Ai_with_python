import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Define the x range
x = np.linspace(-5,5,100)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

# plot a graph
plt.figure(figsize=(8,6))

plt.plot(x, y1, label=r'$y=2x+1$', color='blue', linestyle='-', linewidth='2')
plt.plot(x, y2, label=r'$y=2x+2$', color='green', linestyle='--', linewidth='2')
plt.plot(x, y3, label=r'$y=2x+3$', color='red', linestyle=':', linewidth='2')

plt.title('Graph of y=2x+1, y=2x+2, y=2x+3', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

plt.legend()

plt.grid(True)
plt.show()

