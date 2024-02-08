import matplotlib.pyplot as plt
import numpy as np


def plotting_xy():
    """
        Plot a line between two points using Matplotlib.

        The function utilizes Matplotlib's plot() function to draw a line between two points in a diagram.

        Parameters:
            - xpoints: Array of x-coordinates for the two points.
            - ypoints: Array of y-coordinates for the two points.

        Example:
            If xpoints = [1, 8] and ypoints = [3, 10], the function plots a line from (1, 3) to (8, 10).
    """
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()


def plotting_without_line():
    """
        To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
    """
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints, 'o')
    plt.show()


def multiple_points():
    """
        Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
    """
    xpoints = np.array([1, 2, 6, 8])
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(xpoints, ypoints)
    plt.show()


def default_x_points():
    """
        If we don't specify the points on the x-axis, they will
        get the default values 1, 2, 3, etc, depending on the length of the y-points.
    """
    ypoints = np.array([3, 8, 1, 10, 5, 7])

    plt.plot(ypoints)
    plt.show()


if __name__ == "__main__":
    pass
    multiple_points()
