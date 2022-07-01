import localminima.testfunctions.testfunctions as tf
import localminima.opt.opt as opt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot_results(support, func, inits, minima):

    x1 = np.linspace(support[0][0], support[0][1], 100)
    x2 = np.linspace(support[1][0], support[1][1], 100)

    X1, X2 = np.meshgrid(x1, x2)

    F = func([X1, X2])

    _, ax = plt.subplots(1, 1)
    ax.contourf(X1, X2, F, 20)
    plt.contour(X1, X2, F, 20, colors="black")
    ax.set_title("Filled Contours Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    for p in inits:
        plt.plot([p[0]], [p[1]], marker="o", markersize=4, color="g")
    for r in list(minima):
        plt.plot([r[0]], [r[1]], marker="x", markersize=15, color="r")
    plt.tight_layout()
    plt.savefig("./artifacts/plot.png")


def init_grid(support, npoints_per_dim=10):
    x1 = np.linspace(support[0][0], support[0][1], npoints_per_dim)
    x2 = np.linspace(support[1][0], support[1][1], npoints_per_dim)

    X1, X2 = np.meshgrid(x1, x2)
    return np.vstack([X1.flatten(), X2.flatten()]).T


support = [[-5, 5], [-5, 5]]  # x-dim  # y-dimension

inits = init_grid(support)

findlocalminima = opt.FindLocalMinima(inits, n_cores=2)

result_hb = findlocalminima.execute_parallel(tf.himmelblau)

plot_results(support, tf.himmelblau, findlocalminima.inits, result_hb)
