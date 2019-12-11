# A python program to draw line through points
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt

def do_regression():
    fig,ax = plt.subplots()
    fig.set_size_inches(10,6)
    X = [1,3,5,7]
    Y = [1,5,4,11]

    # Plot the data
    for xy in zip(X,Y):
        ax.scatter(xy[0],xy[1], color="blue")

    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    # Compute the variance of X
    SSxx = sum([(x - x_mean)**2 for x in X])
    
    Z = zip(X,Y)

    # Compute the covariance of X and Y...
    SSxy = sum([(z[0]-x_mean) * (z[1]-y_mean) for z in Z])

    # Compute the slope and y-intercept
    m = SSxy/SSxx
    b = y_mean - (m * x_mean)
    print("y = {}x + {}".format(m,b))
    rx = [min(X)-1,max(X)+1]
    ry = [m*s + b for s in rx]

    #Plot the line
    line = Line2D(rx,ry)
    ax.add_line(line)
    plt.show()
    
if __name__ == '__main__':
    do_regression()