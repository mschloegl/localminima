from scipy import optimize
import multiprocessing
import numpy as np
from functools import partial


class FindLocalMinima:
    def __init__(self, inits, n_cores=4, npoints_per_dim=10):

        self.inits = list(inits)

        self.pool = multiprocessing.Pool(processes=n_cores)

    @staticmethod
    def _postprocess_opt_output(minima):
        return np.array(
            [
                m["x"]
                for m in minima
                if m["message"] == "Optimization terminated successfully."
            ]
        )

    @staticmethod
    def _minimize(func, x0):
        return optimize.minimize(func, x0, method="Nelder-Mead")

    def set_inits(self, inits):
        self.inits = list(inits)

    def execute_parallel(self, func):

        outputs = self.pool.map(partial(self._minimize, func), self.inits)

        return self._postprocess_opt_output(outputs)

    def execute_sequential(self, func):

        outputs = [self._minimize(func, x0) for x0 in self.inits]

        return self._postprocess_opt_output(outputs)
