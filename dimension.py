# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Create axis
x_length = 20
y_length = 10
z_length = 250
down_scale = 10
axes = [x_length//down_scale,y_length//down_scale,z_length//down_scale]

# Create Data
data = np.ones(axes, dtype=np.bool_)

# Control Transparency
alpha = 0.9

# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

# colors[0] = [1, 0, 0, alpha] # red
# colors[1] = [0, 1, 0, alpha] # green
# colors[2] = [0, 0, 1, alpha] # blue
# colors[3] = [1, 1, 0, alpha] # yellow
# colors[4] = [1, 1, 1, alpha] # grey
colors[:] = [1,0,0, alpha]
# colors[1,:,:,0:3] = 0
# turn black
data[1,:,:] = False

# Plot figure
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(111, projection='3d')

# Voxels is used to customizations of
# the sizes, positions and colors.
ax.voxels(data, facecolors=colors, edgecolors='grey')

plt.show()