import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')

# Draw a line in a diagram from position (0, 0) to position (6, 250)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

# Show the plot (optional)
plt.show()

# Save the plot as an image
plt.savefig('line_plot.png')

# Flush the stdout buffer
sys.stdout.flush()