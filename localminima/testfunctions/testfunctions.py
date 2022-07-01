import numpy as np


def rosenbrock(X, b=10.0):
    x, y = X
    return (1 - x) ** 2 + b * (y - x**2) ** 2


def himmelblau(X, a=-11.0, b=-7.0):
    x, y = X
    return (x**2 + y + a) ** 2 + (x + y**2 + b) ** 2


def hoeldertable(X):
    x, y = X
    return -np.abs(
        np.sin(x) * np.cos(y) * np.exp(np.abs((1 - np.sqrt((x**2 + y**2))) / np.pi))
    )


def easy_func(x):
    x = x**2 + 2 * np.sin(x * np.pi)
    return x
