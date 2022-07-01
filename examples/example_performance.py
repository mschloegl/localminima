import localminima.testfunctions.testfunctions as tf
import localminima.opt.opt as opt
import time
import numpy as np
import multiprocessing
import logging

logging.basicConfig(
    filename="artifacts/performance.log", level=logging.DEBUG, filemode="w"
)

ncores = multiprocessing.cpu_count()


def init_grid(support, npoints_per_dim=10):
    x1 = np.linspace(support[0][0], support[0][1], npoints_per_dim)
    x2 = np.linspace(support[1][0], support[1][1], npoints_per_dim)

    X1, X2 = np.meshgrid(x1, x2)
    return np.vstack([X1.flatten(), X2.flatten()]).T


support = [[-5, 5], [-5, 5]]

inits = init_grid(support)

findlocalminima = opt.FindLocalMinima(inits, n_cores=ncores)

logging.info("Evaluating Himmelblau function")
start = time.time()
result_hb = findlocalminima.execute_parallel(tf.himmelblau)
logging.info(f"Parallel Execution took: {time.time()-start} s ")

start = time.time()
result_hb_seq = findlocalminima.execute_sequential(tf.himmelblau)
logging.info(f"Sequential Execution took: {time.time()-start} s ")

logging.info("--------------------------------------------")

support = [[-10, 10], [-10, 10]]

inits = init_grid(support, 50)

findlocalminima.set_inits(support)

logging.info("Evaluating Hoeldertable function")

start = time.time()
result_ht = findlocalminima.execute_parallel(tf.hoeldertable)
logging.info(f"Parallel Execution took: {time.time()-start} s ")

start = time.time()
result_ht_seq = findlocalminima.execute_sequential(tf.hoeldertable)
logging.info(f"Sequential Execution took: {time.time()-start} s ")
