import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def print_graph(x_cor, x_width, y_cor, y_height):
    sample_data = np.ones((40,40),dtype=int)
    sample_data[y_cor:y_cor+y_height,x_cor:x_cor+x_width] = 0
    sample_data = pd.DataFrame(sample_data)
    cmap = plt.cm.colors.ListedColormap(['white', 'green'])
    fig, ax = plt.subplots()

    # Plot the array with 0 as white and 1 as green
    im = ax.imshow(sample_data, cmap=cmap, interpolation='none')
    ytick_labels = ax.get_yticks().astype(int)[::-1]
    ax.set_yticklabels(ytick_labels)

    # Show the plot
    plt.show()
    print(sample_data)

horizontal_cor = 20
horizontal_width = 10
vertical_cor  = 0
vertical_height = 25
print_graph(horizontal_cor, horizontal_width, vertical_cor, vertical_height)