# localminima
Find and return local minima

## General comment

The vectorization for multiple starting points is based on employing pythons multiprocessing package. As optimization proceedure an **Nelder-Mead** simplex algorithm is used from the **scipy** package. 

## Setup
Assuming you have docker installed you can build the image with a controlled python environment based on poetry by running

```
./build_image.sh
```

## Executing scripts

To reproduce the performance evaluation and visulization artifacts saved in the artifacts folder you can run

```
./run_dockerized example_performance.py
```

and

```
./run_dockerized example_visualize.py
```

The performance evaluation is carried out on two different test functions with different numbers of starting points on a equally spaced grid of defined support for the maximum number of cores specified on the available machine. For 8 cores the speedup is roughly a factor of 4 in the first example but the parallelization would benefit strongly by using cloud computation with many cores, minimizing computation time.

A visualization is provided in **artifacts/plot.png** for the **Himmelblau** function. The inital grid is shown with green dots and the found minima are displayed as red crosses and correspond to the known 4 local minima for this function on the given support.


